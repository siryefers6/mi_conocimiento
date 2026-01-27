// Leer valor de input

// HTML: <input type="text" id="nombre" value="">

const input = document.getElementById('nombre');

// Leer valor actual
console.log(input.value); // "" (vacío inicialmente)

// Escribir algo en el input
input.value = 'Juan';
console.log(input.value); // "Juan"

// Leer después de que el usuario escriba
input.addEventListener('input', function() {
  console.log('Valor actual:', input.value);
});

// Con diferentes tipos de input
// HTML: <input type="number" id="edad">
const edad = document.getElementById('edad');
edad.value = 25;
console.log(Number(edad.value)); // 25 como número

// HTML: <input type="checkbox" id="acepto">
const acepto = document.getElementById('acepto');
console.log(acepto.checked); // true/false

// HTML: <input type="radio" name="genero">
const radios = document.querySelectorAll('input[name="genero"]');
radios.forEach(function(radio) {
  if (radio.checked) {
    console.log('Seleccionado:', radio.value);
  }
});

// HTML: <select id="pais">
//   <option value="">Seleccionar</option>
//   <option value="mx">México</option>
//   <option value="ar">Argentina</option>
// </select>
const pais = document.getElementById('pais');
console.log(pais.value); // Valor seleccionado
