// Validar formulario

// HTML: <form id="formulario">
//   <input type="text" name="nombre" required>
//   <input type="email" name="email" required>
//   <button type="submit">Enviar</button>
// </form>

const formulario = document.getElementById('formulario');

// Validar si el formulario es válido (campos requeridos llenos)
formulario.addEventListener('submit', function(evento) {
  // Comprobar validez del formulario HTML5
  if (!formulario.checkValidity()) {
    evento.preventDefault();
    console.log('Formulario inválido');
  } else {
    console.log('Formulario válido');
  }
});

// checkValidity() verifica:
// - required: campos obligatorios
// - type: tipo de dato correcto (email, number, etc.)
// - pattern: expresiones regulares
// - minlength/maxlength: longitud de texto
// - min/max: números

// Validación manual
const email = document.getElementById('email');
const nombre = document.getElementById('nombre');

formulario.addEventListener('submit', function(evento) {
  evento.preventDefault();
  
  // Validar nombre no vacío
  if (nombre.value.trim() === '') {
    alert('El nombre es requerido');
    return;
  }
  
  // Validar email con regex
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email.value)) {
    alert('Email inválido');
    return;
  }
  
  console.log('Datos válidos, enviando...');
});

// Validar campo por campo
nombre.addEventListener('blur', function() {
  if (nombre.value.trim() === '') {
    nombre.classList.add('error');
  } else {
    nombre.classList.remove('error');
  }
});
