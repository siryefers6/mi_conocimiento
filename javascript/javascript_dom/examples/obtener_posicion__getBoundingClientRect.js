// Obtener posición en el viewport (getBoundingClientRect)

// HTML: <div id="caja">Contenido</div>

const caja = document.getElementById('caja');

// Obtener rectángulo con posición y dimensiones
const rect = caja.getBoundingClientRect();

// Propiedades del rectángulo
console.log(rect.width);   // Ancho del elemento
console.log(rect.height);  // Alto del elemento
console.log(rect.top);     // Distancia desde la parte superior del viewport
console.log(rect.bottom);  // Distancia desde la parte inferior
console.log(rect.left);    // Distancia desde la izquierda del viewport
console.log(rect.right);   // Distancia desde la derecha
console.log(rect.x);       // Lo mismo que left
console.log(rect.y);       // Lo mismo que top

// Verificar si elemento es visible en viewport
function esVisible(elemento) {
  const rect = elemento.getBoundingClientRect();
  return (
    rect.top < window.innerHeight &&
    rect.bottom > 0 &&
    rect.left < window.innerWidth &&
    rect.right > 0
  );
}

if (esVisible(caja)) {
  console.log('El elemento es visible');
}

// Scroll suave a un elemento
function scrollAElemento(elemento) {
  const rect = elemento.getBoundingClientRect();
  window.scrollBy(rect.left, rect.top);
}

// O usar scrollIntoView
caja.scrollIntoView({ behavior: 'smooth' });

// Detectar cuando un elemento entra en viewport
window.addEventListener('scroll', function() {
  if (esVisible(caja)) {
    caja.classList.add('en-vista');
  }
});
