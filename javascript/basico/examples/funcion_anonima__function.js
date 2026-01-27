/**
 * Objetivo: usar funciones sin nombre (anónimas)
 * Referencia: function()
 * Tipo: keyword
 * Nivel: básico
 */

// Función anónima asignada a variable
const multiplicar = function(a, b) {
    return a * b;
};

console.log(multiplicar(4, 5));

// Función anónima como argumento
const numeros = [1, 2, 3, 4, 5];

numeros.forEach(function(num) {
    console.log(num * 2);
});

// Función anónima en variable con lógica
const dividir = function(a, b) {
    if (b === 0) {
        return "No se puede dividir entre cero";
    }
    return a / b;
};

console.log(dividir(10, 2));
console.log(dividir(10, 0));

/*
output
20
2
4
6
8
10
5
No se puede dividir entre cero
*/
