/**
 * Objetivo: eliminar el último elemento de un array
 * Referencia: pop()
 * Tipo: método
 * Nivel: básico
 */

// Pop básico
const numeros = [1, 2, 3, 4, 5];
console.log(numeros);

const eliminado = numeros.pop();
console.log("Eliminado:", eliminado);
console.log("Array:", numeros);

// Pop múltiples veces
const colores = ["rojo", "verde", "azul", "amarillo"];

colores.pop();
console.log("Después de pop 1:", colores);

colores.pop();
console.log("Después de pop 2:", colores);

// Pop en array vacío
const vacio = [];
const resultado = vacio.pop();
console.log("Pop en vacío:", resultado);
console.log("Array:", vacio);

// Pop con strings
const palabras = ["hola", "mundo"];
const palabra = palabras.pop();
console.log("Palabra eliminada:", palabra);
console.log("Palabras:", palabras);

/*
output
[ 1, 2, 3, 4, 5 ]
Eliminado: 5
Array: [ 1, 2, 3, 4 ]
Después de pop 1: [ 'rojo', 'verde', 'azul' ]
Después de pop 2: [ 'rojo', 'verde' ]
Pop en vacío: undefined
Array: []
Palabra eliminada: mundo
Palabras: [ 'hola' ]
*/
