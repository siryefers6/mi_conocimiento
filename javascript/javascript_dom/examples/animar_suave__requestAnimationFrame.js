// Animar suave con requestAnimationFrame

// HTML: <div id="caja">Animar</div>

const caja = document.getElementById('caja');

let posicion = 0;

// requestAnimationFrame: se ejecuta 60 veces por segundo (suave)
function animar() {
  posicion += 2;
  caja.style.left = posicion + 'px';
  
  // Repetir si no llegamos al final
  if (posicion < 300) {
    requestAnimationFrame(animar);
  }
}

// Iniciar animación
animar();

// Ejemplo: animar desde 0 a 100%
let progreso = 0;

function animarProgreso() {
  progreso += 2;
  caja.style.width = progreso + '%';
  
  if (progreso < 100) {
    requestAnimationFrame(animarProgreso);
  }
}

// Animar múltiples propiedades
let x = 0;
let y = 0;

function animarMultiple() {
  x += 2;
  y += 1;
  
  caja.style.left = x + 'px';
  caja.style.top = y + 'px';
  
  if (x < 300) {
    requestAnimationFrame(animarMultiple);
  }
}

// Detener animación guardando el ID
let animacionId;

function iniciar() {
  animacionId = requestAnimationFrame(animar);
}

function detener() {
  cancelAnimationFrame(animacionId);
}

// Ventajas de requestAnimationFrame:
// - Sincronizado con refresh del navegador (suave)
// - Mejor rendimiento que setInterval
// - Se pausa cuando la pestaña no está activa
