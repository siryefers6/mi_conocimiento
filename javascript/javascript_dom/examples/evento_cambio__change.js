// Evento change (cambio)

// HTML: <select id="opciones">
//   <option value="">Seleccionar...</option>
//   <option value="rojo">Rojo</option>
//   <option value="azul">Azul</option>
// </select>

const opciones = document.getElementById('opciones');

// Escuchar cambio de select
opciones.addEventListener('change', function(evento) {
  console.log('Nuevo valor:', evento.target.value);
});

// También funciona con inputs type checkbox
// HTML: <input type="checkbox" id="acepto" value="sí">

const acepto = document.getElementById('acepto');

acepto.addEventListener('change', function(evento) {
  if (evento.target.checked) {
    console.log('Aceptado');
  } else {
    console.log('No aceptado');
  }
});

// Y con radio buttons
// HTML: <input type="radio" name="genero" value="M"> Masculino
//       <input type="radio" name="genero" value="F"> Femenino

const generos = document.querySelectorAll('input[name="genero"]');

generos.forEach(function(radio) {
  radio.addEventListener('change', function() {
    console.log('Seleccionado:', radio.value);
  });
});

// change se dispara cuando se termina de editar
// Se diferencia de 'input' que se dispara mientras escribes
