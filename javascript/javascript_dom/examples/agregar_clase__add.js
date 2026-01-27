// Agregar clase CSS

// HTML: <button id="boton">Presionar</button>
// CSS:
// .boton-activo { background-color: green; }

const boton = document.getElementById('boton');

// Agregar una clase
boton.classList.add('boton-activo');
// Resultado: <button id="boton" class="boton-activo">Presionar</button>

// Agregar múltiples clases
boton.classList.add('grande', 'importancia-alta');
// Resultado: class="boton-activo grande importancia-alta"

// Si la clase ya existe, no se duplica
boton.classList.add('boton-activo');
// Sigue siendo: class="boton-activo grande importancia-alta"

// Ejemplo práctico: agregar clase al hacer hover
const tarjeta = document.getElementById('tarjeta');
tarjeta.addEventListener('mouseover', function() {
  tarjeta.classList.add('hover-effect');
});

tarjeta.addEventListener('mouseout', function() {
  tarjeta.classList.remove('hover-effect');
});
