// Obtener hermano anterior

// HTML: <ul>
//   <li id="item1">Elemento 1</li>
//   <li id="item2">Elemento 2</li>
//   <li id="item3">Elemento 3</li>
// </ul>

const item3 = document.getElementById('item3');
const item2 = document.getElementById('item2');

// Obtener hermano anterior de item3
const anterior = item3.previousElementSibling;
console.log(anterior.textContent); // "Elemento 2"
console.log(anterior === item2); // true

// Obtener anterior del anterior
const anterior2 = item2.previousElementSibling;
console.log(anterior2.textContent); // "Elemento 1"

// El anterior del primero es null
const item1 = document.getElementById('item1');
const nada = item1.previousElementSibling;
console.log(nada); // null

// Verificar si tiene hermano anterior
if (item3.previousElementSibling) {
  console.log('Hay elemento anterior');
}

// Modificar hermano anterior
item3.previousElementSibling.classList.add('antes-final');

// Obtener hermano anterior y siguiente
const centro = item2;
const izq = centro.previousElementSibling;
const der = centro.nextElementSibling;

console.log(izq.textContent); // "Elemento 1"
console.log(der.textContent); // "Elemento 3"

// previousElementSibling vs previousSibling
// previousElementSibling: solo elementos
// previousSibling: incluye nodos de texto
