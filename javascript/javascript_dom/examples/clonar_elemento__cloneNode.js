// Clonar elemento

// HTML: <div id="original">
//   <p>Contenido original</p>
// </div>

const original = document.getElementById('original');

// Clonar elemento (copia superficial)
const clon1 = original.cloneNode(false);
console.log(clon1); // <div id="original"></div> (sin hijos)

// Clonar elemento con todo su contenido (copia profunda)
const clon2 = original.cloneNode(true);
console.log(clon2); // <div id="original"><p>Contenido original</p></div>

// Agregar clon a la página
document.body.appendChild(clon2);

// Clonar y modificar
const tarjeta = document.querySelector('.tarjeta');
const nuevaTarjeta = tarjeta.cloneNode(true);

// Cambiar ID para que sea único
nuevaTarjeta.id = 'tarjeta-2';

// Modificar contenido
nuevaTarjeta.querySelector('h2').textContent = 'Nueva tarjeta';

// Agregar a la página
document.body.appendChild(nuevaTarjeta);

// Clonar múltiples elementos
const items = document.querySelectorAll('.item');
const contenedor = document.getElementById('contenedor');

items.forEach(function(item) {
  const clon = item.cloneNode(true);
  
  // Limpiar ID (evitar duplicados)
  if (clon.id) {
    clon.id = clon.id + '-clon';
  }
  
  contenedor.appendChild(clon);
});

// NOTA: cloneNode NO copia escuchadores de eventos
// Después de clonar, necesitas agregar nuevos escuchadores si los necesitas
