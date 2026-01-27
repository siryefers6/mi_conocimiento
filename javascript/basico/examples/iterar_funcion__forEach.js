/**
 * Objetivo: iterar array con función
 * Referencia: forEach()
 * Tipo: método
 * Nivel: intermedio
 */

// ForEach básico
const numeros = [1, 2, 3, 4, 5];
numeros.forEach(n => {
    console.log(n);
});

console.log("---");

// ForEach con índice
const colores = ["rojo", "verde", "azul"];
colores.forEach((color, indice) => {
    console.log(`${indice}: ${color}`);
});

console.log("---");

// ForEach con array (parámetro)
const items = ["a", "b", "c"];
items.forEach((item, indice, array) => {
    console.log(`Elemento ${indice} de ${array.length}: ${item}`);
});

console.log("---");

// ForEach con objetos
const usuarios = [
    { nombre: "Juan", edad: 25 },
    { nombre: "Elena", edad: 30 },
    { nombre: "Marco", edad: 28 }
];

usuarios.forEach(usuario => {
    console.log(`${usuario.nombre} - ${usuario.edad} años`);
});

console.log("---");

// ForEach con operación
const precios = [10, 20, 30];
let total = 0;
precios.forEach(precio => {
    total += precio;
});
console.log("Total:", total);

// ForEach no retorna (a diferencia de map)
const resultado = numeros.forEach(n => n * 2);
console.log("Resultado forEach:", resultado);

/*
output
1
2
3
4
5
---
0: rojo
1: verde
2: azul
---
Elemento 0 de 3: a
Elemento 1 de 3: b
Elemento 2 de 3: c
---
Juan - 25 años
Elena - 30 años
Marco - 28 años
---
Total: 60
Resultado forEach: undefined
*/
