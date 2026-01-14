# controller or business logic
# funções comuns a todos os módulos

import os
from flask import send_from_directory, current_app
from utils.logger import logger


class geralController:
    __connection = None
    app = None

    def __init__(self):
        pass

    def formataNumero(self, num, moeda=None):
        # recebe um valor numerico, devolve string formatada
        # substitui ponto decimal por virgula e coloca ponto nos milhares
        # se valor recebido for zero, devolve branco
        # se o parametro 'moeda' for informado acrescenta no inicio da string.
        if num is None:
            return 0
        numS = ' '

        if moeda != None:
            moeda = moeda + ' '
        else:
            moeda = ''

        if num != 0:
            numS = moeda + \
                "{:,.2f}".format(num).replace(",", "X").replace(
                    ".", ",").replace("X", ".")

        return numS

    def formataPerc(self, num, zeros=None):
        # recebe um valor numerico, devolve string formatada
        # substitui ponto decimal por virgula
        # se valor recebido for zero, devolve branco ou
        # se parametro 'zeros' for informado devolve '0,00%'

        numS = ' '

        if num != 0:
            numS = "{:,.2f}".format(num).replace(
                ",", "X").replace(".", ",").replace("X", ".") + '%'
        elif zeros != None:
            numS = zeros
            numS = "{:,.2f}".format(num).replace(
                ",", "X").replace(".", ",").replace("X", ".") + '%'
        return numS

    def formatammmaa(self, mes, ano):
        # recebe um numerico de mes (nn) e ano (nnnn), devolve mmm/aa

        mmm = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
               'jul', 'ago', 'set', 'out', 'nov', 'dez']
        aa = ano[2:4]
        mmmaa = mmm[int(mes)-1] + '/' + aa

        return mmmaa

    def listar_arquivos_com_prefixo(self, diretorio, prefixo):

        #        print('----------- listar_arquivos_com_prefixo -------------')
        #        print('++++++++++++++++++++++', diretorio, prefixo )
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        docs = os.listdir(diretorio)
        result = []
        logger.info(
            f"Listando arquivos no diretório: {diretorio} com prefixo: {prefixo}")
        logger.info(f"Arquivos encontrados: {docs}")
        for arquivo in docs:
            if arquivo.startswith(prefixo) and os.path.isfile(os.path.join(diretorio, arquivo)):
                result.append(arquivo)
        logger.info(f"Arquivos filtrados: {result}")
        return result

    def download_arquivo(self, arquivo):
        diretorio = os.path.join(current_app.config['DIRSYS'], 'Relatorios')
#        print ('+++++++++++++', arquivo)
        return send_from_directory(os.path.normpath(diretorio), arquivo, as_attachment=True)
