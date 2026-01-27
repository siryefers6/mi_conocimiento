/**
 * Objetivo: devolver valores desde una función
 * Referencia: return
 * Tipo: keyword
 * Nivel: básico
 */

// Función con return
function obtenerPar(numero) {
    return numero % 2 === 0;
}

console.log(obtenerPar(4));
console.log(obtenerPar(7));

// Return termina la función
function validarEdad(edad) {
    if (edad < 0) {
        return "Edad inválida";
    }
    if (edad < 18) {
        return "Menor de edad";
    }
    return "Mayor de edad";
}

console.log(validarEdad(-5));
console.log(validarEdad(15));
console.log(validarEdad(25));

// Return con objeto
function crearPersona(nombre, edad) {
    return { nombre: nombre, edad: edad };
}

const persona = crearPersona("Marco", 32);
console.log(persona);

// Return con array
function obtenerPares(hasta) {
    const pares = [];
    for (let i = 0; i <= hasta; i += 2) {
        pares.push(i);
    }
    return pares;
}

console.log(obtenerPares(10));

/*
output
true
false
Edad inválida
Menor de edad
Mayor de edad
{ nombre: 'Marco', edad: 32 }
[ 0, 2, 4, 6, 8, 10 ]
*/
