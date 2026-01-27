// Reemplazar elemento

// HTML: <div id="contenedor">
//   <p id="viejo">Texto viejo</p>
// </div>

const contenedor = document.getElementById('contenedor');
const viejo = document.getElementById('viejo');

// Crear nuevo elemento
const nuevo = document.createElement('p');
nuevo.textContent = 'Texto nuevo';
nuevo.className = 'importante';

// Reemplazar viejo por nuevo
contenedor.replaceChild(nuevo, viejo);

// Resultado: <div id="contenedor">
//   <p class="importante">Texto nuevo</p>
// </div>

// Ejemplo: reemplazar con contenido HTML
const item = document.getElementById('item-1');
const itemActualizado = document.createElement('li');
itemActualizado.innerHTML = '<strong>Actualizado</strong>';

item.parentElement.replaceChild(itemActualizado, item);

// Reemplazar múltiples elementos
const lista = document.getElementById('lista');
const items = lista.querySelectorAll('li');

items.forEach(function(item) {
  const nuevoItem = document.createElement('li');
  nuevoItem.textContent = '[NUEVO] ' + item.textContent;
  item.parentElement.replaceChild(nuevoItem, item);
});
