
function agregarOption(nombrecategoria){
    var selectCategorias = document.getElementById("categorias");
    let nueva_categoria=`<option>${nombrecategoria} </option>`;
    selectCategorias.insertAdjacentHTML("beforeend", nueva_categoria) 
}

function crearNuevaCat(){
    let allcategorias= [
        "Futbol",
        "Basquetbol",
        "Voleibol",
        "Rugby",
        "Tenis"
    ]
    for (i = 0; i<allcategorias.length ; i++){
        agregarOption(allcategorias[i])
    }
}

document.addEventListener('DOMContentLoaded',() => {
    crearNuevaCat();
})