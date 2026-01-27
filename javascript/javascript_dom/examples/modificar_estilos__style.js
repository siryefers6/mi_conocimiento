// Modificar estilos CSS directamente

// HTML: <div id="caja">Contenido</div>

const caja = document.getElementById('caja');

// Modificar propiedad CSS individual
caja.style.color = 'red';
caja.style.backgroundColor = 'yellow';
caja.style.padding = '20px';
caja.style.borderRadius = '5px';

// Los nombres de propiedades van en camelCase
// CSS: font-size → JavaScript: fontSize
// CSS: background-color → JavaScript: backgroundColor

caja.style.fontSize = '18px';
caja.style.fontWeight = 'bold';
caja.style.textAlign = 'center';

// Leer estilos en línea
console.log(caja.style.color); // "red"
console.log(caja.style.padding); // "20px"

// Remover estilo estableciéndolo a vacío
caja.style.color = '';

// Agregar múltiples estilos
const elemento = document.getElementById('elemento');
elemento.style.width = '200px';
elemento.style.height = '100px';
elemento.style.display = 'flex';
elemento.style.alignItems = 'center';
elemento.style.justifyContent = 'center';
