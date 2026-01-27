// Acceder a archivos subidos

// HTML: <input type="file" id="cargador">

const cargador = document.getElementById('cargador');

// Escuchar cambio en el input
cargador.addEventListener('change', function() {
  // Obtener lista de archivos
  const archivos = cargador.files;
  
  console.log('Cantidad de archivos:', archivos.length);
  
  // Acceder a propiedades del primer archivo
  if (archivos.length > 0) {
    const archivo = archivos[0];
    
    console.log('Nombre:', archivo.name);
    console.log('Tamaño:', archivo.size, 'bytes');
    console.log('Tipo:', archivo.type);
    console.log('Fecha:', archivo.lastModified);
  }
});

// Iterar sobre múltiples archivos
// HTML: <input type="file" id="archivos" multiple>

const archivos_input = document.getElementById('archivos');

archivos_input.addEventListener('change', function() {
  const archivos = archivos_input.files;
  
  // Iterar cada archivo
  for (let i = 0; i < archivos.length; i++) {
    const archivo = archivos[i];
    console.log(`Archivo ${i + 1}: ${archivo.name} (${archivo.size} bytes)`);
  }
});

// Validar tamaño de archivo
cargador.addEventListener('change', function() {
  const archivo = cargador.files[0];
  const maxSize = 5 * 1024 * 1024; // 5 MB
  
  if (archivo.size > maxSize) {
    alert('El archivo es muy grande');
    cargador.value = ''; // Limpiar input
  }
});

// Validar tipo de archivo
cargador.addEventListener('change', function() {
  const archivo = cargador.files[0];
  
  if (!archivo.type.startsWith('image/')) {
    alert('Solo se permiten imágenes');
    cargador.value = '';
  }
});
