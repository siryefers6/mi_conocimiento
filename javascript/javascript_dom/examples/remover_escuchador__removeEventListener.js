// Remover escuchador de eventos

// HTML: <button id="boton">Presionar</button>

const boton = document.getElementById('boton');

// Definir función para poder removerla después
function manejadorClick() {
  console.log('¡Botón presionado!');
}

// Agregar escuchador
boton.addEventListener('click', manejadorClick);

// Remover escuchador
boton.removeEventListener('click', manejadorClick);

// Después de remover, el evento no se dispara más
// Presionar el botón no hace nada

// Ejemplo: agregar y remover condicionalmente
const botonToggle = document.getElementById('boton-toggle');

function contador() {
  console.log('Contando...');
}

// Función para activar el escucha
function activar() {
  botonToggle.addEventListener('click', contador);
  console.log('Escuchador activado');
}

// Función para desactivar
function desactivar() {
  botonToggle.removeEventListener('click', contador);
  console.log('Escuchador desactivado');
}

// Remover todos los escuchadores
// Para eso, necesitamos una referencia a la función
// o clonar el elemento

// Clonar elemento (remueve todos los escuchadores)
const elementoAntiguo = document.getElementById('elemento');
const elementoNuevo = elementoAntiguo.cloneNode(true);
elementoAntiguo.replaceWith(elementoNuevo);
// Ahora elementoNuevo no tiene escuchadores
