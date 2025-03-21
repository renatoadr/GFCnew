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

  $(".percent").mask("##0,00", {
    reverse: true,
    onChange: function(val, evt, el, opt) {
      let fval = parseFloat(val.replace(',', '.'))
      if (!isNaN(fval) && fval > 100) {
        el.val(100)
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

  $('.email').mask("A", {
    translation: {
        "A": { pattern: /[\w@\-.+]/, recursive: true }
    }
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

  $("#atcplt-box").delegate('.list-group-item-action', 'click', function(evt) {
    evt.preventDefault();
    let data = JSON.parse($(this).attr('data-client'));
    let docView = '';

    if (data.tipoDoc === 'CPF') {
      docView = data.doc.replace(/(\d{3})(\d{3})(\d{3})(\d{2})$/, '$1.$2.$3-$4');
    } else {
      docView = data.doc.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
    }

    $("#atcplt-list").empty().hide('slow');
    $('#atcplt-email').text(data.email);
    $('#atcplt-tel').text(data.tel.replace(/(\d{2})(\d{4,5})(\d{4})$/, '($1) $2-$3'));
    $('#atcplt-doc').text(docView);
    $('#atcplt-docTipo').text(data.tipoDoc);
    $('#atcplt-nome').text(data.nome);
    $("#atcplt-dados").attr('data-client-selected', JSON.stringify(data)).show('slow');
    $('#modalAssociarClienteConfirmar').removeAttr('disabled');
  });

  let timer = null;
  $("#atcplt-inpu").on('input', function() {
    clearTimeout(timer);
    let that = $(this);
    $('#modalAssociarClienteConfirmar').attr('disabled', true);
    timer = setTimeout(function() {
      let val = that.val();
      let list = $("#atcplt-list");
      $("#atcplt-dados").hide('slow');
      $('#atcplt-email').text('');
      $('#atcplt-tel').text('');
      $('#atcplt-doc').text('');
      $('#atcplt-docTipo').text('');
      $('#atcplt-nome').text('');
      list.hide('slow');
      if (val.length > 3) {
        that.attr('disabled');
        $.getJSON('/api/clientes?search=' + val, function(data) {
          list.empty();

          if (data.length > 0) {
            for(let item of data) {
              let li = $('<li/>');
              let a = $('<a/>');
              a.addClass('list-group-item list-group-item-action');
              a.attr('data-client', JSON.stringify(item));
              a.attr('href', '#');
              a.html(item.nome);
              li.append(a);
              list.append(li);
            }
          } else {
            list.append('<li class="text-center mt-4">Não há clientes para essa busca</li>');
          }

          list.show('slow');
          that.removeAttr('disabled');
        });
      }
    }, 650);
  })

  $('#modalAssociarCliente').on('show.bs.modal', event => {
    const button = event.relatedTarget;
    const nameReceiver = button.getAttribute('data-input-name-receiver');
    const docReceiver = button.getAttribute('data-input-doc-receiver');
    $('#modalAssociarClienteConfirmar').attr('data-input-name-receiver', nameReceiver);
    $('#modalAssociarClienteConfirmar').attr('data-input-doc-receiver', docReceiver);
  });

  $('#modalAssociarCliente').on('hide.bs.modal', event => {
    $("#atcplt-list").empty().hide('slow');
    $("#atcplt-dados").hide('slow');
    $('#atcplt-email').text('');
    $('#atcplt-tel').text('');
    $('#atcplt-doc').text('');
    $('#atcplt-docTipo').text('');
    $('#atcplt-nome').text('');
    $("#atcplt-inpu").val('');
    $("#atcplt-dados").removeAttr('data-client-selected');
    $('#modalAssociarClienteConfirmar').removeAttr('data-input-name-receiver');
    $('#modalAssociarClienteConfirmar').removeAttr('data-input-doc-receiver');
  });

  $('#modalAssociarClienteConfirmar').on('click', function() {
    let isVisibleDados = $("#atcplt-dados").is(':visible');
    let value = $("#atcplt-inpu").val();
    let dados = $("#atcplt-dados").attr('data-client-selected')
    let iptName = $(this).attr('data-input-name-receiver');
    let iptDoc = $(this).attr('data-input-doc-receiver');
    if (isVisibleDados && value != '') {
      dados = JSON.parse(dados);
      $('#' + iptName).val(dados.nome).attr('readonly', true);
      $('#' + iptDoc).val(dados.doc);
    }
    $('#modalAssociarCliente').modal('hide')
  });

});
