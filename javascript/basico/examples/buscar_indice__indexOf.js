/**
 * Objetivo: encontrar el índice de un elemento
 * Referencia: indexOf()
 * Tipo: método
 * Nivel: intermedio
 */

// IndexOf básico
const numeros = [10, 20, 30, 40, 50];
console.log(numeros.indexOf(30));
console.log(numeros.indexOf(20));

// IndexOf no encontrado
console.log(numeros.indexOf(100));

// IndexOf con strings
const frutas = ["manzana", "banana", "cereza", "banana"];
console.log(frutas.indexOf("banana"));

// IndexOf última posición
console.log(frutas.lastIndexOf("banana"));

// IndexOf desde posición
const items = [1, 2, 3, 2, 4, 2, 5];
console.log(items.indexOf(2));
console.log(items.indexOf(2, 3));

// IndexOf en condicional
const colores = ["rojo", "verde", "azul"];

if (colores.indexOf("verde") !== -1) {
    console.log("Verde encontrado en índice", colores.indexOf("verde"));
}

// IndexOf con strings
const palabra = "hola";
console.log(palabra.indexOf("o"));

/*
output
2
1
-1
1
3
1
3
Verde encontrado en índice 1
2
*/
