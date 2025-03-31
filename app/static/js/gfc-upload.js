$(function() {
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
  })
});
