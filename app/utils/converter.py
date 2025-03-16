from datetime import datetime

def converterStrToFloat(value, default = 0):
    if value is None:
       return default
    return float(value.replace('.', '').replace(',', '.'))

def converterStrDateTimeToDateFormat(stringdatetime):
    return format(datetime.strptime(stringdatetime, "%Y-%m-%d %H:%M:%S"), "%d/%m/%Y")

def converterDateTimeToDateEnFormat(stringdatetime):
    return format(stringdatetime, "%Y-%m-%d")

def converterFloatToCurrency(value):
   return '{:20,.2f}'.format(float(value)).replace('.', '_').replace(',', '.').replace('_', ',')

def isNumber(value):
    try:
      float(value)
      return True
    except:
      return False
