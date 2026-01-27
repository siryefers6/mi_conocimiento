// Establecer foco en elemento

// HTML: <input type="text" id="nombre">
//       <button id="boton">Enfocar nombre</button>

const nombre = document.getElementById('nombre');
const boton = document.getElementById('boton');

// Dar foco al elemento
boton.addEventListener('click', function() {
  nombre.focus();
  // Ahora el nombre input tiene foco y está listo para escribir
});

// focus() automáticamente hace scroll al elemento si está fuera de vista
const elemento_lejano = document.getElementById('elemento-al-final');

boton.addEventListener('click', function() {
  elemento_lejano.focus();
  // Scroll suavemente al elemento
});

// Dar foco con opciones (moderno)
nombre.focus({ preventScroll: false }); // Scroll al elemento
nombre.focus({ preventScroll: true });  // No hacer scroll

// Dar foco y seleccionar todo el texto
nombre.addEventListener('focus', function() {
  nombre.select(); // Selecciona todo el contenido
});

// O simplemente:
nombre.focus();
nombre.select();

// Secuencia de enfoque en un formulario
const inputs = document.querySelectorAll('input');

// Al presionar Tab, moverse entre inputs
inputs.forEach(function(input, indice) {
  input.addEventListener('keydown', function(evento) {
    if (evento.key === 'Enter') {
      evento.preventDefault();
      
      // Enfocar el siguiente input
      if (indice < inputs.length - 1) {
        inputs[indice + 1].focus();
      } else {
        // Si es el último, enfocar el primero
        inputs[0].focus();
      }
    }
  });
});

// Verificar si tiene foco
if (nombre === document.activeElement) {
  console.log('El nombre input tiene foco');
}
