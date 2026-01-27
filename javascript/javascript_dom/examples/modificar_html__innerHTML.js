// Modificar contenido HTML

// HTML: <div id="contenedor"></div>

const contenedor = document.getElementById('contenedor');

// Establecer HTML
contenedor.innerHTML = '<p>Párrafo con <strong>HTML</strong></p>';

// Leer HTML
console.log(contenedor.innerHTML);
// "<p>Párrafo con <strong>HTML</strong></p>"

// Agregar más HTML
contenedor.innerHTML += '<p>Nuevo párrafo</p>';

// innerHTML interpreta etiquetas HTML
contenedor.innerHTML = '<h1>Título</h1><p>Contenido</p>';

// Cuidado: innerHTML puede ser peligroso con datos no verificados
// No usar con datos de usuarios sin validación
