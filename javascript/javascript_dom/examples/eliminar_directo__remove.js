// Eliminar elemento directamente (remove)

// HTML: <div id="caja">Contenido</div>

const caja = document.getElementById('caja');

// Eliminar el elemento directamente
caja.remove();
// El elemento se quita del DOM

// Más simple que removeChild
// No es necesario acceder al padre

// Ejemplo práctico: eliminar tarjeta
const tarjeta = document.getElementById('tarjeta-1');
const botonEliminar = tarjeta.querySelector('.boton-eliminar');

botonEliminar.addEventListener('click', function() {
  tarjeta.remove();
});

// Eliminar múltiples elementos
const elementosAEliminar = document.querySelectorAll('.temporal');
elementosAEliminar.forEach(function(elemento) {
  elemento.remove();
});

// Eliminar con confirmación
const articulo = document.getElementById('articulo');
if (confirm('¿Desea eliminar este artículo?')) {
  articulo.remove();
}

// remove() es moderno (IE11+)
// Para navegadores antiguos, usar removeChild()
