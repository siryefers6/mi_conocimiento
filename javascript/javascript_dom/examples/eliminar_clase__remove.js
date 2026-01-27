// Eliminar clase CSS

// HTML: <div id="elemento" class="activo error premium">Contenido</div>

const elemento = document.getElementById('elemento');

// Eliminar una clase
elemento.classList.remove('error');
// Resultado: class="activo premium"

// Eliminar múltiples clases
elemento.classList.remove('activo', 'premium');
// Resultado: class="" (o vacío)

// Si la clase no existe, no produce error
elemento.classList.remove('no-existe');

// Eliminar y agregar alternativamente
const boton = document.getElementById('boton');
boton.classList.add('deshabilitado');
// Resultado: class="deshabilitado"

boton.classList.remove('deshabilitado');
// Resultado: class="" (o vacío)

// Ejemplo práctico: remover clase de error
const input = document.getElementById('email');
input.classList.remove('error-input');

// O remover múltiples clases relacionadas
input.classList.remove('error-input', 'borde-rojo', 'fondo-alerta');
