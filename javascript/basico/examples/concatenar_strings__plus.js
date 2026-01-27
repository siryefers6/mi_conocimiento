/**
 * Objetivo: unir strings con el operador +
 * Referencia: +
 * Tipo: operador
 * Nivel: básico
 */

// Concatenación básica
const nombre = "Pedro";
const apellido = "Martínez";

const nombreCompleto = nombre + " " + apellido;
console.log(nombreCompleto);

// Concatenar con números
const numero = 42;
const resultado = "El número es " + numero;
console.log(resultado);

// Concatenar múltiples strings
const saludo = "Hola" + ", " + "bienvenido" + " " + "a" + " " + "JavaScript";
console.log(saludo);

// Concatenar y reasignar
let texto = "Hola";
texto = texto + " mundo";
texto = texto + "!";
console.log(texto);

// Concatenar con expresiones
const edad = 30;
const mensaje = "Tengo " + edad + " años";
console.log(mensaje);

// Concatenar booleanos
const activo = true;
console.log("Estado: " + activo);

// Concatenación en bucle
let resultado2 = "";
for (let i = 1; i <= 3; i++) {
    resultado2 = resultado2 + i;
}
console.log(resultado2);

/*
output
Pedro Martínez
El número es 42
Hola, bienvenido a JavaScript
Hola mundo!
Tengo 30 años
Estado: true
123
*/
