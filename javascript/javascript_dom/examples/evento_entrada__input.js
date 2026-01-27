// Evento input (entrada de datos)

// HTML: <input type="text" id="buscador" placeholder="Buscar...">

const buscador = document.getElementById('buscador');

// Escuchar entrada de texto en tiempo real
buscador.addEventListener('input', function(evento) {
  console.log('Texto ingresado:', evento.target.value);
});

// Filtrar una lista mientras escribes
// HTML: <input type="text" id="filtro">
//       <ul id="lista">
//         <li>Manzana</li>
//         <li>Banana</li>
//         <li>Cereza</li>
//       </ul>

const filtro = document.getElementById('filtro');
const items = document.querySelectorAll('#lista li');

filtro.addEventListener('input', function(evento) {
  const texto = evento.target.value.toLowerCase();
  
  items.forEach(function(item) {
    if (item.textContent.toLowerCase().includes(texto)) {
      item.style.display = '';
    } else {
      item.style.display = 'none';
    }
  });
});

// input se dispara mientras escribes (en tiempo real)
// change se dispara solo cuando terminas de editar

// Validar mientras escribes
const email = document.getElementById('email');

email.addEventListener('input', function() {
  if (email.value.includes('@')) {
    email.classList.remove('error');
    email.classList.add('valido');
  } else {
    email.classList.remove('valido');
    email.classList.add('error');
  }
});
