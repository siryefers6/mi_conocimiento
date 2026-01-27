// Seleccionar elemento por ID

// HTML: <div id="miElemento">Contenido</div>

// Obtener elemento por ID
const elemento = document.getElementById('miElemento');

// Usar el elemento
console.log(elemento);           // <div id="miElemento">Contenido</div>
console.log(elemento.textContent); // "Contenido"

// Modificar el elemento
elemento.textContent = 'Nuevo contenido';
