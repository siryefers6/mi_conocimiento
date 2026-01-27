/**
 * Objetivo: dividir un string en array
 * Referencia: split()
 * Tipo: método
 * Nivel: intermedio
 */

// Split básico
const frase = "hola mundo desde javascript";
const palabras = frase.split(" ");
console.log(palabras);

// Split sin parámetro (whole string)
const texto = "hola";
console.log(texto.split());

// Split con string vacío (cada carácter)
console.log(texto.split(""));

// Split con límite
const frase2 = "manzana-banana-cereza-dátil";
console.log(frase2.split("-", 2));

// Split por carácter especial
const csv = "Juan,25,Madrid";
console.log(csv.split(","));

// Split por saltos de línea
const multilinea = "Primera\nSegunda\nTercera";
console.log(multilinea.split("\n"));

// Split con regex
const texto2 = "uno,dos;tres:cuatro";
console.log(texto2.split(/[,;:]/));

// Split y procesar
const numeros = "1 2 3 4 5";
const arr = numeros.split(" ");
const suma = arr.reduce((a, n) => a + Number(n), 0);
console.log("Suma:", suma);

/*
output
[ 'hola', 'mundo', 'desde', 'javascript' ]
[ 'hola mundo desde javascript' ]
[ 'h', 'o', 'l', 'a' ]
[ 'manzana', 'banana' ]
[ 'Juan', '25', 'Madrid' ]
[ 'Primera', 'Segunda', 'Tercera' ]
[ 'uno', 'dos', 'tres', 'cuatro' ]
Suma: 15
*/
