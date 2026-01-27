// Obtener y modificar valor de input

// HTML: <input type="text" id="email" value="">

const input = document.getElementById('email');

// Obtener valor actual
console.log(input.value); // ""

// Modificar valor
input.value = 'usuario@ejemplo.com';
console.log(input.value); // "usuario@ejemplo.com"

// Limpiar input
input.value = '';

// Funciona con diferentes tipos de input
// HTML: <input type="number" id="cantidad" value="0">
const cantidad = document.getElementById('cantidad');
cantidad.value = 10;

// HTML: <input type="checkbox" id="acepto">
const acepto = document.getElementById('acepto');
console.log(acepto.checked); // true/false
acepto.checked = true;
