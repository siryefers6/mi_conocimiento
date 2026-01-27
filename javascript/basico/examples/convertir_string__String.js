/**
 * Objetivo: convertir valores a string
 * Referencia: String()
 * Tipo: función
 * Nivel: básico
 */

// Convertir número a string
const numero = 42;
const numeroStr = String(numero);
console.log(numeroStr);
console.log(typeof numeroStr);

// Convertir booleano a string
const booleano = true;
const booleanoStr = String(booleano);
console.log(booleanoStr);

// Convertir null y undefined
console.log(String(null));
console.log(String(undefined));

// Convertir array a string
const array = [1, 2, 3, 4, 5];
const arrayStr = String(array);
console.log(arrayStr);

// Convertir objeto a string
const objeto = { nombre: "Sofía", edad: 28 };
const objetoStr = String(objeto);
console.log(objetoStr);

// Usar con método toString()
const decimal = 99.99;
console.log(decimal.toString());

// Convertir con contexto
const fecha = new Date("2024-01-27");
console.log(String(fecha));

/*
output
42
string
true
null
undefined
1,2,3,4,5
[object Object]
99.99
Sun Jan 27 2024 01:00:00 GMT+0100 (Hora central de Europa)
*/
