$(function(){
  let listaEstados = [];

  $('[data-bs-toggle="tooltip"]').tooltip();

  $('[data-bs-target="#modalExclude"]').parent().click(function(evt) {
    evt.preventDefault();
  })

  $('#modalExclude').on('show.bs.modal', event => {
    const button = event.relatedTarget
    const action = button.getAttribute('data-modal-exclude-action')
    const text = button.getAttribute('data-modal-exclude-text')
    const title = button.getAttribute('data-modal-exclude-title')
    $("#modalExcludeText").html(text)
    $("#modalExcludeTitle").html(title)
    $("#modalExcludeConfirm").attr("data-bs-exclude-exec-action", action)
  });

   $('#modalExcludeConfirm').on('click', event => {
    const action = event.currentTarget.getAttribute('data-bs-exclude-exec-action')
    if (action) {
      const link = $(`<a href="${action}"></a>`);
      link[0].click();
    }
  });

  $('.money').mask('#.##0,00', {reverse: true});
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
});
