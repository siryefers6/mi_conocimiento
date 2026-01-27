/**
 * Objetivo: definir y llamar una función
 * Referencia: function
 * Tipo: keyword
 * Nivel: básico
 */

// Función sin parámetros
function saludar() {
    console.log("Hola");
}

saludar();

// Función con parámetros
function sumar(a, b) {
    const resultado = a + b;
    return resultado;
}

console.log(sumar(5, 3));
console.log(sumar(10, 20));

// Función con múltiples parámetros
function describir(nombre, edad, ciudad) {
    return nombre + " tiene " + edad + " años y vive en " + ciudad;
}

console.log(describir("Elena", 28, "Barcelona"));

// Función sin retorno explícito
function imprimir(texto) {
    console.log("Mensaje: " + texto);
}

imprimir("Esto es importante");

/*
output
Hola
8
30
Elena tiene 28 años y vive en Barcelona
Mensaje: Esto es importante
*/
