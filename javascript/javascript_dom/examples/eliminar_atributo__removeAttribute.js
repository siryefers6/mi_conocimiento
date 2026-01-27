// Eliminar atributo HTML

// HTML: <img id="foto" src="perfil.jpg" alt="Foto" title="Mi foto">

const foto = document.getElementById('foto');

// Eliminar atributo title
foto.removeAttribute('title');

// Eliminamos el atributo alt
foto.removeAttribute('alt');

// Después de remover:
// <img id="foto" src="perfil.jpg">

// HTML: <button id="boton" disabled>Botón</button>
const boton = document.getElementById('boton');

// Remover atributo disabled
boton.removeAttribute('disabled');

// Después de remover:
// <button id="boton">Botón</button>

// Remover atributo personalizado
const enlace = document.getElementById('enlace');
enlace.removeAttribute('data-id');
