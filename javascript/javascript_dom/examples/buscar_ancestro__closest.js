// Buscar ancestro que cumple selector (closest)

// HTML: <ul>
//   <li class="item">
//     <button class="boton">Eliminar</button>
//   </li>
// </ul>

const boton = document.querySelector('.boton');

// Buscar el ancestro más cercano con clase "item"
const item = boton.closest('.item');
console.log(item); // <li class="item">...</li>

// Buscar el ancestro más cercano que sea li
const listItem = boton.closest('li');
console.log(listItem); // <li>...</li>

// Buscar si existe un ancestro que cumple la condición
const ancestro = boton.closest('div');
if (ancestro) {
  console.log('Encontró un div ancestro');
} else {
  console.log('No hay div ancestro');
}

// Usar selectores complejos
const elemento = boton.closest('ul li.item');
console.log(elemento);

// Útil para delegación de eventos
const lista = document.getElementById('lista');

lista.addEventListener('click', function(evento) {
  // Encontrar el item clickeado
  const item = evento.target.closest('.item');
  
  if (item) {
    console.log('Clickeaste en:', item);
    // Eliminar el item
    item.remove();
  }
});

// Diferencia entre closest() y querySelector()
// closest() - busca en ancestros (hacia arriba)
// querySelector() - busca en descendientes (hacia abajo)

const li = document.querySelector('li');

// Buscar ancestro ul
const ul = li.closest('ul'); // true, encontrado

// No encontrar elemento que no está en ancestros
const div = li.closest('div'); // null, no encontrado
