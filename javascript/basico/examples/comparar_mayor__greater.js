/**
 * Objetivo: comparar si un valor es mayor
 * Referencia: >
 * Tipo: operador
 * Nivel: básico
 */

// Comparación numérica
console.log(10 > 5);
console.log(5 > 10);
console.log(5 > 5);

// Comparación con strings
console.log("b" > "a");
console.log("abc" > "abb");

// Con variables
const puntuacion = 95;
const puntuacionMinima = 80;
console.log(puntuacion > puntuacionMinima);

// Mayor o igual
console.log(5 >= 5);
console.log(10 >= 5);
console.log(5 >= 10);

// En condicionales
const ingresos = 50000;
if (ingresos > 30000) {
    console.log("Ingresos altos");
}

// Comparaciones múltiples
const precio = 150;
if (precio > 100 && precio < 200) {
    console.log("Precio en rango");
}

// Convertir tipos
console.log(10 > "5");  // true
console.log(5 > "10");  // false

// Con booleanos
console.log(true > false);  // true
console.log(1 > 0);         // true

/*
output
true
false
false
true
true
true
true
true
false
Ingresos altos
Precio en rango
true
false
true
true
*/
