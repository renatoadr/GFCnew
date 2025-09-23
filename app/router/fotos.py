from utils.security import login_required
from flask import Blueprint, request, render_template, current_app, redirect, flash, jsonify, send_file
from utils.logger import logger
from utils.CtrlSessao import IdEmpreend, NmEmpreend, Vigencia
from utils.converter import converterStrToInt
from PIL import Image, ImageDraw, ImageFont, ImageFile
from utils.helper import criaPastas
import ast
import os
import re

fotos_bp = Blueprint('fotos', __name__)

SIZE_IMAGE = (1280, 720)

months = {
    "01": "Jan",
    "02": "Fev",
    "03": "Mar",
    "04": "Abr",
    "05": "Mai",
    "06": "Jun",
    "07": "Jul",
    "08": "Ago",
    "09": "Set",
    "10": "Out",
    "11": "Nov",
    "12": "Dez",
}

camposCapa = (
    ('Foto Atual', 'fotoAtual', 'foto_atual'),
    ('Elétrica 3D', 'eletrica3D', 'eletrica_3D'),
    ('Hidráulica 3D', 'hidraulica3D', 'hidraulica_3D'),
    ('Evolução 3D', 'evolucao3D', 'evolucao_3D')
)


@fotos_bp.route('/upload_config_fotos')
@login_required
def upload_config_fotos():
    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (idEmpreend is None and not IdEmpreend().has()) or (nmEmpreend is None and not NmEmpreend().has()):
        return redirect('/home')

    if idEmpreend is None:
        idEmpreend = IdEmpreend().get()
    else:
        IdEmpreend().set(idEmpreend)

    if nmEmpreend is None:
        nmEmpreend = NmEmpreend().get()
    else:
        NmEmpreend().set(nmEmpreend)

    diretorio = getDir()

    listVigencias = []
    try:
        folders = os.listdir(diretorio)
    except:
        folders = []

    for folder in folders:
        if not os.path.isdir(os.path.join(diretorio, folder)):
            continue
        ano, mes = folder.split('_')
        mes = mes.zfill(2)
        if mes in months:
            listVigencias.append((f"{months[mes]}/{ano}", folder))

    listVigencias.reverse()

    return render_template("upload_fotos_config.html", camposCapa=camposCapa, listVigencias=listVigencias)


@fotos_bp.route('/upload_fotos', methods=['POST'])
@login_required
def upload_fotos():
    qtdFotosObra = converterStrToInt(request.form.get("qtdObra"))
    qtd3D = converterStrToInt(request.form.get("qtd3D"))
    capa = request.form.getlist("capa")
    vig = Vigencia().get()
    mesV = converterStrToInt(vig[1])
    anoV = converterStrToInt(vig[0])

    if qtdFotosObra > 0:
        qtdFotosObra += 1

    if qtd3D > 0:
        qtd3D += 1

    camposTelaCapa = []

    if capa is not None:
        for label, value, name in camposCapa:
            if value in capa:
                camposTelaCapa.append((label, value, name))

    fotosCarregadas = carregarImagens('_'.join(vig))

    return render_template(
        "upload_fotos.html",
        camposCapa=camposTelaCapa,
        qtd3D=qtd3D,
        qtdObra=qtdFotosObra,
        mesV=mesV,
        anoV=anoV,
        fotosCarregadas=fotosCarregadas
    )


@fotos_bp.route('/upload_arquivo_fotos', methods=['POST'])
@login_required
def upload_arquivo_fotos():
    mesV = request.form.get('mesVigencia')
    anoV = request.form.get('anoVigencia')
    capa = request.form.get('camposCapa')
    qtdObra = converterStrToInt(request.form.get('qtdObra'))
    qtd3D = converterStrToInt(request.form.get('qtd3D'))

    diretorio = getDir(f"{anoV}_{mesV}")

    if not criaPastas(diretorio):
        flash('Não foi possível criar as pastas')
        return redirect('/upload_fotos')

    if qtdObra > 0:
        qtdObra += 1

    if qtd3D > 0:
        qtd3D += 1

    for label, value, file in ast.literal_eval(capa):
        for label, field, name in camposCapa:
            if value == field:
                saveImage(label, field, name, diretorio)

    for idx in range(1, qtd3D):
        saveImage(f"Imagens 3D {idx}", f"foto_3D_{idx}",
                  f"foto_3D_{idx}", diretorio)

    for idx in range(1, qtdObra):
        saveImageObra(idx, diretorio)

    return redirect("/home")


@fotos_bp.route('/api/imagens/vigencia_corrente', methods=['GET'])
def api_files():
    vigCurrent = request.args.get('vig')
    return jsonify(carregarImagens(vigCurrent))


@fotos_bp.route('/obter_imagem/<idEmpreend>/<vigencia>/<nameFile>')
@login_required
def obter_imagem(idEmpreend, vigencia, nameFile):
    dirPath = os.path.abspath(__name__).replace(__name__, '')
    file = os.path.join(
        dirPath,
        current_app.config['DIRSYS'],
        idEmpreend,
        vigencia,
        nameFile
    )
    return send_file(file)


def carregarImagens(vigCurrent):
    if vigCurrent is None:
        return {}

    dir = getDir(vigCurrent)
    try:
        listFiles = os.listdir(dir)
    except:
        return {}
    files = [arq for arq in listFiles if os.path.isfile(os.path.join(dir, arq)) and (
        arq.lower().endswith(".jpg") or arq.lower().endswith(".png") or arq.lower().endswith(".jpeg"))]
    capaFiles = [arquivo for nome, campo, arquivo in camposCapa]
    imgs = {}

    for fileName in files:
        name, ext = fileName.split('.')
        if name in capaFiles or re.search(r"foto_3D_[\d]{1}", name) or re.search(r"foto_[\d]{1,2}", name):
            imgs[name] = f"{IdEmpreend().get()}/{vigCurrent}/{fileName}"
    return imgs


def getDir(path=None):
    nPath = os.path.join(current_app.config['DIRSYS'], IdEmpreend().get())
    if path is not None:
        nPath = os.path.join(nPath, path)
    return os.path.normpath(nPath)


def saveImage(label, fieldName, nameFile, path):
    if fieldName not in request.files:
        flash(f"Não foi encontrado imagem para o campo {label}")
    else:
        file = request.files.get(fieldName)
        if file:
            imgResize = redimensionar(file)
            img = background_image(imgResize)
            img.filename = file.filename
            if not saveFile(img, path, nameFile):
                flash(
                    f"Ouve um erro ao tentar salvar a imagem para o campo {label}")


def saveFile(file: ImageFile, path, nameFile):
    try:
        if file and file.filename.lower().endswith(('png', 'jpg', 'jpeg')):
            filePath = os.path.normpath(f"{path}/{nameFile}.png")
            if os.path.exists(filePath):
                os.remove(filePath)
            file.save(filePath, 'PNG')
            return True
        else:
            return False
    except Exception as error:
        logger.error('Erro ao salvar a imagem: %s', error)
        return False


def escreverNaImagem(file, desc):
    fontSize = 26
    img = file
    try:
        img = Image.open(file)
    except:
        pass

    draw = ImageDraw.Draw(img, 'RGBA')
    font = ImageFont.load_default(fontSize)
    while draw.textlength(desc.capitalize(), font) > img.width:
        fontSize -= 2
        font = ImageFont.load_default(fontSize)

    img.convert('RGBA')

    txtSize = draw.textlength(desc.capitalize(), font)
    draw.rectangle(
        [0, img.height - 50, img.width, img.height],
        fill=(0, 0, 0, int(255 * 0.75))
    )
    draw.text(
        ((img.width - txtSize) / 2, img.height - 40),
        desc.capitalize(),
        font=font,
        fill='white'
    )
    return img


def background_image(file: ImageFile) -> ImageFile:
    width, height = SIZE_IMAGE
    image_background = Image.new("RGB", (width, height), "white")
    pos_x = (width - file.width) // 2
    pos_y = (height - file.height) // 2
    image_background.paste(file, (pos_x, pos_y), file.convert("RGBA"))
    return image_background


def redimensionar(file):
    img = file
    try:
        img = Image.open(file)
    except:
        pass
    nWSize, nHSize = SIZE_IMAGE
    nWidth = 0
    nHeight = 0

    if img.width > img.height:
        razao = nWSize / img.width
        nWidth = nWSize
        nHeight = img.height * razao
    elif img.width < img.height:
        razao = nHSize / img.height
        nHeight = nHSize
        nWidth = img.width * razao
    else:
        nWidth = nWSize
        nHeight = nWSize
    return img.resize((int(nWidth), int(nHeight)))


def saveImageObra(idx, path):
    fieldName = f"fotosObra_{idx}"
    label = f"Foto da Obra {idx}"
    nameFile = f"foto_{idx}"
    fieldDesc = f"fotosObra_desc_{idx}"

    if fieldName not in request.files:
        flash(f"Não foi encontrado imagem para o campo {label}")
    else:
        file = request.files.get(fieldName)
        desc = request.form.get(fieldDesc)
        if not desc and file:
            if not saveFile(file, path, nameFile):
                flash(
                    f"Ouve um erro ao tentar salvar a imagem para o campo {label}")
        else:
            if file:
                imgResize = redimensionar(file)
                img = background_image(imgResize)
                img = escreverNaImagem(img, desc)
                img.filename = file.filename
                if not saveFile(img, path, nameFile):
                    flash(
                        f"Ouve um erro ao tentar salvar a imagem para o campo {label}")
