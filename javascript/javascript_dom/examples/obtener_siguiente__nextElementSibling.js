// Obtener siguiente hermano

// HTML: <ul>
//   <li id="item1">Elemento 1</li>
//   <li id="item2">Elemento 2</li>
//   <li id="item3">Elemento 3</li>
// </ul>

const item1 = document.getElementById('item1');
const item2 = document.getElementById('item2');

// Obtener siguiente hermano de item1
const siguiente = item1.nextElementSibling;
console.log(siguiente.textContent); // "Elemento 2"
console.log(siguiente === item2); // true

// Obtener siguiente del siguiente
const siguiente2 = item2.nextElementSibling;
console.log(siguiente2.textContent); // "Elemento 3"

// El siguiente del último es null
const item3 = document.getElementById('item3');
const nada = item3.nextElementSibling;
console.log(nada); // null

// Verificar si tiene siguiente hermano
if (item1.nextElementSibling) {
  console.log('Hay elemento siguiente');
}

// Modificar siguiente hermano
item1.nextElementSibling.style.color = 'blue';

// nextElementSibling vs nextSibling
// nextElementSibling: solo elementos
// nextSibling: incluye nodos de texto
