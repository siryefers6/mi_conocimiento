/**
 * Objetivo: añadir elementos al final de un array
 * Referencia: push()
 * Tipo: método
 * Nivel: básico
 */

// Push un elemento
const numeros = [1, 2, 3];
console.log(numeros);

numeros.push(4);
console.log(numeros);

// Push múltiples elementos
const frutas = ["manzana"];
frutas.push("banana", "cereza", "dátil");
console.log(frutas);

// Push con variable
const colores = ["rojo"];
const nuevoColor = "azul";
colores.push(nuevoColor);
console.log(colores);

// Push retorna la nueva longitud
const items = [10, 20];
const newLength = items.push(30);
console.log("Nueva longitud:", newLength);
console.log("Array:", items);

// Push con objeto
const personas = [];
personas.push({ nombre: "Ana", edad: 25 });
personas.push({ nombre: "Carlos", edad: 30 });
console.log(personas);

/*
output
[ 1, 2, 3 ]
[ 1, 2, 3, 4 ]
[ 'manzana', 'banana', 'cereza', 'dátil' ]
[ 'rojo', 'azul' ]
Nueva longitud: 3
Array: [ 10, 20, 30 ]
[
  { nombre: 'Ana', edad: 25 },
  { nombre: 'Carlos', edad: 30 }
]
*/
