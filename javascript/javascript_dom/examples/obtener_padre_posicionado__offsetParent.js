// Obtener padre posicionado (offsetParent)

// HTML: <div id="abuelo" style="position: relative;">
//   <div id="padre" style="position: absolute;">
//     <div id="hijo">Contenido</div>
//   </div>
// </div>

const hijo = document.getElementById('hijo');
const padre = document.getElementById('padre');
const abuelo = document.getElementById('abuelo');

// Obtener el padre posicionado
const padrePos = hijo.offsetParent;
console.log(padrePos === padre); // true (es el elemento posicionado más cercano)

// Si el elemento está hidden (display: none)
// offsetParent devuelve null
const oculto = document.getElementById('oculto');
console.log(oculto.offsetParent); // null

// offsetParent es el elemento posicionado más cercano
// (position: relative, absolute, fixed, sticky)
// Si no hay ninguno, es el body/html

// Obtener la cadena de padres posicionados
function obtenerPadresPos(elemento) {
  const padres = [];
  let actual = elemento.offsetParent;
  
  while (actual) {
    padres.push(actual);
    actual = actual.offsetParent;
  }
  
  return padres;
}

const padres = obtenerPadresPos(hijo);
console.log(padres); // [padre, abuelo, body, html]

// offsetLeft/offsetTop son relativos a offsetParent
console.log(hijo.offsetLeft);   // X relativa a padre
console.log(hijo.offsetTop);    // Y relativa a padre

console.log(padre.offsetLeft);  // X relativa a abuelo
console.log(padre.offsetTop);   // Y relativa a abuelo
