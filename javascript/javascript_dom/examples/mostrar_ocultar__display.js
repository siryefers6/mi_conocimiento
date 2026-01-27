// Mostrar/ocultar elemento

// HTML: <div id="modal">Contenido modal</div>
//       <button id="boton">Mostrar/Ocultar</button>

const modal = document.getElementById('modal');
const boton = document.getElementById('boton');

// Ocultar elemento (no ocupa espacio - display: none)
modal.style.display = 'none';

// Mostrar elemento
modal.style.display = 'block'; // o 'flex', 'grid', etc.

// Toggle mostrar/ocultar
boton.addEventListener('click', function() {
  if (modal.style.display === 'none') {
    modal.style.display = 'block';
  } else {
    modal.style.display = 'none';
  }
});

// Forma más simple con toggle
boton.addEventListener('click', function() {
  modal.classList.toggle('oculto');
  // CSS: .oculto { display: none; }
});

// Valores comunes de display
// - 'none' - no mostrar (no ocupa espacio)
// - 'block' - bloque (ocupa todo el ancho)
// - 'inline' - línea (solo lo que necesita)
// - 'flex' - flexbox
// - 'grid' - grid
// - 'inline-block' - híbrido

// Visibilidad vs Display
// display: none - no ocupa espacio
// visibility: hidden - ocupa espacio pero invisible

modal.style.visibility = 'hidden'; // Invisible pero reserva espacio
modal.style.visibility = 'visible'; // Visible
