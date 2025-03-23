from datetime import datetime
import re

def converterStrToFloat(value, default = 0):
    if value is None:
       return default
    return float(value.replace('.', '').replace(',', '.'))

def converterStrDateTimeToDateFormat(stringdatetime):
    return format(datetime.strptime(stringdatetime, "%Y-%m-%d %H:%M:%S"), "%d/%m/%Y")

def converterStrDateTimeFormatBr(stringdatetime):
    return format(datetime.strptime(stringdatetime, "%Y-%m-%d %H:%M:%S"), "%d/%m/%Y %H:%M:%S")

def converterDateTimeToDateEnFormat(stringdatetime):
    return format(stringdatetime, "%Y-%m-%d")

def converterFloatToCurrency(value):
   return '{:20,.2f}'.format(float(value)).replace('.', '_').replace(',', '.').replace('_', ',')

def removeAlpha(value):
   return re.sub(r"\D+", "", value)

def maskCpfOrCnpj(value: str):
  if len(value) == 11:
      cpf = value.zfill(11)
      return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
  elif len(value) == 14:
      cnpj = value.zfill(14)
      return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
  return value

def isNumber(value):
    try:
      float(value)
      return True
    except:
      return False
