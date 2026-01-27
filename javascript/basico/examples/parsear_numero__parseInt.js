/**
 * Objetivo: extraer número entero de un string
 * Referencia: parseInt()
 * Tipo: función
 * Nivel: básico
 */

// Parsear entero simple
console.log(parseInt("42"));

// Parsear número con decimales (ignora decimales)
console.log(parseInt("45.67"));

// Parsear string con números al inicio
console.log(parseInt("123abc"));

// Parsear número negativo
console.log(parseInt("-50"));

// Parsear con base numérica
console.log(parseInt("1010", 2));  // Binario
console.log(parseInt("FF", 16));    // Hexadecimal
console.log(parseInt("17", 8));     // Octal

// Parsear con espacios
console.log(parseInt("  78  "));

// Parsear inválido
console.log(parseInt("abc"));

// Parsear cero
console.log(parseInt("0123"));

// Diferencia entre parseInt y Number
console.log(parseInt("45.67"));
console.log(Number("45.67"));

/*
output
42
45
123
-50
10
255
15
78
NaN
123
45
45.67
*/
