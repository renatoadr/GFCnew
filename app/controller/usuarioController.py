# controller or business logic
# Trata base de USUARIOS

from utils.dbContext import MySql
from dto.usuario import usuario
from dto.empreendimento import empreendimento
import bcrypt


class usuarioController:

    def lista_usuarios(self):
        query = f"SELECT id_usuario, email, tp_acesso, nm_usuario FROM {MySql.DB_NAME}.tb_usuarios ORDER BY id_usuario"
        users = MySql.getAll(query)
        list = []
        for row in users:
            user = usuario()
            user.setIdUsuario(row.get('id_usuario'))
            user.setEmail(row.get('email'))
            user.setTpAcesso(row.get('tp_acesso'))
            user.setNmUsuario(row.get('nm_usuario'))
            list.append(user)
        return list

    def consultarAcesso(self, email, senha):
        query = f"SELECT id_usuario, email, senha, tp_acesso, nm_usuario, salt FROM {MySql.DB_NAME}.tb_usuarios WHERE email = %s"

        linha = MySql.getOne(query, (email,))

        if linha:
            senhaSalva = self.encrypt(linha.get('senha'), linha.get('salt'))
            senhaInformada = self.encrypt(senha, linha.get('salt'))

            if senhaInformada == senhaSalva:
                user = usuario()
                user.setIdUsuario(linha.get('id_usuario'))
                user.setEmail(linha.get('email'))
                user.setSenha(linha.get('senha'))
                user.setTpAcesso(linha.get('tp_acesso'))
                user.setNmUsuario(linha.get('nm_usuario'))
                return user

        return None

    def consultarApelidos(self, idUsuario):
        query = f"""SELECT * from {MySql.DB_NAME}.tb_empreendimentos emp
        INNER JOIN  {MySql.DB_NAME}.tb_usuario_empreendimento user
        ON user.id_empreendimento = emp.id_empreendimento
        WHERE user.id_usuario = %s
        ORDER BY emp.apelido"""

        lista = MySql.getAll(query, (idUsuario,))
        listaA = []

        for x in lista:
            e = empreendimento()
            e.setApelido(x['apelido'])
            e.setNmConstrutor(x['nm_construtor'])
            e.setNmEmpreend(x['nm_empreendimento'])
            e.setNmIncorp(x['nm_incorporador'])
            e.setLogradouro(x['logradouro'])
            e.setCidade(x['cidade'])
            e.setBairro(x['bairro'])
            e.setEstado(x['estado'])
            e.setCep(x['cep'])
            listaA.append(e)

        return listaA

    def encrypt(self, senha: str, salt=bcrypt.gensalt(6)) -> str:
        return bcrypt.hashpw(senha, salt)
