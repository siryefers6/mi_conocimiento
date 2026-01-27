/**
 * Objetivo: usar sintaxis concisa de funciones
 * Referencia: =>
 * Tipo: operador
 * Nivel: básico
 */

// Arrow function simple
const saludar = () => {
    console.log("Hola desde arrow function");
};

saludar();

// Arrow function con parámetros
const sumar = (a, b) => {
    return a + b;
};

console.log(sumar(7, 3));

// Arrow function compacta (sin llaves)
const multiplicar = (a, b) => a * b;

console.log(multiplicar(6, 4));

// Arrow function con un parámetro (sin paréntesis)
const doble = n => n * 2;

console.log(doble(5));

// Arrow function con array
const numeros = [1, 2, 3, 4, 5];

numeros.forEach(n => console.log(n));

/*
output
Hola desde arrow function
10
24
10
1
2
3
4
5
*/
