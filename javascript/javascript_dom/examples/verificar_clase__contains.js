// Verificar si elemento tiene clase

// HTML: <div id="caja" class="activo importante">Contenido</div>

const caja = document.getElementById('caja');

// Verificar si contiene una clase
console.log(caja.classList.contains('activo'));     // true
console.log(caja.classList.contains('importante'));  // true
console.log(caja.classList.contains('deshabilitado')); // false

// Usar con condicionales
if (caja.classList.contains('activo')) {
  console.log('La caja está activa');
}

// Combinación con operadores
if (caja.classList.contains('activo') && caja.classList.contains('importante')) {
  console.log('La caja es activa e importante');
}

// Ejemplo práctico: cambiar comportamiento según clase
const elemento = document.getElementById('elemento');

elemento.addEventListener('click', function() {
  if (elemento.classList.contains('seleccionado')) {
    elemento.classList.remove('seleccionado');
  } else {
    elemento.classList.add('seleccionado');
  }
});

// O usando toggle para simplificar
elemento.addEventListener('click', function() {
  elemento.classList.toggle('seleccionado');
});
