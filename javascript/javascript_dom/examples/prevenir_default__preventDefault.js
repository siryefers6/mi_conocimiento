// Prevenir comportamiento por defecto (preventDefault)

// HTML: <a id="enlace" href="https://ejemplo.com">Ir a ejemplo</a>

const enlace = document.getElementById('enlace');

// Prevenir que el navegador abra el enlace
enlace.addEventListener('click', function(evento) {
  evento.preventDefault();
  console.log('Enlace no se abrió');
  
  // Hacer algo personalizado
  console.log('En lugar de ir al enlace, hacemos otra cosa');
});

// Prevenir envío de formulario por defecto
// HTML: <form id="formulario">
//   <input type="text" name="usuario">
//   <button type="submit">Enviar</button>
// </form>

const formulario = document.getElementById('formulario');

formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();
  console.log('Formulario no se envió (no recargó la página)');
  
  // Validar o procesar manualmente
  const usuario = formulario.elements.usuario.value;
  if (usuario.length > 0) {
    console.log('Usuario válido:', usuario);
  }
});

// Prevenir menú contextual (clic derecho)
document.addEventListener('contextmenu', function(evento) {
  evento.preventDefault();
  console.log('Menú contextual bloqueado');
});

// Casos comunes donde se usa preventDefault():
// - Formularios (validar antes de enviar)
// - Enlaces (hacer acciones personalizadas)
// - Drag & drop (permitir drop)
// - Comportamientos del navegador personalizados

// NOTA: preventDefault() NO detiene la propagación del evento
// Para detener la propagación usar stopPropagation()
