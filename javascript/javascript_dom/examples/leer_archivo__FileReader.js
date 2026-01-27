// Leer contenido de archivo (FileReader)

// HTML: <input type="file" id="archivo">

const archivo_input = document.getElementById('archivo');

// Crear FileReader para leer el archivo
archivo_input.addEventListener('change', function() {
  const archivo = archivo_input.files[0];
  
  if (archivo) {
    const reader = new FileReader();
    
    // Escuchar cuando el archivo se cargue
    reader.addEventListener('load', function(evento) {
      console.log('Archivo cargado');
      console.log('Contenido:', evento.target.result);
    });
    
    // Escuchar errores
    reader.addEventListener('error', function() {
      console.error('Error al leer el archivo');
    });
    
    // Iniciar lectura como texto
    reader.readAsText(archivo);
  }
});

// FileReader ofrece varios métodos:
// - readAsText(archivo) - lee como texto
// - readAsDataURL(archivo) - convierte a Data URL
// - readAsArrayBuffer(archivo) - lee como buffer
// - readAsBinaryString(archivo) - lee como binario

// Propiedades útiles:
// - reader.result - contenido del archivo
// - reader.readyState - estado (0=no iniciado, 1=cargando, 2=completado)
// - reader.error - información del error

// Ejemplo: mostrar progreso de carga
archivo_input.addEventListener('change', function() {
  const archivo = archivo_input.files[0];
  const reader = new FileReader();
  
  reader.addEventListener('progress', function(evento) {
    if (evento.lengthComputable) {
      const porcentaje = (evento.loaded / evento.total) * 100;
      console.log('Progreso:', porcentaje.toFixed(2) + '%');
    }
  });
  
  reader.addEventListener('load', function() {
    console.log('Carga completada');
  });
  
  reader.readAsText(archivo);
});
