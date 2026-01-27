// Escuchar evento en un elemento

// HTML: <button id="boton">Presionar</button>

const boton = document.getElementById('boton');

// Escuchar evento click
boton.addEventListener('click', function() {
  console.log('¡Se presionó el botón!');
});

// Escuchar con función nombrada
function manejador() {
  console.log('Manejador ejecutado');
}

boton.addEventListener('click', manejador);

// Escuchar con función flecha
boton.addEventListener('click', () => {
  console.log('Función flecha');
});

// Escuchar múltiples eventos
const input = document.getElementById('email');

input.addEventListener('focus', function() {
  console.log('Input enfocado');
});

input.addEventListener('blur', function() {
  console.log('Input desfocado');
});

input.addEventListener('input', function() {
  console.log('Texto ingresado:', input.value);
});

// addEventListener permite múltiples escuchadores
// Todos se ejecutarán en orden
boton.addEventListener('click', function() {
  console.log('Primero');
});

boton.addEventListener('click', function() {
  console.log('Segundo');
});
