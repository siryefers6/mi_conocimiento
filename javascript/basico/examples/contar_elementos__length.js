/**
 * Objetivo: obtener la cantidad de elementos en un array
 * Referencia: length
 * Tipo: propiedad
 * Nivel: básico
 */

// Length básico
const numeros = [1, 2, 3, 4, 5];
console.log(numeros.length);

// Length con strings
const palabra = "hola";
console.log(palabra.length);

// Length con array vacío
const vacio = [];
console.log(vacio.length);

// Usar length en bucle
const frutas = ["manzana", "banana", "cereza"];
for (let i = 0; i < frutas.length; i++) {
    console.log(frutas[i]);
}

// Length para acceder último elemento
const items = [10, 20, 30, 40];
console.log(items[items.length - 1]);

// Reasignar length
const arr = [1, 2, 3, 4, 5];
console.log("Original:", arr.length);
arr.length = 3;
console.log("Después:", arr);

/*
output
5
4
0
manzana
banana
cereza
40
Original: 5
Después: [ 1, 2, 3 ]
*/
