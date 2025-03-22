from flask import Blueprint
import utils.converter as converter
from datetime import datetime

filtros_bp = Blueprint('filtros', __name__)

@filtros_bp.app_template_filter('to_date')
def format_datetime(value):
    if value is not None and value != '--' and isinstance(value, datetime):
        return value.strftime('%d/%m/%Y')
    elif isinstance(value, str):
        return converter.converterStrDateTimeToDateFormat(value)
    return value


@filtros_bp.app_template_filter('to_datetime')
def format_datetime(value):
    if value is not None and value != '--' and isinstance(value, datetime):
        return value.strftime('%d/%m/%Y %H:%M:%S')
    elif isinstance(value, str):
        return converter.converterStrDateTimeFormatBr(value)
    return value


@filtros_bp.app_template_filter('to_currency')
def format_datetime(value):
    if value is not None and value != '--' and converter.isNumber(value):
        return converter.converterFloatToCurrency(value)
    return value


@filtros_bp.app_template_filter('to_cpf_cnpj')
def format_cpf(value):
    if value is None or value == '--' or not isinstance(value, str):
        return value
    elif len(value) == 11:
        cpf = value.zfill(11)
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    elif len(value) == 14:
        cnpj = value.zfill(14)
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    return value


@filtros_bp.app_template_filter('to_cel_tel')
def format_tel_cel(value):
    if value is None or value == '--' or not isinstance(value, str):
        return value
    elif len(value) == 8 or len(value) == 9:
        tel = value.zfill(len(value))
        return f'{tel[:4]}-{tel[4:]}' if len(value) == 8 else f'{tel[:5]}-{tel[5:]}'
    elif len(value) == 10 or len(value) == 11:
        telCp = value.zfill(len(value))
        return f'({telCp[:2]}) {telCp[2:6]}-{telCp[6:]}' if len(value) == 10 else f'({telCp[:2]}) {telCp[2:7]}-{telCp[7:]}'
    return value
