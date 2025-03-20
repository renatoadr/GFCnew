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

def removeCaractersNotDigit(value):
   return re.sub(r"^\d+", "", value)

def isNumber(value):
    try:
      float(value)
      return True
    except:
      return False
