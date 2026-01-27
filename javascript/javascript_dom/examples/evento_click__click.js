// Evento click (clic)

// HTML: <button id="boton">Presionar</button>

const boton = document.getElementById('boton');

// Escuchar clic
boton.addEventListener('click', function(evento) {
  console.log('¡Se presionó el botón!');
  console.log('Evento:', evento);
});

// También se puede asignar directamente
// boton.onclick = function() { ... };

// Evento click con parámetro de evento
const caja = document.getElementById('caja');

caja.addEventListener('click', function(evento) {
  // evento.target es el elemento que fue clicado
  console.log('Clicaste en:', evento.target);
  
  // Cambiar color
  evento.target.style.backgroundColor = 'yellow';
});

// Click en múltiples elementos
const botones = document.querySelectorAll('.boton');

botones.forEach(function(btn) {
  btn.addEventListener('click', function() {
    console.log('Presionaste: ' + btn.textContent);
  });
});

// Contar clics
let contador = 0;
const botonContar = document.getElementById('boton-contar');

botonContar.addEventListener('click', function() {
  contador++;
  console.log('Clics: ' + contador);
  botonContar.textContent = 'Clicado ' + contador + ' veces';
});
