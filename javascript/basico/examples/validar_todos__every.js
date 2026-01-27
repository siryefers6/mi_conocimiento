/**
 * Objetivo: verificar si todos los elementos cumplen condición
 * Referencia: every()
 * Tipo: método
 * Nivel: intermedio
 */

// Every básico
const numeros = [2, 4, 6, 8, 10];
const todosPares = numeros.every(n => n % 2 === 0);
console.log("Todos pares:", todosPares);

const numerosConImpar = [2, 4, 5, 8, 10];
const todosPares2 = numerosConImpar.every(n => n % 2 === 0);
console.log("Todos pares (con impar):", todosPares2);

// Every con strings
const palabras = ["sol", "mar", "rio"];
const todasCortas = palabras.every(p => p.length <= 3);
console.log("Todas cortas:", todasCortas);

// Every con objetos
const usuarios = [
    { nombre: "Juan", activo: true },
    { nombre: "Elena", activo: true },
    { nombre: "Marco", activo: true }
];

const todosActivos = usuarios.every(u => u.activo);
console.log("Todos activos:", todosActivos);

// Every en validación
const edades = [25, 30, 28, 35];
if (edades.every(e => e >= 18)) {
    console.log("Todos son mayores de edad");
}

// Every vs some
const items = [1, 2, 3, 4, 5];
const todosMayores0 = items.every(i => i > 0);
const algunoMayorque3 = items.some(i => i > 3);

console.log("Todos > 0:", todosMayores0);
console.log("Alguno > 3:", algunoMayorque3);

// Every con array vacío
const vacio = [];
console.log("Array vacío every:", vacio.every(n => n > 0));

// Every no modifica el array
const original = [1, 2, 3];
const resultado = original.every(n => n > 0);
console.log("Array original:", original);
console.log("Resultado every:", resultado);

/*
output
Todos pares: true
Todos pares (con impar): false
Todas cortas: true
Todos activos: true
Todos son mayores de edad
Todos > 0: true
Alguno > 3: true
Array vacío every: true
Array original: [ 1, 2, 3 ]
Resultado every: true
*/
