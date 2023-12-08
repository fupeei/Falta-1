function traerCategorias(event) {
    fetch(`/obtener_categoria_tipo/${event.target.value}`) // Aquí faltaban los backticks para concatenar la variable en la cadena
    .then((res) => {
        return res.json();
    })
    .then((datos) => {
        var selectCategorias = document.getElementById("categorias");
        selectCategorias.innerHTML = "";
        datos.forEach((categoria) => {
        // Utiliza comillas simples para las cadenas en HTML y template literals para las variables
        var content = `<option value="${categoria.id_categoria}">${categoria.nombre_categoria}</option>`;
        selectCategorias.innerHTML += content;
        });
    })
    .catch((error) => {
        console.error('Error al obtener categorías:', error);
    });
}
