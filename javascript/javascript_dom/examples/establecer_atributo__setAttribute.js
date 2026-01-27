// Establecer atributo HTML

// HTML: <a id="enlace">Enlace</a>

const enlace = document.getElementById('enlace');

// Establecer atributo href
enlace.setAttribute('href', 'https://ejemplo.com');

// Establecer atributo class
enlace.setAttribute('class', 'enlace-externo');

// Establecer atributo personalizado (data)
enlace.setAttribute('data-id', '123');
enlace.setAttribute('data-tipo', 'premium');

// Establecer múltiples atributos
const imagen = document.getElementById('imagen');
imagen.setAttribute('src', 'foto.jpg');
imagen.setAttribute('alt', 'Foto de perfil');
imagen.setAttribute('width', '200');

// Si el atributo existe, lo actualiza
// Si no existe, lo crea
enlace.setAttribute('title', 'Ir a ejemplo.com');
console.log(enlace.getAttribute('title')); // "Ir a ejemplo.com"
