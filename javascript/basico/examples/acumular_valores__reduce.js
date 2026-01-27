/**
 * Objetivo: acumular valores en un solo resultado
 * Referencia: reduce()
 * Tipo: método
 * Nivel: intermedio
 */

// Reduce suma básica
const numeros = [1, 2, 3, 4, 5];
const suma = numeros.reduce((acum, n) => acum + n, 0);
console.log(suma);

// Reduce sin valor inicial
const producto = [1, 2, 3, 4].reduce((acum, n) => acum * n);
console.log(producto);

// Reduce concatenar strings
const palabras = ["hola", "mundo", "desde", "js"];
const frase = palabras.reduce((acum, p) => acum + " " + p);
console.log(frase);

// Reduce contar elementos
const items = ["a", "b", "a", "c", "b", "a"];
const conteo = items.reduce((acum, item) => {
    acum[item] = (acum[item] || 0) + 1;
    return acum;
}, {});
console.log(conteo);

// Reduce con objetos
const usuarios = [
    { nombre: "Ana", edad: 25 },
    { nombre: "Bruno", edad: 30 },
    { nombre: "Carlos", edad: 28 }
];

const edadTotal = usuarios.reduce((suma, u) => suma + u.edad, 0);
console.log("Edad total:", edadTotal);

// Reduce promedio
const numeros2 = [10, 20, 30, 40, 50];
const promedio = numeros2.reduce((a, n) => a + n, 0) / numeros2.length;
console.log("Promedio:", promedio);

/*
output
15
24
hola mundo desde js
{ a: 3, b: 2, c: 1 }
Edad total: 83
Promedio: 30
*/
