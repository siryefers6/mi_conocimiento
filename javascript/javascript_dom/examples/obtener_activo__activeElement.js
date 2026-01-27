// Obtener elemento con foco activo

// HTML: <input id="email" type="email">
//       <input id="password" type="password">

// Obtener elemento que actualmente tiene foco
const activo = document.activeElement;
console.log(activo); // El input que tiene foco

// Verificar cuál input tiene foco
if (document.activeElement === document.getElementById('email')) {
  console.log('El foco está en email');
} else if (document.activeElement === document.getElementById('password')) {
  console.log('El foco está en password');
}

// Escuchar cambio de foco
const email = document.getElementById('email');
const password = document.getElementById('password');

email.addEventListener('focus', function() {
  console.log('Email tiene foco');
  console.log('activeElement:', document.activeElement.id);
});

email.addEventListener('blur', function() {
  console.log('Email perdió foco');
  console.log('activeElement:', document.activeElement.id);
});

// Hacer que un elemento tenga foco
function enfocarEmail() {
  email.focus();
  console.log('Ahora activeElement es:', document.activeElement.id);
}

// Después de hacer clic en un botón
const boton = document.getElementById('boton');
boton.addEventListener('click', function() {
  email.focus(); // Mover foco al email
});

// Verificar si un elemento tiene foco
if (email === document.activeElement) {
  console.log('Email tiene foco');
}

// El elemento body tiene foco si nada más lo tiene
if (document.activeElement === document.body) {
  console.log('Ningún elemento tiene foco');
}
