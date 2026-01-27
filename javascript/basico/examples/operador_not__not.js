/**
 * Objetivo: usar operador lógico NOT
 * Referencia: !
 * Tipo: operador
 * Nivel: básico
 */

// NOT básico
console.log(!true);
console.log(!false);

// NOT con comparación
const esMayor = 20 > 18;
console.log(!esMayor);

// NOT con variable booleana
const activo = true;
if (!activo) {
    console.log("No está activo");
} else {
    console.log("Está activo");
}

// NOT para invertir condición
const tieneAcceso = false;

if (!tieneAcceso) {
    console.log("Acceso denegado");
}

// NOT con expresiones
const numero = 0;
if (!numero) {
    console.log("El número es cero o falsy");
}

// Double NOT para convertir a booleano
console.log(!!1);
console.log(!!0);
console.log(!!"texto");
console.log(!!"");

// NOT con objetos
const usuario = null;
if (!usuario) {
    console.log("Usuario no existe");
}

/*
output
false
true
false
Está activo
Acceso denegado
El número es cero o falsy
true
false
true
false
Usuario no existe
*/
