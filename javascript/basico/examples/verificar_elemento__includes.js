/**
 * Objetivo: verificar si un array contiene un elemento
 * Referencia: includes()
 * Tipo: método
 * Nivel: intermedio
 */

// Includes básico
const numeros = [1, 2, 3, 4, 5];
console.log(numeros.includes(3));
console.log(numeros.includes(10));

// Includes con strings
const frutas = ["manzana", "banana", "cereza"];
console.log(frutas.includes("banana"));
console.log(frutas.includes("pera"));

// Includes con position (desde qué índice buscar)
const items = [1, 2, 3, 2, 4, 2, 5];
console.log(items.includes(2));
console.log(items.includes(2, 3));

// Includes en condicional
const colores = ["rojo", "verde", "azul"];

if (colores.includes("verde")) {
    console.log("Verde está en la lista");
}

// Includes con booleanos
const valores = [true, false, null, undefined];
console.log(valores.includes(true));
console.log(valores.includes(false));
console.log(valores.includes(null));

// Includes case-sensitive
const palabras = ["Hola", "Mundo"];
console.log(palabras.includes("Hola"));
console.log(palabras.includes("hola"));

/*
output
true
false
true
false
true
true
Verde está en la lista
true
true
true
true
false
*/
