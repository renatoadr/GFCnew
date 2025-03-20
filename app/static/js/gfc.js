$(function(){
  jQuery.validator.addMethod("cpf", function(value, element) {
    value = jQuery.trim(value);

    value = value.replace('.','');
    value = value.replace('.','');
    cpf = value.replace('-','');
    while(cpf.length < 11) cpf = "0"+ cpf;
    var expReg = /^0+$|^1+$|^2+$|^3+$|^4+$|^5+$|^6+$|^7+$|^8+$|^9+$/;
    var a = [];
    var b = new Number;
    var c = 11;
    for (i=0; i<11; i++){
        a[i] = cpf.charAt(i);
        if (i < 9) b += (a[i] * --c);
    }
    if ((x = b % 11) < 2) { a[9] = 0 } else { a[9] = 11-x }
    b = 0;
    c = 11;
    for (y=0; y<10; y++) b += (a[y] * c--);
    if ((x = b % 11) < 2) { a[10] = 0; } else { a[10] = 11-x; }

    var retorno = true;
    if ((cpf.charAt(9) != a[9]) || (cpf.charAt(10) != a[10]) || cpf.match(expReg)) retorno = false;

    return this.optional(element) || retorno;

  }, "Informe um CPF válido");

  jQuery.validator.addMethod("cnpj", function(value, element) {
    value = jQuery.trim(value);

    var b = [ 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2 ]
    var c = String(value).replace(/[^\d]/g, '')

    if(c.length !== 14)
        return false

    if(/0{14}/.test(c))
        return false

    for (var i = 0, n = 0; i < 12; n += c[i] * b[++i]);
    if(c[12] != (((n %= 11) < 2) ? 0 : 11 - n))
        return false

    for (var i = 0, n = 0; i <= 12; n += c[i] * b[i++]);
    if(c[13] != (((n %= 11) < 2) ? 0 : 11 - n))
        return false

    return true
  }, "Informe um CNPJ válido");

  jQuery.validator.addMethod("maxf", function(val, element, limiter) {
    let value = jQuery.trim(val);
    if (value === '' || value === undefined) return true
    let fvalue = parseFloat(value.replace(',', '.'));
    return !(fvalue > limiter);
  }, "Campo inválido. O valor está acima do permitido.");

  jQuery.validator.addMethod("minf", function(val, element, limiter) {
    let value = jQuery.trim(val);
    if (value === '' || value === undefined) return true
    let fvalue = parseFloat(value.replace(',', '.'));
    return !(fvalue < limiter);
  }, "Campo inválido. O valor está abaixo do permitido.");

  $.validator.methods.email = function( value, element ) {
    return this.optional( element ) || /[a-z]+@[a-z]+(\.[a-z]+){1,3}/.test( value );
  }
});

window.GFC_MESSAGES = (function() {
  return {
    REQUIRED: 'Este campo é obrigatório',
    EMAIL: 'Informe um email válido',
    CPF: 'Informe um CPF válido',
    CNPJ: 'Informe um CNPJ válido',
    MIN: (minValue) => `Este campo não é válido. O valor mínimo é ${minValue}`,
    MAX: (minValue) => `Este campo não é válido. O valor máximo é ${minValue}`,
    MIN_LENGTH: (minValue) => `Este campo não é válido. O valor mínimo de caracteres é ${minValue}`
  }
})();

window.GFC = (function() {
  const getRequiredFields = function(idForm) {
   const inputNames = Array.from(
      document.querySelectorAll(`#${idForm} input, #${idForm} select`)
    ).filter(
      item => item.type !== 'hidden' && !item.readOnly
    ).map(
      item => item.name
    );

    const rules = inputNames.reduce(function (mount, name) {
      mount[name] = 'required';
      return mount;
    }, {});

    const messages = inputNames.reduce(function (mount, name) {
      mount[name] = 'Este campo é obrigatório';
      return mount;
    }, {});

    return {messages, rules}
  }

  return {
    getRequiredFields
  }

})();

