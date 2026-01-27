// Seleccionar primer elemento con selector CSS

// HTML:
// <div class="contenedor">
//   <p class="importante">Primer párrafo importante</p>
//   <p>Segundo párrafo</p>
//   <p class="importante">Tercer párrafo importante</p>
// </div>

// Seleccionar el primer párrafo con clase "importante"
const primero = document.querySelector('.importante');

console.log(primero);           // <p class="importante">Primer párrafo importante</p>
console.log(primero.textContent); // "Primer párrafo importante"

// Seleccionar el primer párrafo dentro de contenedor
const parrafo = document.querySelector('.contenedor p');
console.log(parrafo.textContent); // "Primer párrafo importante"

// Si no existe, devuelve null
const noExiste = document.querySelector('.no-existe');
console.log(noExiste); // null
