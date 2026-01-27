// Obtener elemento padre

// HTML: <div id="contenedor">
//   <p id="parrafo">Contenido</p>
// </div>

const parrafo = document.getElementById('parrafo');

// Obtener padre directo
const padre = parrafo.parentElement;
console.log(padre.id); // "contenedor"

// Acceder a propiedades del padre
console.log(padre.className);
console.log(padre.tagName); // "DIV"

// Padre del padre
const abuelo = padre.parentElement;
console.log(abuelo); // <body> u otro elemento

// Verificar si tiene padre
if (parrafo.parentElement) {
  console.log('El elemento tiene padre');
}

// Modificar padre desde hijo
parrafo.parentElement.style.backgroundColor = 'blue';

// Remover elemento desde el padre obtenido
parrafo.parentElement.removeChild(parrafo);

// parentElement vs parentNode
// parentElement: devuelve elemento o null
// parentNode: devuelve nodo o null
const p = document.getElementById('parrafo');
console.log(p.parentElement === p.parentNode); // usualmente true
