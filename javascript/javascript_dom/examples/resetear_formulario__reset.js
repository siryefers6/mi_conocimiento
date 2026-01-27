// Resetear (limpiar) formulario

// HTML: <form id="formulario">
//   <input type="text" name="nombre" value="">
//   <input type="email" name="email" value="">
//   <input type="checkbox" name="acepto" checked>
//   <button type="reset">Limpiar</button>
//   <button type="submit">Enviar</button>
// </form>

const formulario = document.getElementById('formulario');

// Resetear formulario (volver a valores iniciales)
function limpiarFormulario() {
  formulario.reset();
}

// Al presionar botón con type="reset"
// Se limpia automáticamente

// O programáticamente
const botonLimpiar = document.getElementById('boton-limpiar');
botonLimpiar.addEventListener('click', function(evento) {
  evento.preventDefault();
  formulario.reset();
});

// reset() devuelve todos los campos a su estado inicial
// - inputs vacios a ""
// - checked vuelven a su valor inicial
// - selects al primer option
// - textareas vacios

// Resetear solo algunos campos
botonLimpiar.addEventListener('click', function() {
  // Limpiar manualmente
  formulario.elements.nombre.value = '';
  formulario.elements.email.value = '';
  formulario.elements.acepto.checked = false;
});

// Resetear después de envío exitoso
formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();
  
  // Procesar datos...
  console.log('Datos enviados');
  
  // Limpiar el formulario
  formulario.reset();
  alert('Enviado correctamente');
});
