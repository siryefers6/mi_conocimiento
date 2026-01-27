// Leer archivo como Data URL

// HTML: <input type="file" id="imagen">
//       <img id="preview">

const imagen_input = document.getElementById('imagen');
const preview = document.getElementById('preview');

// Convertir imagen a Data URL y mostrar preview
imagen_input.addEventListener('change', function() {
  const archivo = imagen_input.files[0];
  
  if (archivo) {
    const reader = new FileReader();
    
    reader.addEventListener('load', function(evento) {
      // evento.target.result es un Data URL
      const dataUrl = evento.target.result;
      
      // Mostrar la imagen
      preview.src = dataUrl;
    });
    
    // Leer como Data URL
    reader.readAsDataURL(archivo);
  }
});

// Data URL tiene formato: data:image/jpeg;base64,/9j/4AAQSkZJRg...

// Enviar archivo como Data URL al servidor
const form = document.getElementById('formulario');

form.addEventListener('submit', function(evento) {
  evento.preventDefault();
  
  const archivo = imagen_input.files[0];
  const reader = new FileReader();
  
  reader.addEventListener('load', function() {
    const dataUrl = reader.result;
    
    // Enviar Data URL al servidor
    fetch('/guardar-imagen', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ imagen: dataUrl })
    });
  });
  
  reader.readAsDataURL(archivo);
});

// Guardar como descarga (download)
const descargar = document.getElementById('descargar');

descargar.addEventListener('click', function() {
  const archivo = imagen_input.files[0];
  const reader = new FileReader();
  
  reader.addEventListener('load', function() {
    const enlace = document.createElement('a');
    enlace.href = reader.result;
    enlace.download = archivo.name;
    enlace.click();
  });
  
  reader.readAsDataURL(archivo);
});
