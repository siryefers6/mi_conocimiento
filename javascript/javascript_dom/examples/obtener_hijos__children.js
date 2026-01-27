// Obtener todos los elementos hijos

// HTML: <div id="contenedor">
//   <p>Párrafo 1</p>
//   <span>Texto</span>
//   <p>Párrafo 2</p>
// </div>

const contenedor = document.getElementById('contenedor');

// Obtener colección de hijos (HTMLCollection)
const hijos = contenedor.children;

console.log(hijos);           // HTMLCollection(3) [p, span, p]
console.log(hijos.length);    // 3

// Acceder a hijo específico por índice
console.log(hijos[0].textContent); // "Párrafo 1"
console.log(hijos[1].textContent); // "Texto"
console.log(hijos[2].textContent); // "Párrafo 2"

// Iterar sobre los hijos
for (let i = 0; i < hijos.length; i++) {
  console.log(hijos[i].tagName); // "P", "SPAN", "P"
}

// También se puede usar forEach (moderno)
Array.from(hijos).forEach(function(hijo) {
  console.log(hijo.textContent);
});

// Modificar todos los hijos
for (let i = 0; i < hijos.length; i++) {
  hijos[i].style.padding = '10px';
}

// children es HTMLCollection (vivo, se actualiza)
// childNodes es NodeList (incluye nodos de texto)
