/**
 * Objetivo: verificar si un string contiene un texto
 * Referencia: includes()
 * Tipo: método
 * Nivel: intermedio
 */

// Includes básico
const texto = "javascript es genial";
console.log(texto.includes("javascript"));
console.log(texto.includes("python"));

// Includes case-sensitive
const frase = "Hola Mundo";
console.log(frase.includes("Hola"));
console.log(frase.includes("hola"));

// Includes con position
const palabra = "supercalifragilistico";
console.log(palabra.includes("cal"));
console.log(palabra.includes("cal", 5));

// Includes en condicional
const email = "usuario@example.com";

if (email.includes("@")) {
    console.log("Es un email válido");
}

// Includes para validar
const url = "https://google.com";
if (url.includes("https://")) {
    console.log("Es una URL segura");
}

// Includes en array de strings
const palabras = ["gato", "perro", "pajaro"];
const buscar = "gato";

if (palabras.some(p => p.includes("ga"))) {
    console.log("Hay una palabra que contiene 'ga'");
}

// Includes para búsqueda de patrones
const comentario = "Este código es muy lento";
if (comentario.includes("lento")) {
    console.log("Detectado problema de rendimiento");
}

/*
output
true
false
true
false
true
true
Es un email válido
Es una URL segura
Hay una palabra que contiene 'ga'
Detectado problema de rendimiento
*/
