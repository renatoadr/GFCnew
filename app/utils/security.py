from functools import wraps
from flask import session, request, redirect, url_for
from models.User import User
from enums.tipo_acessos import TipoAcessos


def login_required(fn):
    @wraps(fn)
    def validate_login(*args, **kwargs):
        if not has_user_logged():
            return redirect(url_for('inicio.login', next=request.url))
        return fn(*args, **kwargs)
    return validate_login


def permission_access(tipo: TipoAcessos):
    def wrap_function(fn):
        @wraps(fn)
        def check_acess(*args, **kwargs):
            user = get_user_logged()
            if user.profile != tipo.name:
                return redirect('/sem_permissao')
            return fn(*args, **kwargs)
        return check_acess
    return wrap_function


def login_user(user: User):
    session['user_logged'] = user.to_string()
    session['nome_usuario'] = user.name.split(' ')[0]
    session['eh_adm'] = user.profile == 'ADM'
    session.modified = True


def logout_user():
    session.pop('user_logged', None)
    session.pop('nome_usuario', None)
    session.pop('eh_adm', None)
    session.modified = True


def get_user_logged() -> User:
    return User.from_string(session.get('user_logged'))


def has_user_logged() -> bool:
    return session.get('user_logged') is not None
