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

  $('.alphanum').mask("A", {
    translation: {
        "A": { pattern: /[A-Za-z0-9\sÇçÃÂÀÁâãàáÕÔôõÉÈéè]/, recursive: true }
    }
  })

  $(".percent").mask("##0,00", {
    reverse: true,
    onChange: function(val, evt, el, opt) {
      let fval = parseFloat(val.replace(',', '.'))
      if (!isNaN(fval) && fval > 100) {
        el.val(100)
      }
    }
  });

  $(".percent10").mask("0,00", {
    reverse: true,
    onChange: function(val, evt, el, opt) {
      if (val.length === 2) {
        val = val.split('');
        val = `${val[0]},${val[1]}`
        el.val(val)
      } else {
        let fval = parseFloat(val.replace(',', '.'))
        if (!isNaN(fval) && fval > 10) {
          el.val('9,99')
        }
      }
    }
  });

  $(".perc").mask("##0", {
    reverse: true,
    onChange: function(val, evt, el, opt) {
      let fval = parseFloat(val.replace(',', '.'))
      if (!isNaN(fval) && fval > 100) {
        el.val(100)
      }
    }
  });

  $('.money').mask('#.##0,00', {reverse: true});

  $('.4num').mask('9999', {reverse: true});

  $('.2num').mask('99', {reverse: true});

  $('.cpf').mask('000.000.000-00', {reverse: true});

  $('.cnpj').mask('00.000.000/0000-00', {reverse: true});

  $('.tel').mask("Z0000-0000", {
    translation: {
      'Z': {
        pattern: /[0-9]/, optional: true
      }
    },
    reverse: true
  });

  $('.cep').mask('00000-000', {
    onChange: function(cep) {
      $("#logradouro").val('');
      $("#bairro").val('');
      $("#cidade").val('');
      $("#estado").val('');
    },
    onComplete: function(cep) {
      $.getJSON('//brasilapi.com.br/api/cep/v2/' + cep.replace('-', ''), function(data){
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

  $('.email').mask("A", {
    translation: {
        "A": { pattern: /[\w@\-.+]/, recursive: true }
    }
  });

  $.getJSON('//brasilapi.com.br/api/banks/v1', function(data) {
    const listaBancos = data.sort(function (ba, bb) {
      return ba.name < bb.name ? -1 : 1
    });
    for (let banco of listaBancos) {
      $('#nmBanco').append(`<option value="${banco.name}">${banco.name}</option>`);
    }
  });

  $.getJSON('//servicodados.ibge.gov.br/api/v1/localidades/estados', function (data) {
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
    $.getJSON(`//servicodados.ibge.gov.br/api/v1/localidades/estados/${estado.id}/municipios`, function (data) {
      const cidades = data.sort(function (da, db) {
        return da.nome < db.nome ? -1 : 1
      });
      for (let cidade of cidades) {
        $('#cidade').append(`<option value="${cidade.nome}">${cidade.nome}</option>`);
      }
    });
  });

  $("#formUploadExcel").validate({
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

  $("#submenu a").each(function() {
    if (location.pathname === $(this).attr('href')) {
      $(this).addClass('bg-body active')
    }
  })

  $("#submenu_action").click(function() {
    const svg = $(this).children('svg')
    const subMenu = $('#submenu_perfil')
    if (svg.hasClass('fa-xmark')) {
      svg.addClass('fa-bars');
      svg.removeClass('fa-xmark');
      subMenu.hide('fast')
    } else {
      svg.addClass('fa-xmark');
      subMenu.show('fast')
    }
  });
});
