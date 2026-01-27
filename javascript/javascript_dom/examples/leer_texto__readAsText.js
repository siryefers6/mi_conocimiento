// Leer archivo como texto

// HTML: <input type="file" id="archivo">
//       <div id="contenido"></div>

const archivo_input = document.getElementById('archivo');
const contenido = document.getElementById('contenido');

// Leer archivo de texto
archivo_input.addEventListener('change', function() {
  const archivo = archivo_input.files[0];
  
  if (archivo) {
    const reader = new FileReader();
    
    reader.addEventListener('load', function(evento) {
      // evento.target.result contiene el contenido de texto
      const texto = evento.target.result;
      
      // Mostrar el contenido en la página
      contenido.textContent = texto;
    });
    
    // Iniciar lectura como texto
    reader.readAsText(archivo);
  }
});

// Leer archivos CSV
archivo_input.addEventListener('change', function() {
  const archivo = archivo_input.files[0];
  const reader = new FileReader();
  
  reader.addEventListener('load', function(evento) {
    const csv = evento.target.result;
    
    // Procesar CSV
    const filas = csv.split('\n');
    const datos = filas.map(fila => fila.split(','));
    
    console.log('Datos CSV:', datos);
  });
  
  reader.readAsText(archivo, 'UTF-8');
});

// Leer con encoding específico
archivo_input.addEventListener('change', function() {
  const archivo = archivo_input.files[0];
  const reader = new FileReader();
  
  reader.addEventListener('load', function(evento) {
    const contenido = evento.target.result;
    console.log('Contenido:', contenido);
  });
  
  // UTF-8 es el encoding por defecto
  reader.readAsText(archivo, 'UTF-8');
});

// Procesar línea por línea
archivo_input.addEventListener('change', function() {
  const archivo = archivo_input.files[0];
  const reader = new FileReader();
  
  reader.addEventListener('load', function(evento) {
    const lineas = evento.target.result.split('\n');
    
    lineas.forEach(function(linea, indice) {
      console.log(`Línea ${indice + 1}: ${linea}`);
    });
  });
  
  reader.readAsText(archivo);
});
