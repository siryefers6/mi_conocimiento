/**
 * Objetivo: convertir valores a número
 * Referencia: Number()
 * Tipo: función
 * Nivel: básico
 */

// Convertir string a número
const texto = "123";
const numero = Number(texto);
console.log(numero);
console.log(typeof numero);

// Convertir string con decimales
const decimal = Number("45.67");
console.log(decimal);

// Convertir booleano
console.log(Number(true));
console.log(Number(false));

// Convertir null y undefined
console.log(Number(null));
console.log(Number(undefined));

// String inválido devuelve NaN
console.log(Number("abc"));

// Convertir array
console.log(Number([42]));
console.log(Number([1, 2, 3]));

// Usar con unary plus
const texto2 = "99";
const resultado = +texto2;
console.log(resultado);
console.log(typeof resultado);

// Multiplicar por 1 también funciona
const texto3 = "77";
console.log(texto3 * 1);

/*
output
123
number
45.67
1
0
0
NaN
42
NaN
99
number
77
*/
