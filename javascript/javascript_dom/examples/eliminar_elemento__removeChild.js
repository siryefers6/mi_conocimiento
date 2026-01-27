// Eliminar elemento hijo

// HTML: <div id="contenedor">
//   <p id="parrafo1">Párrafo 1</p>
//   <p id="parrafo2">Párrafo 2</p>
// </div>

const contenedor = document.getElementById('contenedor');
const parrafo1 = document.getElementById('parrafo1');

// Eliminar especificando el hijo
contenedor.removeChild(parrafo1);

// Resultado: <div id="contenedor">
//   <p id="parrafo2">Párrafo 2</p>
// </div>

// Eliminar el primer hijo
const primerHijo = contenedor.firstElementChild;
contenedor.removeChild(primerHijo);

// Eliminar todos los hijos
const lista = document.getElementById('lista');
while (lista.firstElementChild) {
  lista.removeChild(lista.firstElementChild);
}

// O de forma más moderna (usando remove() en el elemento)
const elementoAEliminar = document.getElementById('elemento');
elementoAEliminar.remove();

// Remover después de obtener referencia
const parrafo = document.querySelector('p');
if (parrafo && parrafo.parentElement) {
  parrafo.parentElement.removeChild(parrafo);
}
