// Obtener estilos computados (del CSS aplicado)

// HTML: <div id="caja">Contenido</div>
// CSS: #caja { color: blue; padding: 15px; }

const caja = document.getElementById('caja');

// Obtener todos los estilos computados
const estilos = window.getComputedStyle(caja);

// Leer propiedades específicas
console.log(estilos.color);           // "rgb(0, 0, 255)" o similar
console.log(estilos.padding);         // "15px"
console.log(estilos.backgroundColor); // "rgba(0, 0, 0, 0)" o similar

// Los estilos computados devuelven valores reales aplicados
// No solo los estilos en línea

// Ejemplo: obtener ancho real
const ancho = estilos.width;
console.log(ancho); // "200px" (el ancho real)

// Obtener fuente
const fuente = estilos.fontFamily;
console.log(fuente); // "Arial, sans-serif"

// Obtener posición
const posicion = estilos.position;
console.log(posicion); // "static", "relative", "absolute", etc.

// Consejo: getComputedStyle es útil para leer valores
// pero no para escribir (usar .style para eso)
