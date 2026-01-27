/**
 * Objetivo: seleccionar elementos que cumplen una condición
 * Referencia: filter()
 * Tipo: método
 * Nivel: intermedio
 */

// Filter básico
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const pares = numeros.filter(n => n % 2 === 0);
console.log(pares);

// Filter con comparación
const edades = [15, 18, 12, 25, 30, 16];
const mayoresEdad = edades.filter(e => e >= 18);
console.log(mayoresEdad);

// Filter con strings
const palabras = ["sol", "luna", "mar", "montaña", "rio"];
const largas = palabras.filter(p => p.length > 3);
console.log(largas);

// Filter con objetos
const usuarios = [
    { nombre: "Ana", activo: true },
    { nombre: "Bruno", activo: false },
    { nombre: "Carlos", activo: true }
];

const activos = usuarios.filter(u => u.activo);
console.log(activos);

// Filter múltiples condiciones
const numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const resultado = numeros2.filter(n => n > 3 && n < 8);
console.log(resultado);

/*
output
[ 2, 4, 6, 8, 10 ]
[ 18, 25, 30 ]
[ 'luna', 'montaña' ]
[ { nombre: 'Ana', activo: true }, { nombre: 'Carlos', activo: true } ]
[ 4, 5, 6, 7 ]
*/
