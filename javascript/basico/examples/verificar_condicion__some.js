/**
 * Objetivo: verificar si al menos un elemento cumple condición
 * Referencia: some()
 * Tipo: método
 * Nivel: intermedio
 */

// Some básico
const numeros = [1, 2, 3, 4, 5];
const hayPar = numeros.some(n => n % 2 === 0);
console.log("Hay pares:", hayPar);

const hayMayora10 = numeros.some(n => n > 10);
console.log("Hay mayores a 10:", hayMayora10);

// Some con strings
const palabras = ["sol", "luna", "mar"];
const conM = palabras.some(p => p.includes("m"));
console.log("Hay palabra con 'm':", conM);

// Some con objetos
const usuarios = [
    { nombre: "Juan", activo: false },
    { nombre: "Elena", activo: false },
    { nombre: "Marco", activo: true }
];

const hayActivo = usuarios.some(u => u.activo);
console.log("Hay usuario activo:", hayActivo);

// Some en condicional
const edades = [10, 15, 12, 8];
if (edades.some(e => e >= 18)) {
    console.log("Hay al menos un mayor de edad");
} else {
    console.log("No hay menores de edad");
}

// Some vs find
const items = [1, 2, 3, 4, 5];
const existePar = items.some(i => i % 2 === 0);
const primerPar = items.find(i => i % 2 === 0);

console.log("Existe par:", existePar);
console.log("Primer par:", primerPar);

// Some no modifica el array
const original = [1, 2, 3];
const resultado = original.some(n => n > 2);
console.log("Array original:", original);
console.log("Resultado some:", resultado);

/*
output
Hay pares: true
Hay mayores a 10: false
Hay palabra con 'm': true
Hay usuario activo: true
No hay menores de edad
Existe par: true
Primer par: 2
Array original: [ 1, 2, 3 ]
Resultado some: true
*/
