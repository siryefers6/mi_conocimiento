// Seleccionar todos los elementos con selector CSS

// HTML:
// <div class="contenedor">
//   <p class="importante">Párrafo 1</p>
//   <p>Párrafo 2</p>
//   <p class="importante">Párrafo 3</p>
// </div>

// Seleccionar todos los párrafos con clase "importante"
const importantes = document.querySelectorAll('.importante');

console.log(importantes);           // NodeList(2) [p.importante, p.importante]
console.log(importantes.length);    // 2

// querySelectorAll devuelve NodeList (similar a array)
// Se puede usar forEach directamente
importantes.forEach(function(elemento) {
  console.log(elemento.textContent);
});

// También se puede usar for tradicional
for (let i = 0; i < importantes.length; i++) {
  console.log(importantes[i].textContent);
}

// Seleccionar con selectores más complejos
const todosParrafos = document.querySelectorAll('.contenedor p');
console.log(todosParrafos.length); // 3
