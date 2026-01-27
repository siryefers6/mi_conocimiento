/**
 * Objetivo: eliminar, reemplazar o insertar elementos en cualquier posición
 * Referencia: splice()
 * Tipo: método
 * Nivel: básico
 */

// Splice: eliminar elementos
const numeros = [1, 2, 3, 4, 5, 6];
const eliminados = numeros.splice(2, 2);
console.log("Eliminados:", eliminados);
console.log("Array:", numeros);

// Splice: insertar sin eliminar
const frutas = ["manzana", "cereza"];
frutas.splice(1, 0, "banana");
console.log(frutas);

// Splice: reemplazar
const letras = ["a", "b", "c", "d", "e"];
letras.splice(1, 2, "x", "y", "z");
console.log(letras);

// Splice con índice negativo
const items = [10, 20, 30, 40, 50];
items.splice(-2, 1);
console.log(items);

// Splice retorna array de eliminados
const datos = ["a", "b", "c", "d"];
const resultado = datos.splice(0, 1);
console.log("Resultado:", resultado);
console.log("Array:", datos);

/*
output
Eliminados: [ 3, 4 ]
Array: [ 1, 2, 5, 6 ]
[ 'manzana', 'banana', 'cereza' ]
[ 'a', 'x', 'y', 'z', 'e' ]
[ 10, 20, 30, 50 ]
Resultado: [ 'a' ]
Array: [ 'b', 'c', 'd' ]
*/
