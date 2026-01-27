// Obtener último elemento hijo

// HTML: <ul id="lista">
//   <li>Elemento 1</li>
//   <li>Elemento 2</li>
//   <li>Elemento 3</li>
// </ul>

const lista = document.getElementById('lista');

// Obtener último hijo elemento
const ultimo = lista.lastElementChild;
console.log(ultimo.textContent); // "Elemento 3"

// Modificar el último hijo
ultimo.style.fontWeight = 'bold';

// Agregar clase al último hijo
ultimo.classList.add('fin-lista');

// Eliminar último hijo
ultimo.remove();

// Obtener el nuevo último hijo
const ahora = lista.lastElementChild;
console.log(ahora.textContent); // "Elemento 2"

// Alternancia entre primero y último
const primerItem = lista.firstElementChild;
const ultimoItem = lista.lastElementChild;

primerItem.style.color = 'green';
ultimoItem.style.color = 'red';

// lastElementChild vs lastChild
// lastElementChild: solo elementos
// lastChild: incluye nodos de texto

// Condicional: si solo tiene un elemento
if (lista.firstElementChild === lista.lastElementChild) {
  console.log('La lista tiene solo un elemento');
}
