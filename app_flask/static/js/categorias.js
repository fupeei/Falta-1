/*botones de inicio y cerrar sesion */
function over(element){
    element.style.backgroundColor = "#3461e9";
    element.style.color = "#f0f0f0"
}
function out(element){
    element.style.backgroundColor = "#f0f0f0"
    element.style.color = "black"
}
function overlog(element){
    element.style.backgroundColor = "#cb272c";
    element.style.color = "#f0f0f0"
}
function outlog(element){
    element.style.backgroundColor = "#f0f0f0"
    element.style.color = "black"
}
/*botones de seleccion de categoria */

const prev = document.querySelector('.prev')
const next = document.querySelector('.next')
const lista = document.querySelector('.lista_deportes')
/* 
prev.addEventListener('click', () => {
    lista.scrollLeft -= 300
})

next.addEventListener('click', () => {
    lista.scrollLeft += 300
})
 */
/*recuadro seccion deportes */
function overdeportes(element){
    element.style.color = "#f0f0f0"
}
function outdeportes(element){
    element.style.color = "black"
}

/*Formulario crear un evento */
function traerCategorias(event) {
    fetch(`/categorias/${ event.target.value }`) //LO FUE A BUSCAR A LA RUTA
        .then((res) => {
            //Lo recibio
            return res.json();
        })
        .then((datos) => {
            //LO PROCESÓ
            //hago algo con los datos
            var selectCategorias = document.getElementById("categorias");
            selectCategorias.innerHTML = "";
            console.log(datos);
            datos.forEach((categoria) => {
                var content = `<option value="${categoria.id}">${categoria.nombre}</option>`;
                selectCategorias.innerHTML += content;
            });
        });
}

