/**
 * Objetivo: usar operador lógico AND
 * Referencia: &&
 * Tipo: operador
 * Nivel: básico
 */

// AND básico
console.log(true && true);
console.log(true && false);
console.log(false && true);
console.log(false && false);

// AND con comparaciones
const edad = 25;
const tieneLicencia = true;

if (edad >= 18 && tieneLicencia) {
    console.log("Puedes conducir");
}

// AND con múltiples condiciones
const temperatura = 25;
const humedad = 60;
const presion = 1013;

if (temperatura > 20 && humedad < 80 && presion > 1000) {
    console.log("Condiciones normales");
}

// AND con variables
const x = 10;
const y = 20;

const resultado1 = (x > 5) && (y > 15);
console.log(resultado1);

const resultado2 = (x > 15) && (y > 15);
console.log(resultado2);

// AND cortocircuito (evalúa hasta encontrar false)
const a = 5;
const b = 10;

console.log(a > 3 && b > 8);
console.log(a < 3 && b > 8);

/*
output
true
false
false
false
Puedes conducir
Condiciones normales
true
false
true
false
*/
