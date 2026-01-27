/**
 * Objetivo: desempacar elementos de un array u objeto
 * Referencia: ...
 * Tipo: operador
 * Nivel: intermedio
 */

// Spread en arrays
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combinado = [...arr1, ...arr2];
console.log(combinado);

// Spread para copiar array
const original = [1, 2, 3];
const copia = [...original];
console.log(copia);

// Spread con elementos adicionales
const numeros = [2, 3];
const conMas = [1, ...numeros, 4, 5];
console.log(conMas);

// Spread en objetos
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const merged = { ...obj1, ...obj2 };
console.log(merged);

// Spread para copiar objeto
const persona = { nombre: "Juan", edad: 25 };
const personaCopia = { ...persona };
personaCopia.edad = 26;
console.log(persona);
console.log(personaCopia);

// Spread en función
function sumar(a, b, c) {
    return a + b + c;
}

const valores = [1, 2, 3];
console.log(sumar(...valores));

// Spread con rest parameters
const [primero, ...resto] = [1, 2, 3, 4, 5];
console.log("Primero:", primero);
console.log("Resto:", resto);

/*
output
[ 1, 2, 3, 4, 5, 6 ]
[ 1, 2, 3 ]
[ 1, 2, 3, 4, 5 ]
{ a: 1, b: 2, c: 3, d: 4 }
{ nombre: 'Juan', edad: 25 }
{ nombre: 'Juan', edad: 26 }
6
Primero: 1
Resto: [ 2, 3, 4, 5 ]
*/
