// Evento load (archivo cargado)

// HTML: <input type="file" id="archivo">

const archivo_input = document.getElementById('archivo');

archivo_input.addEventListener('change', function() {
  const archivo = archivo_input.files[0];
  
  if (archivo) {
    const reader = new FileReader();
    
    // Evento load: se dispara cuando el archivo se cargó completamente
    reader.addEventListener('load', function(evento) {
      console.log('Archivo cargado');
      console.log('Contenido:', evento.target.result);
      console.log('Tamaño cargado:', evento.loaded, 'bytes');
    });
    
    // Evento progress: se dispara mientras se carga
    reader.addEventListener('progress', function(evento) {
      if (evento.lengthComputable) {
        const porcentaje = (evento.loaded / evento.total) * 100;
        console.log('Cargado:', porcentaje.toFixed(2) + '%');
      }
    });
    
    // Evento error: si hay error durante la carga
    reader.addEventListener('error', function(evento) {
      console.error('Error:', evento.target.error.message);
    });
    
    // Evento abort: si se cancela la carga
    reader.addEventListener('abort', function() {
      console.log('Carga cancelada');
    });
    
    // Iniciar lectura
    reader.readAsText(archivo);
  }
});

// Procesar imagen cuando carga
const img_input = document.getElementById('imagen');

img_input.addEventListener('change', function() {
  const archivo = img_input.files[0];
  const reader = new FileReader();
  
  reader.addEventListener('load', function() {
    // Crear elemento img
    const img = document.createElement('img');
    img.src = reader.result;
    
    // Esperar a que la imagen cargue
    img.addEventListener('load', function() {
      console.log('Imagen ancho:', img.width);
      console.log('Imagen alto:', img.height);
      
      // Agregar a la página
      document.body.appendChild(img);
    });
  });
  
  reader.readAsDataURL(archivo);
});
