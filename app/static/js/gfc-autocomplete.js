$(function() {
  let timer = null;

  function openDataClient(data) {
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
    $("#atcplt-inpu").val(data.nome);
  }

  function clearDataClient() {
    $("#atcplt-dados").hide('slow');
    $('#atcplt-email').text('');
    $('#atcplt-tel').text('');
    $('#atcplt-doc').text('');
    $('#atcplt-docTipo').text('');
    $('#atcplt-nome').text('');
  }

  function strongSearch(item) {
    let target = item.trim().normalize('NFD').replace(/[\u0300-\u036f]/g, "").toLowerCase();
    let source = val.trim().normalize('NFD').replace(/[\u0300-\u036f]/g, "").toLowerCase();
    let index = target.indexOf(source);
    if (index > -1) {
      let init = item.substring(0, index);
      let middle = item.substring(index, index + val.length);
      let end = item.substring(index + val.length)
      return `${init}<strong>${middle}</strong>${end}`;
    }
    return item;
  }

  function execSearch() {
    let val = $(this).val();
    let list = $("#atcplt-list");
    if (val.length >= 3) {
      $(this).attr('disabled');
      $.getJSON('/api/clientes?search=' + val, function(data) {
        list.empty();
        if (data.length > 0) {
          for(let item of data) {
            let li = $('<li class="list-group-item" />');
            let a = $('<a/>');
            let nome = item.nome.split(' ').map(strongSearch.bind(null, val)).join(' ');
            a.addClass('list-group-item-action');
            a.attr('data-client', JSON.stringify(item));
            a.attr('href', '#');
            a.html(nome);
            li.append(a);
            list.append(li);
          }
        } else {
          list.append('<li class="text-center mt-4">Não há clientes para essa busca</li>');
        }

        list.show('slow');
        $(this).removeAttr('disabled');
      });
    }
  }

  $("#atcplt-box").delegate('.list-group-item-action', 'click', function(evt) {
    evt.preventDefault();
    let data = JSON.parse($(this).attr('data-client'));
    openDataClient(data);
    $('#modalAssociarClienteConfirmar').removeAttr('disabled');
  });

  $("#atcplt-inpu").on('input', function() {
    clearTimeout(timer);
    $('#modalAssociarClienteConfirmar').attr('disabled', true);
    clearDataClient();
    $("#atcplt-list").hide('slow');
    timer = setTimeout(execSearch.bind(this), 450);
  })

  $('#modalAssociarCliente').on('show.bs.modal', function(event) {
    const button = event.relatedTarget;
    const nameReceiver = button.getAttribute('data-input-name-receiver');
    const docReceiver = button.getAttribute('data-input-doc-receiver');
    const initialClient = button.getAttribute('data-initial-selected');
    const url = new URL(location.href);
    const modo = url.searchParams.get('modo') || '';

    if (modo.toLowerCase() === 'consulta') {
      $('#modalAssociarClienteConfirmar').hide();
      $("#atcplt-inpu").attr('readonly', true);
    } else {
      $('#modalAssociarClienteConfirmar').show();
      $('#modalAssociarClienteConfirmar').attr('data-input-name-receiver', nameReceiver);
      $('#modalAssociarClienteConfirmar').attr('data-input-doc-receiver', docReceiver);
      $("#atcplt-inpu").removeAttr('readonly');
    }

    if (initialClient && initialClient !== 'None' && /\d+/.test(initialClient)) {
      $.getJSON('/api/cliente/'+initialClient, function(data) {
        openDataClient(data);
      });
    }
  });

  $('#modalAssociarCliente').on('hide.bs.modal', function() {
    $("#atcplt-list").empty().hide('slow');
    clearDataClient();
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
      $('[data-bs-target="#modalAssociarCliente"]').attr('data-initial-selected', dados.doc);
    }
    $('#modalAssociarCliente').modal('hide')
  });
});
