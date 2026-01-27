// Alternar clase CSS (toggle)

// HTML: <button id="boton">Alternar luz</button>

const boton = document.getElementById('boton');

// Si la clase existe, la elimina
// Si no existe, la agrega
boton.classList.toggle('activo');
// Primera vez: agrega clase → class="activo"
// Segunda vez: elimina clase → class=""
// Tercera vez: agrega clase → class="activo"

// Alternancia múltiple
const elemento = document.getElementById('elemento');
elemento.classList.toggle('visible');
elemento.classList.toggle('importante');

// Ejemplo práctico: menú desplegable
const menu = document.getElementById('menu');
const botonMenu = document.getElementById('boton-menu');

botonMenu.addEventListener('click', function() {
  menu.classList.toggle('mostrar');
});

// Ejemplo: tema oscuro/claro
const body = document.body;
const botonTema = document.getElementById('boton-tema');

botonTema.addEventListener('click', function() {
  body.classList.toggle('tema-oscuro');
});

// También puedes especificar el estado deseado (true = agregar, false = eliminar)
elemento.classList.toggle('activo', true);  // Siempre agrega
elemento.classList.toggle('activo', false); // Siempre elimina
