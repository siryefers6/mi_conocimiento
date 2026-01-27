// Enviar formulario

// HTML: <form id="formulario">
//   <input type="text" name="usuario">
//   <input type="email" name="email">
//   <button type="submit">Enviar</button>
// </form>

const formulario = document.getElementById('formulario');

// Enviar formulario programáticamente
function enviarFormulario() {
  formulario.submit();
}

// Llamar función al hacer clic en botón
// O en cualquier otro evento

// Enviar con validación
formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();
  
  // Validar datos
  const usuario = formulario.elements.usuario.value;
  const email = formulario.elements.email.value;
  
  if (usuario === '' || email === '') {
    alert('Completar todos los campos');
    return;
  }
  
  // Enviar (opcional con fetch o AJAX)
  console.log('Enviando:', { usuario, email });
  
  // Si todo está bien, enviar
  // formulario.submit();
});

// Enviar con fetch (AJAX moderno)
formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();
  
  // Obtener datos del formulario
  const formData = new FormData(formulario);
  
  // Enviar con fetch
  fetch('/procesar-formulario', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    console.log('Respuesta:', data);
    alert('Formulario enviado con éxito');
  })
  .catch(error => console.error('Error:', error));
});
