// Verificar si elemento contiene otro

// HTML: <div id="padre">
//   <p id="hijo">Texto</p>
// </div>

const padre = document.getElementById('padre');
const hijo = document.getElementById('hijo');
const otroElemento = document.getElementById('otro');

// Verificar si padre contiene hijo
console.log(padre.contains(hijo)); // true

// Verificar si padre contiene otro elemento
console.log(padre.contains(otroElemento)); // false (si no está dentro)

// Un elemento siempre contiene a sí mismo
console.log(padre.contains(padre)); // true

// Usar en condicionales
if (padre.contains(hijo)) {
  console.log('El hijo está dentro del padre');
}

// Verificar si un elemento está en un contenedor específico
const contenedor = document.getElementById('contenedor');
const elemento = event.target;

if (contenedor.contains(elemento)) {
  console.log('El click fue dentro del contenedor');
} else {
  console.log('El click fue fuera del contenedor');
}

// Detectar clics fuera de un modal
const modal = document.getElementById('modal');

document.addEventListener('click', function(evento) {
  if (!modal.contains(evento.target)) {
    console.log('Clic fuera del modal');
    // Cerrar modal
    modal.remove();
  }
});

// Verificar jerarquía de elementos
const elemento1 = document.getElementById('elemento1');
const elemento2 = document.getElementById('elemento2');

if (elemento1.contains(elemento2)) {
  console.log('elemento2 está dentro de elemento1');
} else if (elemento2.contains(elemento1)) {
  console.log('elemento1 está dentro de elemento2');
} else {
  console.log('No tienen relación de contenencia');
}
