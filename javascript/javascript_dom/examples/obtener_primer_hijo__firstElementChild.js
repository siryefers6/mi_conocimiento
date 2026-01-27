// Obtener primer elemento hijo

// HTML: <div id="lista">
//   <p>Primer párrafo</p>
//   <p>Segundo párrafo</p>
//   <p>Tercer párrafo</p>
// </div>

const lista = document.getElementById('lista');

// Obtener primer hijo elemento
const primero = lista.firstElementChild;
console.log(primero.textContent); // "Primer párrafo"

// Modificar el primer hijo
primero.style.color = 'red';

// Agregar clase al primer hijo
primero.classList.add('destacado');

// Eliminar primer hijo
primero.remove();

// Obtener el nuevo primer hijo
const ahora = lista.firstElementChild;
console.log(ahora.textContent); // "Segundo párrafo"

// firstElementChild vs firstChild
// firstElementChild: solo elementos
// firstChild: incluye nodos de texto y comentarios

// Ejemplo: procesar primer hijo
const contenedor = document.getElementById('contenedor');
if (contenedor.firstElementChild) {
  console.log(contenedor.firstElementChild.tagName);
}

// firstChild podría devolver un nodo de texto
console.log(lista.firstChild); // #text (espacios en blanco)
console.log(lista.firstElementChild); // <p> (primer elemento)
