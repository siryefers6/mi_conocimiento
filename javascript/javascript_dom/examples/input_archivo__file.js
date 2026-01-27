// Input de tipo archivo

// HTML: <input type="file" id="cargador">

const cargador = document.getElementById('cargador');

// Escuchar cuando se selecciona un archivo
cargador.addEventListener('change', function(evento) {
  console.log('Archivo seleccionado');
});

// Atributos útiles
// - accept: ".jpg,.png" o "image/*"
// - multiple: permite múltiples archivos
// - capture: captura cámara/micrófono

// HTML: <input type="file" id="fotos" accept="image/*" multiple>

const fotos = document.getElementById('fotos');

fotos.addEventListener('change', function(evento) {
  console.log('Archivos seleccionados:', evento.target.files);
});

// Hacer clic en input desde un botón personalizado
// HTML: <button id="boton">Seleccionar archivo</button>
//       <input type="file" id="entrada" style="display: none;">

const boton = document.getElementById('boton');
const entrada = document.getElementById('entrada');

boton.addEventListener('click', function() {
  entrada.click(); // Simula clic en el input
});

// Mostrar nombre del archivo
const inputArchivo = document.getElementById('archivo');
const nombreArchivo = document.getElementById('nombre');

inputArchivo.addEventListener('change', function() {
  if (inputArchivo.files.length > 0) {
    nombreArchivo.textContent = inputArchivo.files[0].name;
  }
});
