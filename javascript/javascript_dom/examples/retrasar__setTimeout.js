// Retrasar ejecución con setTimeout

// Ejecutar función después de ciertos milisegundos
function saludar() {
  console.log('¡Hola!');
}

// Esperar 2 segundos (2000 ms)
setTimeout(saludar, 2000);

// Con función anónima
setTimeout(function() {
  console.log('Después de 3 segundos');
}, 3000);

// Con función flecha
setTimeout(() => {
  console.log('Después de 1 segundo');
}, 1000);

// Guardar ID para cancelar si es necesario
const id = setTimeout(function() {
  console.log('Esta función se cancelará');
}, 5000);

// Cancelar timeout
clearTimeout(id);
console.log('Se canceló el timeout');

// Ejemplo práctico: desaparecer un mensaje después de 3 segundos
const mensaje = document.getElementById('mensaje');

setTimeout(function() {
  mensaje.style.opacity = '0';
  setTimeout(function() {
    mensaje.remove();
  }, 300); // Dejar que termine la transición
}, 3000);

// Múltiples timeouts encadenados
setTimeout(function() {
  console.log('Paso 1');
  setTimeout(function() {
    console.log('Paso 2');
    setTimeout(function() {
      console.log('Paso 3');
    }, 1000);
  }, 1000);
}, 1000);

// Mejor con async/await o promesas
