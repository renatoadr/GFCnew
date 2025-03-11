$(function(){
  $('[data-bs-toggle="tooltip"]').tooltip();
  $('.btnExcluir').click(function(evt) {
    evt.preventDefault();
  })

  $('#modalExcludeOrcamento').on('show.bs.modal', event => {
    const button = event.relatedTarget
    const action = button.getAttribute('data-action')
    const text = button.getAttribute('data-text')
    $("#modalText").html(text)
    $("#modalConfirm").attr("data-exec-action", action)
  });
   $('#modalConfirm').on('click', event => {
    const action = event.currentTarget.getAttribute('data-exec-action')
    if (action) {
      const link = $(`<a href="${action}"></a>`);
      link[0].click();
    }
  });
});
