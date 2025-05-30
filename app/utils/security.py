from functools import wraps
from flask import session, request, redirect, url_for, jsonify
from models.User import User
from enums.tipo_acessos import TipoAcessos
from datetime import datetime, timedelta


def login_required_api(fn):
    @wraps(fn)
    def validate_login(*args, **kwargs):
        if not has_user_logged():
            return jsonify({'status': 401, 'message': 'Usuário não está logado'})
        return fn(*args, **kwargs)
    return validate_login


def login_required(fn):
    @wraps(fn)
    def validate_login(*args, **kwargs):
        if not has_user_logged():
            return redirect(url_for('inicio.login', next=request.url))
        user = get_user_logged()
        if (user.logged_in + timedelta(minutes=15)) < datetime.now():
            logout_user()
            return redirect('/')
        else:
            user.logged_in = datetime.now()
            login_user(user)
        if user.profile == TipoAcessos.VST.name:
            return redirect('/sem_permissao')
        return fn(*args, **kwargs)
    return validate_login


def permission_access(tipo: list[TipoAcessos]):
    def wrap_function(fn):
        @wraps(fn)
        def check_acess(*args, **kwargs):
            user = get_user_logged()
            if TipoAcessos[user.profile] not in tipo:
                return redirect('/sem_permissao')
            return fn(*args, **kwargs)
        return check_acess
    return wrap_function


def login_user(user: User):
    session['user_logged'] = user.to_string()
    session['nome_usuario'] = user.name.split(' ')[0]
    session['is_root'] = user.profile == TipoAcessos.RT.name
    session['is_adm'] = user.profile == TipoAcessos.RT.name or user.profile == TipoAcessos.ADM.name
    session.modified = True


def login_user_mobile(user: User):
    session['user_logged_mobile'] = user.to_string()
    session['name_user_mobile'] = user.name.split(' ')[0]
    session['has_user_mobile_logged'] = True
    session.modified = True


def logout_user():
    session.pop('user_logged', None)
    session.pop('nome_usuario', None)
    session.pop('is_root', None)
    session.pop('is_adm', None)
    session.modified = True


def logout_user_mobile():
    session.pop('user_logged_mobile', None)
    session.pop('name_user_mobile', None)
    session.pop('has_user_mobile_logged', None)
    session.modified = True


def get_user_logged() -> User:
    return User.from_string(session.get('user_logged'))


def get_user_logged_mobile() -> User:
    return User.from_string(session.get('user_logged_mobile'))


def has_user_logged() -> bool:
    return session.get('user_logged') is not None


def has_user_mobile_logged() -> bool:
    return session.get('user_logged_mobile') is not None
