from flask import Blueprint, request, render_template, current_app, redirect, flash, jsonify, send_file
from utils.logger import logger
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from utils.converter import converterStrToInt
from PIL import Image, ImageDraw, ImageFont, ImageFile
from utils.helper import criaPastas
import ast
import os
import re

foto_bp = Blueprint('fotos', __name__)

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
    ('Perspectiva', 'perspectiva', 'perspectiva'),
    ('Foto Atual', 'fotoAtual', 'foto_atual'),
    ('Evolução 3D 1', 'evolucao3D1', 'evolucao_3D_1'),
    ('Evolução 3D 2', 'evolucao3D2', 'evolucao_3D_2')
)


@foto_bp.route('/upload_config_fotos')
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
        listVigencias.append((f"{months[mes.zfill(2)]}/{ano}", folder))

    listVigencias.reverse()

    return render_template("upload_fotos_config.html", camposCapa=camposCapa, listVigencias=listVigencias)


@foto_bp.route('/upload_fotos', methods=['POST'])
def upload_fotos():
    vigCurrent = request.form.get('vigCorrrente')
    qtdFotosObra = converterStrToInt(request.form.get("qtdObra"))
    qtd3D = converterStrToInt(request.form.get("qtd3D"))
    capa = request.form.getlist("capa")
    mesV = converterStrToInt(request.form.get('mesVigencia'))
    anoV = converterStrToInt(request.form.get('anoVigencia'))

    if vigCurrent is None and (mesV is None or mesV == 0 or anoV is None or anoV == 0):
        return redirect('/upload_config_fotos')

    if qtdFotosObra > 0:
        qtdFotosObra += 1

    if qtd3D > 0:
        qtd3D += 1

    if vigCurrent is not None:
        ano, mes = vigCurrent.split('_')
        mesV = mes
        anoV = ano

    camposTelaCapa = []

    if capa is not None:
        for label, value, name in camposCapa:
            if value in capa:
                camposTelaCapa.append((label, value, name))

    fotosCarregadas = carregarImagens(vigCurrent)

    return render_template(
        "upload_fotos.html",
        camposCapa=camposTelaCapa,
        qtd3D=qtd3D,
        qtdObra=qtdFotosObra,
        mesV=mesV,
        anoV=anoV,
        fotosCarregadas=fotosCarregadas
    )


@foto_bp.route('/upload_arquivo_fotos', methods=['POST'])
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


@foto_bp.route('/api/imagens/vigencia_corrente', methods=['GET'])
def api_files():
    vigCurrent = request.args.get('vig')
    return jsonify(carregarImagens(vigCurrent))


@foto_bp.route('/obter_imagem/<idEmpreend>/<vigencia>/<nameFile>')
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
            img = redimensionar(file)
            img.filename = file.filename
            if not saveFile(img, path, nameFile):
                flash(
                    f"Ouve um erro ao tentar salvar a imagem para o campo {label}")


def saveFile(file: ImageFile, path, nameFile):
    try:
        if file and file.filename.lower().endswith(('png', 'jpg', 'jpeg')):
            name, ext = os.path.splitext(file.filename)
            filePath = os.path.normpath(f"{path}/{nameFile}{ext}")
            if os.path.exists(filePath):
                os.remove(filePath)
            file.save(filePath)
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
    font = ImageFont.truetype('arial.ttf', fontSize)
    while draw.textlength(desc.capitalize(), font) > img.width:
        fontSize -= 2
        font = ImageFont.truetype('arial.ttf', fontSize)

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


def redimensionar(file):
    img = file
    try:
        img = Image.open(file)
    except:
        pass
    nSize = 700
    nWidth = 0
    nHeight = 0

    if img.width > img.height:
        razao = nSize / img.width
        nWidth = nSize
        nHeight = img.height * razao
    elif img.width < img.height:
        razao = nSize / img.height
        nHeight = nSize
        nWidth = img.width * razao
    else:
        nWidth = nSize
        nHeight = nSize
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
                img = redimensionar(file)
                img = escreverNaImagem(img, desc)
                img.filename = file.filename
                if not saveFile(img, path, nameFile):
                    flash(
                        f"Ouve um erro ao tentar salvar a imagem para o campo {label}")
