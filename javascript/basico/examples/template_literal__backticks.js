/**
 * Objetivo: usar template literals para strings
 * Referencia: ``
 * Tipo: literal
 * Nivel: básico
 */

// Template literal básico
const nombre = "Laura";
const edad = 26;

const mensaje = `Hola, ${nombre}`;
console.log(mensaje);

// Template literal con expresiones
console.log(`${nombre} tiene ${edad} años`);

// Template literal con operaciones
const a = 10, b = 20;
console.log(`La suma de ${a} y ${b} es ${a + b}`);

// Template literal multilínea
const texto = `Este es un texto
que ocupa
varias líneas
sin necesidad de caracteres especiales`;
console.log(texto);

// Template literal con objetos
const persona = { nombre: "Roberto", profesion: "Desarrollador" };
console.log(`${persona.nombre} es ${persona.profesion}`);

// Template literal con condicional
const es_admin = true;
console.log(`El usuario ${es_admin ? "es" : "no es"} administrador`);

// Template literal con bucle
const colores = ["rojo", "verde", "azul"];
const lista = `Colores: ${colores.join(", ")}`;
console.log(lista);

/*
output
Hola, Laura
Laura tiene 26 años
La suma de 10 y 20 es 30
Este es un texto
que ocupa
varias líneas
sin necesidad de caracteres especiales
Roberto es Desarrollador
El usuario es administrador
Colores: rojo, verde, azul
*/
