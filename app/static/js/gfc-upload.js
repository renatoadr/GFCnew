$(function() {
  function changeVigencia(val) {
    if (val == 'vigenciaExistente') {
      $('#vigenciaExistenteBox').show();
      $('#novaVigenciaBox').hide();
      $("#mesVigencia").val('');
      $('#anoVigencia').val('');
    } else if (val == 'novaVigencia') {
      $('#vigenciaExistenteBox').hide();
      $('#novaVigenciaBox').show();
      $('[name="vigCorrrente"]').prop('checked', false);
      $('[name="capa"]').prop('checked', false).removeAttr('disabled')
      $('#foto_3D').val(0).attr('min', 0).siblings('output').val(0);
      $('#fotos_obra').val(0).attr('min', 0).siblings('output').val(0);
    } else {
      $('#vigenciaExistenteBox').hide();
      $('#novaVigenciaBox').hide();
      $("#vigenciaExistenteOpt").val('');
      $('#anoVigencia').val('');
      $('[name="vigCorrrente"]').prop('checked', false);
    }
  }

  $('.upload').on('change', function(evt) {
    const file = evt.currentTarget.files.item(0)
    if (file && /jpe?g|png$/.test(file.type)) {
      const read = new FileReader()
      read.onload = () => {
        let img = $(this).siblings('img')
        if (img.length === 0) {
          img = $('<img/>')
          img.addClass('img-thumbnail w-100 mt-2 mb-2')
          img.attr('src', read.result)
          $(this).before(img)
        } else {
          img.attr('src', read.result)
        }
      }
      read.readAsDataURL(file)
    } else {
      $(this).val('')
      $.toast({
        heading: '<strong>Arquivo inválido</strong>',
        text: "Este formato de arquivo não é válido. Envie somente fotos na extensão PNG ou JPG.",
        icon: 'error',
        position: 'bottom-center',
        hideAfter: 10000,
      });
    }
  });

  $('[name="tipoVigencia"]').on('change', function() {
    const val = $(this).val();
    changeVigencia(val);
  });

  $('[name="vigCorrrente"]').on('change', function() {
    const val = $(this).val();
    $('[name="capa"]').prop('checked', false).removeAttr('disabled')
    $('#foto_3D').val(0).attr('min', 0).siblings('output').val(0);
    $('#fotos_obra').val(0).attr('min', 0).siblings('output').val(0);
    $('[name="vigCorrrente"]').attr('disabled', true);
    if (val) {
      $.getJSON('/api/imagens/vigencia_corrente?vig=' + val, function(data) {
        const fields = Object.keys(data)
        const img3D = fields.filter(f => /^foto_3D_\d{1}$/.test(f)).sort((fa, fb) => fa > fb ? -1 : 1)
        const imgObra = fields.filter(f => /^foto_\d{1,2}$/.test(f)).sort((fa, fb) => fa > fb ? -1 : 1)
        const capa = fields.filter(f => !/^foto(_3D)?_\d{1,2}$/.test(f))
        const min3D = img3D[0] ? img3D[0].match(/\d{1,2}$/)[0] : 0;
        const minObra = imgObra[0] ? imgObra[0].match(/\d{1,2}$/)[0] : 0;

        for(let cp of capa) {
          $('#' + cp).prop('checked', true).attr('disabled', true);
        }

        $('#foto_3D').attr('value', min3D).attr('min', min3D).siblings('output').val(min3D);
        $('#fotos_obra').attr('value', minObra).attr('min', minObra).siblings('output').val(minObra);
        $('[name="vigCorrrente"]').removeAttr('disabled');
      }).fail(function() {
        $('[name="vigCorrrente"]').removeAttr('disabled');
        $('[name="vigCorrrente"]').prop('checked', false);
      });
    }
  });

  $('input[type="range"]').each(function () {
    const that = $(this);
    setTimeout(function () {
      that.siblings('output').val(that.val())
    }, 100)
  });

  $('input[type="range"]').on('input', function () {
    $(this).siblings('output').val($(this).val())
  });

  $('.fotosObra').on('change', function() {
    $(this).siblings('.input-group').show();
    $(this).siblings('.input-group').find('input').removeAttr('disabled')
  });
});

$(function() {
  const requireds = GFC.getRequiredFields("formUploadConfig")
  delete requireds.rules;
  const config = GFC.getConfigValidateForm(requireds);
  config.submitHandler = function (form) {
    $('[name="capa"]').removeAttr('disabled')
    form.submit();
  }
  $("#formUploadConfig").validate(config);

  const requiredsUpload = GFC.getRequiredFields("formUpload");
  delete requiredsUpload.rules;
  const configUpload = GFC.getConfigValidateForm(requiredsUpload);
  $("#formUpload").validate(configUpload);
})

$(function() {
  function valuesWidth() {
    const $itens = $('#itensVigencias');
    const $box = $('#boxItensVigencias');
    const $li = $itens.find('li');

    const wBox = parseInt($box.css('width'));
    const wItens = parseInt($itens.css('width'));
    const wli = Math.round(parseFloat($($li.get(0)).css('width')));
    const gap = parseInt($itens.css('gap'));
    const liWidth = wli + gap;

    const pos = Math.abs(parseInt($itens.css('left')));
    const limiter = liWidth * $li.length - (liWidth + 70);

    return {
      pos,
      liWidth,
      $itens,
      hasLimiter: pos <= limiter,
      isListGrandSize: wBox < wItens
    }
  }

  function initBox() {
    const containerWidth = parseInt($('.container').css('width'));
    const values = valuesWidth();
    const over = containerWidth % values.liWidth;
    $('#boxItensVigencias').css('width', (containerWidth - over) + 'px');
  }

  $('#btn-left').click(function() {
    const values = valuesWidth();
    const neg = values.pos * -1
    const isLastpos = neg >= (values.liWidth * -1) && neg <= 0;
    const btns = $('.btnMove');
    btns.attr('disabled', true);
    if (values.isListGrandSize) {
      values.$itens.css('left', (isLastpos ? 0 : neg + values.liWidth) + 'px')
    }
    setTimeout(function() {btns.removeAttr('disabled');}, 50);
  });

  $('#btn-right').click(function() {
    const values = valuesWidth();
    const btns = $('.btnMove');
    btns.attr('disabled', true);
    if (values.isListGrandSize && values.hasLimiter) {
      values.$itens.css('left', -(values.pos + values.liWidth) + 'px')
    }
    setTimeout(function() {btns.removeAttr('disabled');}, 50);
  });

  $('[name="tipoVigencia"]').on('change', function() {
    const val = $(this).val();
    if (val == 'vigenciaExistente') {
      initBox();
    }
  });
})
