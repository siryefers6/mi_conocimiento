// Obtener atributo HTML

// HTML: <a id="enlace" href="https://ejemplo.com" data-id="123">Enlace</a>

const enlace = document.getElementById('enlace');

// Obtener atributo href
const href = enlace.getAttribute('href');
console.log(href); // "https://ejemplo.com"

// Obtener atributo personalizado (data)
const id = enlace.getAttribute('data-id');
console.log(id); // "123"

// Obtener atributo que no existe devuelve null
const noExiste = enlace.getAttribute('no-existe');
console.log(noExiste); // null

// HTML: <button id="boton" disabled>Botón</button>
const boton = document.getElementById('boton');
const deshabilitado = boton.getAttribute('disabled');
console.log(deshabilitado); // "" o "disabled"
