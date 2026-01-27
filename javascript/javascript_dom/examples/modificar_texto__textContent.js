// Modificar contenido de texto plano

// HTML: <div id="mensaje">Hola Mundo</div>

const mensaje = document.getElementById('mensaje');

// Obtener texto
console.log(mensaje.textContent); // "Hola Mundo"

// Modificar texto
mensaje.textContent = 'Nuevo mensaje';

// textContent NO interpreta HTML
mensaje.textContent = '<p>Este es texto, no HTML</p>';
// Muestra literalmente: "<p>Este es texto, no HTML</p>"

// Útil para contenido dinámico sin riesgo de inyección HTML
const nombre = 'Juan';
mensaje.textContent = 'Bienvenido ' + nombre;

// También funciona con template literals
const edad = 25;
mensaje.textContent = `${nombre} tiene ${edad} años`;
