// Evento mouseover (ratón sobre elemento)

// HTML: <div id="caja">Pasa el ratón aquí</div>

const caja = document.getElementById('caja');

// Escuchar cuando el ratón entra
caja.addEventListener('mouseover', function() {
  console.log('Ratón sobre la caja');
  caja.style.backgroundColor = 'lightblue';
});

// Escuchar cuando el ratón sale (mouseout)
caja.addEventListener('mouseout', function() {
  console.log('Ratón fuera de la caja');
  caja.style.backgroundColor = '';
});

// Efecto hover con eventos
const boton = document.getElementById('boton');

boton.addEventListener('mouseover', function() {
  boton.classList.add('hover');
});

boton.addEventListener('mouseout', function() {
  boton.classList.remove('hover');
});

// mouseenter y mouseleave (alternativas)
// No se propagan a elementos hijos
caja.addEventListener('mouseenter', function() {
  console.log('Entraste a la caja');
});

caja.addEventListener('mouseleave', function() {
  console.log('Saliste de la caja');
});

// Diferencia:
// mouseover/mouseout - se propagan
// mouseenter/mouseleave - no se propagan
