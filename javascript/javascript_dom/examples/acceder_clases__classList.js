// Acceder a la lista de clases CSS

// HTML: <div id="elemento" class="activo premium">Contenido</div>

const elemento = document.getElementById('elemento');

// Obtener classList (objeto especial para manejar clases)
const clases = elemento.classList;

console.log(clases);           // DOMTokenList(2) ['activo', 'premium']
console.log(clases.length);    // 2

// Iterar las clases
for (let i = 0; i < clases.length; i++) {
  console.log(clases[i]);
}
// Salida:
// "activo"
// "premium"

// Acceder a clase específica por índice
console.log(clases[0]); // "activo"
console.log(clases[1]); // "premium"

// classList ofrece métodos útiles:
// - add()      - agregar clase
// - remove()   - eliminar clase
// - toggle()   - alternar clase
// - contains() - verificar si tiene clase
