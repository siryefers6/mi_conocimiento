// Seleccionar elementos por etiqueta HTML

// HTML:
// <p>Párrafo 1</p>
// <p>Párrafo 2</p>
// <span>Texto</span>
// <p>Párrafo 3</p>

// Obtener todos los párrafos
const parrafos = document.getElementsByTagName('p');

// getElementsByTagName devuelve HTMLCollection
console.log(parrafos);        // HTMLCollection(3) [p, p, p]
console.log(parrafos.length); // 3

// Recorrer elementos
for (let i = 0; i < parrafos.length; i++) {
  console.log(parrafos[i].textContent);
}

// Obtener todos los spans
const spans = document.getElementsByTagName('span');
console.log(spans.length); // 1
