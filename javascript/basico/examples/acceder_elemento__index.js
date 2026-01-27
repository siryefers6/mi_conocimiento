/**
 * Objetivo: acceder elementos de un array por índice
 * Referencia: array[i]
 * Tipo: operador
 * Nivel: básico
 */

const frutas = ["manzana", "banana", "cereza", "dátil"];

// Acceso por índice
console.log(frutas[0]);
console.log(frutas[1]);
console.log(frutas[3]);

// Acceso con variable
const indice = 2;
console.log(frutas[indice]);

// Índices negativos no funcionan en JavaScript
console.log(frutas[-1]); // undefined

// Última elemento
console.log(frutas[frutas.length - 1]);

// Reasignar elemento
frutas[1] = "naranja";
console.log(frutas[1]);

// Acceso a array anidado
const matriz = [[1, 2], [3, 4], [5, 6]];
console.log(matriz[0][1]);
console.log(matriz[2][0]);

/*
output
manzana
banana
cereza
dátil
cereza
undefined
dátil
naranja
2
5
*/
