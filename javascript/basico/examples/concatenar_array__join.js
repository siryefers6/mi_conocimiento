/**
 * Objetivo: unir elementos del array en un string
 * Referencia: join()
 * Tipo: método
 * Nivel: intermedio
 */

// Join básico (con coma)
const numeros = [1, 2, 3, 4, 5];
console.log(numeros.join());

// Join con separador
console.log(numeros.join("-"));

// Join con espacio
const palabras = ["hola", "mundo", "desde", "javascript"];
console.log(palabras.join(" "));

// Join con string vacío
const letras = ["h", "o", "l", "a"];
console.log(letras.join(""));

// Join con separador especial
const items = ["item1", "item2", "item3"];
console.log(items.join(" | "));

// Join con array vacío
const vacio = [];
console.log(vacio.join(","));

// Join con un elemento
const unico = ["solo"];
console.log(unico.join(","));

// Join para crear HTML
const opciones = ["rojo", "verde", "azul"];
const html = "<ul><li>" + opciones.join("</li><li>") + "</li></ul>";
console.log(html);

// Join con saltos de línea
const parrafos = ["Primera linea", "Segunda linea", "Tercera linea"];
console.log(parrafos.join("\n"));

/*
output
1,2,3,4,5
1-2-3-4-5
hola mundo desde javascript
hola
item1 | item2 | item3

solo
<ul><li>rojo</li><li>verde</li><li>azul</li></ul>
Primera linea
Segunda linea
Tercera linea
*/
