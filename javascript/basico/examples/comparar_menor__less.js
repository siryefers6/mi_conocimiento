/**
 * Objetivo: comparar si un valor es menor
 * Referencia: <
 * Tipo: operador
 * Nivel: básico
 */

// Comparación numérica
console.log(5 < 10);
console.log(10 < 5);
console.log(5 < 5);

// Comparación con strings
console.log("a" < "b");
console.log("abc" < "abd");
console.log("a" < "A");

// Con variables
const edad = 18;
const edadMinima = 21;
console.log(edad < edadMinima);

// Menor o igual
console.log(5 <= 5);
console.log(5 <= 10);
console.log(10 <= 5);

// En condicionales
const temperatura = 15;
if (temperatura < 20) {
    console.log("Hace frío");
}

// Comparaciones múltiples
const numero = 7;
if (numero > 5 && numero < 10) {
    console.log("El número está entre 5 y 10");
}

// Convertir tipos
console.log("5" < 10);  // true
console.log("10" < 5);  // false

/*
output
true
false
false
true
true
false
true
false
false
true
Hace frío
El número está entre 5 y 10
true
false
*/
