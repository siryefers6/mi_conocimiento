// Insertar elemento al final (appendChild)

// HTML: <div id="contenedor">
//   <p>Elemento 1</p>
// </div>

const contenedor = document.getElementById('contenedor');

// Crear nuevo elemento
const nuevoParrafo = document.createElement('p');
nuevoParrafo.textContent = 'Elemento 2';

// Agregar al final del contenedor
contenedor.appendChild(nuevoParrafo);

// Resultado: <div id="contenedor">
//   <p>Elemento 1</p>
//   <p>Elemento 2</p>
// </div>

// Agregar múltiples elementos
const lista = document.getElementById('lista');
for (let i = 1; i <= 3; i++) {
  const item = document.createElement('li');
  item.textContent = `Elemento ${i}`;
  lista.appendChild(item);
}

// appendChild también sirve para mover elementos
const parrafo1 = document.querySelector('p:first-of-type');
const otroContenedor = document.getElementById('otro-contenedor');

// Mover parrafo1 a otroContenedor
otroContenedor.appendChild(parrafo1);
