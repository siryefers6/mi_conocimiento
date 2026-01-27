/**
 * Objetivo: comparar igualdad estricta
 * Referencia: ===
 * Tipo: operador
 * Nivel: básico
 */

// Mismo tipo y valor
console.log(5 === 5);
console.log("hola" === "hola");
console.log(true === true);

// Diferente valor
console.log(5 === 10);
console.log("hola" === "mundo");

// Tipos diferentes (siempre false con ===)
console.log(5 === "5");  // false
console.log(true === 1); // false
console.log(false === 0); // false
console.log(null === undefined); // false

// Variables con === es más seguro
const numero = 20;
const texto = "20";
console.log(numero === texto);  // false
console.log(numero === 20);     // true

// En condicionales
const edad = "25";
if (edad === 25) {
    console.log("Tiene 25 años");
} else if (edad === "25") {
    console.log("Es el string 25");
}

// Comparaciones con null/undefined
console.log(null === null);
console.log(undefined === undefined);
console.log(null === undefined); // false

// Arrays y objetos (sigue siendo por referencia)
console.log([1] == [1]); // false

/*
output
true
true
true
false
false
false
false
false
false
20
false
true
Es el string 25
true
true
false
false
*/
