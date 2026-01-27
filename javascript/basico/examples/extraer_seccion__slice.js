/**
 * Objetivo: extraer una porción del array
 * Referencia: slice()
 * Tipo: método
 * Nivel: intermedio
 */

// Slice básico
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const subarray1 = numeros.slice(2, 5);
console.log(subarray1);

// Slice sin fin
const subarray2 = numeros.slice(5);
console.log(subarray2);

// Slice desde el inicio
const subarray3 = numeros.slice(0, 3);
console.log(subarray3);

// Slice negativo
const subarray4 = numeros.slice(-3);
console.log(subarray4);

// Slice con ambos negativos
const subarray5 = numeros.slice(-6, -2);
console.log(subarray5);

// Slice copia el array
const original = [1, 2, 3];
const copia = original.slice();
copia[0] = 99;
console.log("Original:", original);
console.log("Copia:", copia);

// Slice con strings
const palabra = "hola";
const parte = palabra.slice(1, 3);
console.log(parte);

// Slice últimos elementos
const items = ["a", "b", "c", "d", "e"];
console.log(items.slice(-2));

/*
output
[ 3, 4, 5 ]
[ 6, 7, 8, 9, 10 ]
[ 1, 2, 3 ]
[ 8, 9, 10 ]
[ 5, 6, 7, 8 ]
Original: [ 1, 2, 3 ]
Copia: [ 99, 2, 3 ]
ol
[ 'd', 'e' ]
*/
