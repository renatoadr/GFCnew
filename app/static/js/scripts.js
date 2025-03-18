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

$(function(){
  let listaEstados = [];

  $('[data-bs-toggle="tooltip"]').tooltip();

  $('[data-bs-target="#modalExclude"]').parent().click(function(evt) {
    evt.preventDefault();
  })

  $('#modalExclude').on('show.bs.modal', event => {
    const button = event.relatedTarget;
    const action = button.getAttribute('data-modal-exclude-action');
    const text = button.getAttribute('data-modal-exclude-text');
    const title = button.getAttribute('data-modal-exclude-title');
    $("#modalExcludeText").html(text);
    $("#modalExcludeTitle").html(title);
    $("#modalExcludeConfirm").attr("data-bs-exclude-exec-action", action);
  });

  $('#modalUploadExcel').on('show.bs.modal', event => {
    const button = event.relatedTarget;
    const action = button.getAttribute('data-action-process');
    const text = button.getAttribute('data-desc');
    $("#formUploadExcel").attr('action', action);
    $("#modalUploadExceldesc").html(text);
  });

   $('#modalExcludeConfirm').on('click', event => {
    const action = event.currentTarget.getAttribute('data-bs-exclude-exec-action');
    if (action) {
      const link = $(`<a href="${action}"></a>`);
      link[0].click();
    }
  });

  $('#backHistory').click(function() {
    history.back();
  });

  $('.money').mask('#.##0,00', {reverse: true});
  $('.4num').mask('9999', {reverse: true});
  $('.2num').mask('99', {reverse: true});
  $('.cpf').mask('000.000.000-00', {reverse: true});
  $('.cep').mask('00000-000', {
    onChange: function(cep) {
      $("#logradouro").val('');
      $("#bairro").val('');
      $("#cidade").val('');
      $("#estado").val('');
    },
    onComplete: function(cep) {
      $.getJSON('https://brasilapi.com.br/api/cep/v2/' + cep.replace('-', ''), function(data){
        $("#logradouro").val(data.street);
        $("#bairro").val(data.neighborhood);
        $("#estado").val(data.state);
        $('#estado').trigger('change');
        setTimeout(function() {
          $("#cidade").val(data.city);
        }, 500);
      });
    },
  });

  $.getJSON('https://brasilapi.com.br/api/banks/v1', function(data) {
    const listaBancos = data.sort(function (ba, bb) {
      return ba.name < bb.name ? -1 : 1
    });
    for (let banco of listaBancos) {
      $('#nmBanco').append(`<option value="${banco.name}">${banco.name}</option>`);
    }
  });

  $.getJSON('http://servicodados.ibge.gov.br/api/v1/localidades/estados', function (data) {
    listaEstados = data.sort(function (da, db) {
      return da.sigla < db.sigla ? -1 : 1
    });
    for (let estado of listaEstados) {
      $('#estado').append(`<option value="${estado.sigla}">${estado.nome}</option>`);
    }
  });

  $("#estado").change(function(evt){
    $('#cidade option').remove();
    const selecionado = evt.currentTarget.value;
    if (!selecionado) return;
    const estado = listaEstados.find(function(est) {
      return est.sigla === selecionado
    })
    if (!estado) return;
    $.getJSON(`http://servicodados.ibge.gov.br/api/v1/localidades/estados/${estado.id}/municipios`, function (data) {
      const cidades = data.sort(function (da, db) {
        return da.nome < db.nome ? -1 : 1
      });
      for (let cidade of cidades) {
        $('#cidade').append(`<option value="${cidade.nome}">${cidade.nome}</option>`);
      }
    });
  });

  $( "#formUploadExcel" ).validate({
    rules: {
      file: {
        required: true,
        accept: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
      },
    },
    messages: {
      file: {
        required: "Este campo é obrigatório",
        accept: 'Só é aceito arquivo excel'
      },
    },
    errorClass: 'is-invalid',
    errorElement: 'span',
    highlight: function (element, errorClass, validClass) {
      setTimeout(function () {
        $(element).siblings(`span[id="${element.id}-error"]`).addClass('invalid-feedback').show();
        $(element).addClass(errorClass)
      }, 50)
    },
  });
});
