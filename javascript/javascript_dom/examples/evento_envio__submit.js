// Evento submit (envío de formulario)

// HTML: <form id="formulario">
//   <input type="text" name="nombre" required>
//   <input type="email" name="email" required>
//   <button type="submit">Enviar</button>
// </form>

const formulario = document.getElementById('formulario');

// Escuchar envío del formulario
formulario.addEventListener('submit', function(evento) {
  // Prevenir el comportamiento por defecto
  evento.preventDefault();
  
  console.log('Formulario enviado!');
  
  // Obtener datos del formulario
  const nombre = formulario.elements.nombre.value;
  const email = formulario.elements.email.value;
  
  console.log('Nombre:', nombre);
  console.log('Email:', email);
});

// Validar datos antes de enviar
const form = document.getElementById('form');

form.addEventListener('submit', function(evento) {
  // Obtener valores
  const input = form.querySelector('input[name="usuario"]');
  
  // Validar
  if (input.value.length < 3) {
    evento.preventDefault();
    alert('El usuario debe tener al menos 3 caracteres');
    return;
  }
  
  // Si es válido, permitir el envío (no hacer preventDefault)
  console.log('Datos válidos, enviando...');
});

// Resetear formulario después de envío
formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();
  
  // Procesar datos...
  
  // Limpiar formulario
  formulario.reset();
});
