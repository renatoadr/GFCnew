window.GFC = (function() {
const getRequiredFields = function(idForm) {
   const inputNames = Array.from(
      document.querySelectorAll(`#${idForm} input`)
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
