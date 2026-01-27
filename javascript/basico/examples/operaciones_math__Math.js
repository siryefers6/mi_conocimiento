/**
 * Objetivo: usar objeto Math para operaciones matemáticas
 * Referencia: Math
 * Tipo: objeto
 * Nivel: intermedio
 */

// Math.abs
console.log(Math.abs(-10));
console.log(Math.abs(-3.5));

// Math.round
console.log(Math.round(4.4));
console.log(Math.round(4.5));
console.log(Math.round(4.6));

// Math.floor y Math.ceil
console.log(Math.floor(4.9));
console.log(Math.ceil(4.1));

// Math.max y Math.min
console.log(Math.max(10, 5, 8, 20, 3));
console.log(Math.min(10, 5, 8, 20, 3));

// Math.pow
console.log(Math.pow(2, 3));
console.log(Math.pow(5, 2));

// Math.sqrt
console.log(Math.sqrt(16));
console.log(Math.sqrt(25));

// Math.random (0 a 1)
console.log(Math.random());

// Math.random para número entre 1 y 10
const aleatorio = Math.floor(Math.random() * 10) + 1;
console.log("Número aleatorio 1-10:", aleatorio);

// Constantes de Math
console.log("PI:", Math.PI);
console.log("E:", Math.E);

/*
output
10
3.5
4
4
5
4
1
20
3
8
25
4
5
(número aleatorio entre 0 y 1)
Número aleatorio 1-10: (entre 1 y 10)
PI: 3.141592653589793
E: 2.718281828459045
*/
