// Seleccionar elementos por clase CSS

// HTML:
// <div class="tarjeta">Tarjeta 1</div>
// <div class="tarjeta">Tarjeta 2</div>
// <div class="tarjeta">Tarjeta 3</div>

// Obtener todos los elementos con clase "tarjeta"
const tarjetas = document.getElementsByClassName('tarjeta');

// getElementsByClassName devuelve HTMLCollection (similar a array)
console.log(tarjetas);            // HTMLCollection(3) [div.tarjeta, div.tarjeta, div.tarjeta]
console.log(tarjetas.length);     // 3

// Recorrer los elementos
for (let i = 0; i < tarjetas.length; i++) {
  console.log(tarjetas[i].textContent);
}

// Acceder a elemento específico
console.log(tarjetas[0].textContent); // "Tarjeta 1"
