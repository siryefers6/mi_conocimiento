/**
 * Objetivo: crear y usar arrays
 * Referencia: []
 * Tipo: literal
 * Nivel: básico
 */

// Array vacío
const vacio = [];
console.log(vacio);

// Array con números
const numeros = [1, 2, 3, 4, 5];
console.log(numeros);

// Array con strings
const colores = ["rojo", "verde", "azul"];
console.log(colores);

// Array mixto
const mixto = [1, "dos", true, { nombre: "objeto" }, [1, 2, 3]];
console.log(mixto);

// Array con constructor
const conConstructor = new Array(3);
console.log(conConstructor);

// Array con valores
const conValores = new Array(10, 20, 30);
console.log(conValores);

// Acceder a elementos
console.log(numeros[0]);
console.log(colores[2]);

// Acceder con variable
const indice = 1;
console.log(numeros[indice]);

/*
output
[]
[ 1, 2, 3, 4, 5 ]
[ 'rojo', 'verde', 'azul' ]
[
  1,
  'dos',
  true,
  { nombre: 'objeto' },
  [ 1, 2, 3 ]
]
[ <3 empty items> ]
[ 10, 20, 30 ]
1
azul
2
*/
