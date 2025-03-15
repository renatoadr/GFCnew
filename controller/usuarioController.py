#controller or business logic
# Trata base de USUARIOS

import os
from flask import Flask, send_from_directory, jsonify
from utils.dbContext import MySql
from dto.usuario import usuario
from dto.empreendimento import empreendimento

class usuarioController:
    __connection = None

    def __init__(self):
        pass

    def consultarAcesso(self, email, senha):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

        query =  "select id_usuario, email, senha, tp_acesso, nm_usuario from " + MySql.DB_NAME + ".tb_usuarios where email = '" + email + "' and senha = '" + senha + "'"

#        print(query)

        cursor.execute(query)

        linha = cursor.fetchone()
#        print('++++++++++++ consultarAcesso +++++++++++++++')
#        print (cursor)
#        print (linha)
#        print('+++++++++++++++++++++++++++')

        if linha:
#            print('++++++++++++ passou aqui no usuario +++++++++++++')
            itens = usuario()
            itens.setIdUsuario(linha.get('id_usuario'))
            itens.setEmail(linha.get('email'))
            itens.setSenha(linha.get('senha'))
            itens.setTpAcesso(linha.get('tp_acesso'))
            itens.setNmUsuario(linha.get('nm_usuario'))
            cursor.close()
            MySql.close(self.__connection)
            return itens
        else:
            return None

    def consultarApelidos(self, idUsuario):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

#       print('---consultarApelidos--')
#       print(idUsuario)

        query = "select * from " + MySql.DB_NAME + ".tb_empreendimentos E inner join  " + MySql.DB_NAME + """.tb_usuario_empreendimento U on U.id_empreendimento = E.id_empreendimento where U.id_usuario = %s order by E.apelido"""

#       print(query)
#       print('-----------------')

        cursor.execute(query, (idUsuario,))

        lista = cursor.fetchall()
        listaA = []

        for x in lista:
            e = empreendimento()
            e.setApelido(x['apelido'])
            e.setNmConstrutor(x['nm_construtor'])
            e.setNmEmpreend(x['nm_empreendimento'])
            e.setNmEngenheiro(x['nm_engenheiro'])
            e.setNmIncorp(x['nm_incorporador'])
            e.setLogradouro(x['logradouro'])
            e.setCidade(x['cidade'])
            e.setBairro(x['bairro'])
            e.setEstado(x['estado'])
            e.setCep(x['cep'])
            listaA.append(e)

#       print('listaA  ', listaA)
#       print('---consultarApelidos--')
#       print('------ FIM -------')

        cursor.close()
        MySql.close(self.__connection)
        return listaA


