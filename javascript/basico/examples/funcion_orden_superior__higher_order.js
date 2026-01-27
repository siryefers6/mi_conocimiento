/**
 * Objetivo: función que recibe otra función como argumento
 * Referencia: function(fn)
 * Tipo: patrón
 * Nivel: intermedio
 */

// Función de orden superior básica
function aplicarOperacion(a, b, operacion) {
    return operacion(a, b);
}

function suma(x, y) {
    return x + y;
}

function resta(x, y) {
    return x - y;
}

console.log(aplicarOperacion(10, 5, suma));
console.log(aplicarOperacion(10, 5, resta));

// Función de orden superior con arrow function
const multiplicar = (x, y) => x * y;
console.log(aplicarOperacion(10, 5, multiplicar));

// Función que retorna una función
function crearMultiplicador(factor) {
    return (numero) => numero * factor;
}

const duplicar = crearMultiplicador(2);
const triplicar = crearMultiplicador(3);

console.log(duplicar(5));
console.log(triplicar(5));

// Decorador de función
function decorar(fn) {
    return function(...args) {
        console.log("Llamando función:", fn.name);
        return fn(...args);
    };
}

function saludar(nombre) {
    return "Hola " + nombre;
}

const saludarDecorado = decorar(saludar);
console.log(saludarDecorado("Juan"));

// Map y filter como funciones de orden superior
const numeros = [1, 2, 3, 4, 5];
const procesados = numeros
    .map(n => n * 2)
    .filter(n => n > 5);
console.log(procesados);

/*
output
15
5
50
10
15
Llamando función: saludar
Hola Juan
[ 6, 8, 10 ]
*/
