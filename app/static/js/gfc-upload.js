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

  const requireds = GFC.getRequiredFields("formUploadConfig")
  requireds.messages.anoVigencia = {
    required: GFC_MESSAGES.REQUIRED,
    min: GFC_MESSAGES.MIN(2000),
    max: GFC_MESSAGES.MAX(3000),
  }
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

});
