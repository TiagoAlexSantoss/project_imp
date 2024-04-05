document.addEventListener('DOMContentLoaded', function() {
    const tipoField = document.querySelector('#id_tipo');  // Obtém o campo tipo
    const listaField = document.querySelector('#id_lista');  // Obtém o campo lista

    // Função para habilitar ou desabilitar o campo lista com base no valor do campo tipo
    function toggleListaField() {
        if (tipoField.value === 'list') {
            listaField.disabled = false;  // Habilita o campo lista se o tipo for 'list'
        } else {
            listaField.disabled = true;   // Desabilita o campo lista se o tipo não for 'list'
        }
    }

    // Chama a função ao carregar a página
    toggleListaField();

    // Adiciona um listener para o evento de mudança no campo tipo
    tipoField.addEventListener('change', toggleListaField);
});
