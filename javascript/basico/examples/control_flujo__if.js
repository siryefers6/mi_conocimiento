/**
 * Objetivo: ejecutar código condicionalmente
 * Referencia: if
 * Tipo: keyword
 * Nivel: básico
 */

// Condicional simple
const edad = 18;

if (edad >= 18) {
    console.log("Eres mayor de edad");
}

// Condicional con resultado
const temperatura = 25;

if (temperatura > 30) {
    console.log("Hace calor");
}

if (temperatura <= 20) {
    console.log("Hace frío");
}

if (temperatura >= 20 && temperatura <= 30) {
    console.log("Temperatura moderada");
}

/*
output
Eres mayor de edad
Temperatura moderada
*/
