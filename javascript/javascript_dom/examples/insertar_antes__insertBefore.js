// Insertar elemento antes de otro elemento

// HTML: <div id="contenedor">
//   <p>Elemento 1</p>
//   <p>Elemento 3</p>
// </div>

const contenedor = document.getElementById('contenedor');
const elemento3 = contenedor.children[1]; // Elemento 3

// Crear nuevo elemento
const elemento2 = document.createElement('p');
elemento2.textContent = 'Elemento 2';

// Insertar antes del elemento 3
contenedor.insertBefore(elemento2, elemento3);

// Resultado: <div id="contenedor">
//   <p>Elemento 1</p>
//   <p>Elemento 2</p>
//   <p>Elemento 3</p>
// </div>

// Insertar al principio
const lista = document.getElementById('lista');
const primerItem = lista.firstElementChild;

const nuevoItem = document.createElement('li');
nuevoItem.textContent = 'Primero';

lista.insertBefore(nuevoItem, primerItem);

// Insertar como primer elemento si está vacío
const contenedorVacio = document.getElementById('contenedor-vacio');
const primer = document.createElement('p');
primer.textContent = 'Primer elemento';

contenedorVacio.insertBefore(primer, contenedorVacio.firstElementChild);
