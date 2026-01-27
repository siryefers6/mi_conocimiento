// Acceder directamente a atributos como propiedades

// HTML: <img id="foto" src="perfil.jpg" alt="Mi foto">

const foto = document.getElementById('foto');

// Acceso directo a propiedades estándar
console.log(foto.src);  // "https://..../perfil.jpg"
console.log(foto.alt);  // "Mi foto"

// Modificar propiedades directamente
foto.src = 'nueva-foto.jpg';
foto.alt = 'Nueva foto';

// Algunas propiedades comunes:
// - elemento.id
// - elemento.className
// - elemento.href (para enlaces)
// - elemento.src (para imágenes y scripts)
// - elemento.type (para inputs)
// - elemento.disabled (para botones)
// - elemento.checked (para checkboxes y radios)

// HTML: <input type="checkbox" id="acepto">
const acepto = document.getElementById('acepto');

// Leer propiedad directamente
console.log(acepto.checked); // true/false

// Modificar propiedad directamente
acepto.checked = true;
acepto.type = 'checkbox';
