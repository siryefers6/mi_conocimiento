// Evento keydown (tecla presionada)

// HTML: <input type="text" id="entrada">

const entrada = document.getElementById('entrada');

// Escuchar cuando se presiona una tecla
entrada.addEventListener('keydown', function(evento) {
  console.log('Tecla presionada:', evento.key);
  console.log('Código:', evento.code);
});

// Detectar teclas específicas
entrada.addEventListener('keydown', function(evento) {
  if (evento.key === 'Enter') {
    console.log('Presionaste Enter');
    // Buscar o enviar
  }
  
  if (evento.key === 'Escape') {
    console.log('Presionaste Escape');
    // Cerrar modal o limpiar
  }
  
  if (evento.key === 'ArrowUp') {
    console.log('Flecha arriba');
  }
  
  if (evento.key === 'ArrowDown') {
    console.log('Flecha abajo');
  }
});

// Detectar combinaciones de teclas
document.addEventListener('keydown', function(evento) {
  // Ctrl + S para guardar
  if (evento.ctrlKey && evento.key === 's') {
    evento.preventDefault();
    console.log('Guardando...');
  }
  
  // Alt + Mayús para cambiar idioma
  if (evento.altKey && evento.shiftKey) {
    console.log('Combinación Alt + Mayús');
  }
});

// keyup - cuando se suelta la tecla
entrada.addEventListener('keyup', function(evento) {
  console.log('Tecla soltada:', evento.key);
});

// keypress - cuando se presiona una tecla (deprecated)
// Usar keydown o keyup en su lugar
