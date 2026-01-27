/**
 * Objetivo: declarar una variable inmutable
 * Referencia: const
 * Tipo: keyword
 * Nivel: básico
 */

// Declarar una constante
const pi = 3.14159;
console.log(pi);

// const no puede ser reasignada
// pi = 3.14; // Error

// const con objeto (el objeto sí puede cambiar internamente)
const persona = { nombre: "Carlos", edad: 30 };
console.log(persona);

persona.edad = 31;
console.log(persona);

// const con array
const colores = ["rojo", "verde", "azul"];
console.log(colores);

colores.push("amarillo");
console.log(colores);

/*
output
3.14159
{ nombre: 'Carlos', edad: 30 }
{ nombre: 'Carlos', edad: 31 }
[ 'rojo', 'verde', 'azul' ]
[ 'rojo', 'verde', 'azul', 'amarillo' ]
*/
