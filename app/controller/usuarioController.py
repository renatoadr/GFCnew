# controller or business logic
# Trata base de USUARIOS

from utils.dbContext import MySql
from dto.usuario import usuario
import bcrypt


class usuarioController:

    def lista_usuarios(self) -> list[usuario]:
        query = f"SELECT id_usuario, email, tp_acesso, nm_usuario, cod_banco FROM {MySql.DB_NAME}.tb_usuarios ORDER BY id_usuario"
        users = MySql.getAll(query)
        list = []
        for row in users:
            user = usuario()
            user.setIdUsuario(row.get('id_usuario'))
            user.setEmail(row.get('email'))
            user.setTpAcesso(row.get('tp_acesso'))
            user.setNmUsuario(row.get('nm_usuario'))
            user.setCodBanco(row.get('cod_banco'))
            list.append(user)
        return list

    def consultarAcesso(self, email: str, senha: str):
        query = f"SELECT id_usuario, email, senha, tp_acesso, nm_usuario, cod_banco FROM {MySql.DB_NAME}.tb_usuarios WHERE email = %s"

        linha = MySql.getOne(query, (email,))

        if linha:
            senhaSalva = linha.get('senha').encode('utf8')
            senhaInformada = senha.encode('utf8')

            if bcrypt.checkpw(senhaInformada, senhaSalva):
                user = usuario()
                user.setIdUsuario(linha.get('id_usuario'))
                user.setEmail(linha.get('email'))
                user.setTpAcesso(linha.get('tp_acesso'))
                user.setNmUsuario(linha.get('nm_usuario'))
                user.setCodBanco(linha.get('cod_banco'))
                return user

        return None

    def cadastrar_usuario(self, user: usuario):
        query = f"""INSERT INTO {MySql.DB_NAME}.tb_usuarios(email, senha, tp_acesso, nm_usuario, cod_banco) VALUE (%s, %s, %s, %s, %s)"""
        MySql.exec(query, (
            user.getEmail(),
            self.encrypt(user.getSenha().encode('utf8')),
            user.getTpAcesso(),
            user.getNmUsuario(),
            user.getCodBanco()
        ))

    def get_usuario_pelo_id(self, id: str) -> usuario:
        query = f"SELECT id_usuario, email, tp_acesso, nm_usuario, cod_banco FROM {MySql.DB_NAME}.tb_usuarios WHERE id_usuario = %s"

        linha = MySql.getOne(query, (id,))

        if linha:
            user = usuario()
            user.setIdUsuario(linha.get('id_usuario'))
            user.setEmail(linha.get('email'))
            user.setTpAcesso(linha.get('tp_acesso'))
            user.setNmUsuario(linha.get('nm_usuario'))
            user.setCodBanco(linha.get('cod_banco'))
            return user

        return None

    def atulizar_usuario(self, user: usuario):
        query = f"UPDATE {MySql.DB_NAME}.tb_usuarios SET nm_usuario = %s, email = %s, tp_acesso = %s, cod_banco = %s WHERE id_usuario = %s"
        MySql.exec(query, (
            user.getNmUsuario(),
            user.getEmail(),
            user.getTpAcesso(),
            user.getCodBanco(),
            user.getIdUsuario()
        ))

    def alterar_senha(self, password: str, id: str):
        query = f"UPDATE {MySql.DB_NAME}.tb_usuarios SET senha = %s WHERE id_usuario = %s"
        MySql.exec(query, (
            self.encrypt(password.encode('utf8')),
            id,
        ))

    def excluir_usuario(self, id: int):
        query = f'DELETE FROM {MySql.DB_NAME}.tb_usuarios WHERE id_usuario = %s'
        MySql.exec(query, (id,))

    def encrypt(self, senha: str) -> str:
        return bcrypt.hashpw(senha, bcrypt.gensalt(6))
