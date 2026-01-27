/**
 * Objetivo: declarar una variable con alcance de bloque
 * Referencia: let
 * Tipo: keyword
 * Nivel: básico
 */

// Declarar una variable
let edad = 25;
console.log(edad);

// Modificar su valor
edad = 26;
console.log(edad);

// Declarar múltiples variables
let nombre = "Ana", ciudad = "Madrid";
console.log(nombre, ciudad);

// let tiene alcance de bloque
if (true) {
    let x = 10;
    console.log(x);
}
// console.log(x); // Error: x no está definida aquí

/*
output
25
26
Ana Madrid
10
*/
