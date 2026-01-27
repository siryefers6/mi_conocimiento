/**
 * Objetivo: trabajar con valores booleanos
 * Referencia: true / false
 * Tipo: literal
 * Nivel: básico
 */

// Booleano true
const esActivo = true;
console.log(esActivo);
console.log(typeof esActivo);

// Booleano false
const esAzul = false;
console.log(esAzul);

// Booleano de comparación
const resultado1 = 10 > 5;
console.log(resultado1);

// Booleano con igualdad
const resultado2 = "texto" === "texto";
console.log(resultado2);

// Booleano con constructor (no recomendado)
const bool1 = Boolean(1);
const bool2 = Boolean(0);
const bool3 = Boolean("");
const bool4 = Boolean("texto");

console.log(bool1, bool2, bool3, bool4);

// Valores falsy
console.log(Boolean(0));
console.log(Boolean(""));
console.log(Boolean(null));
console.log(Boolean(undefined));
console.log(Boolean(NaN));

// Valores truthy
console.log(Boolean(1));
console.log(Boolean("texto"));
console.log(Boolean([]));
console.log(Boolean({}));

/*
output
true
boolean
false
true
true
true false false true
false
false
false
false
false
true
true
true
true
*/
