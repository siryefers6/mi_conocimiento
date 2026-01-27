/**
 * Objetivo: interpolación de expresiones en template literals
 * Referencia: `${expr}`
 * Tipo: literal
 * Nivel: intermedio
 */

// Interpolación básica
const nombre = "Ana";
const edad = 28;
console.log(`Mi nombre es ${nombre} y tengo ${edad} años`);

// Interpolación con operaciones
const a = 10;
const b = 20;
console.log(`La suma de ${a} y ${b} es ${a + b}`);

// Interpolación con métodos
const palabra = "javascript";
console.log(`Toda en mayúsculas: ${palabra.toUpperCase()}`);

// Interpolación con ternario
const activo = true;
console.log(`Estado: ${activo ? "activo" : "inactivo"}`);

// Interpolación con array
const colores = ["rojo", "verde", "azul"];
console.log(`Mis colores favoritos son: ${colores.join(", ")}`);

// Interpolación con objeto
const usuario = { nombre: "Carlos", edad: 32 };
console.log(`Usuario: ${usuario.nombre} (${usuario.edad} años)`);

// Interpolación con función
function duplicar(n) {
    return n * 2;
}

console.log(`El doble de 5 es ${duplicar(5)}`);

// Interpolación multilínea
const linea1 = "Hola";
const linea2 = "Mundo";
console.log(`${linea1}
${linea2}`);

/*
output
Mi nombre es Ana y tengo 28 años
La suma de 10 y 20 es 30
Toda en mayúsculas: JAVASCRIPT
Estado: activo
Mis colores favoritos son: rojo, verde, azul
Usuario: Carlos (32 años)
El doble de 5 es 10
Hola
Mundo
*/
