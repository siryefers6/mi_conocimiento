/**
 * Objetivo: reemplazar texto en un string
 * Referencia: replace()
 * Tipo: método
 * Nivel: intermedio
 */

// Replace básico (primer match)
const texto = "hola mundo, hola javascript";
console.log(texto.replace("hola", "adiós"));

// Replace con regex global
const texto2 = "gato gato gato";
console.log(texto2.replace(/gato/g, "perro"));

// Replace case-insensitive
const texto3 = "Hola HOLA hola";
console.log(texto3.replace(/hola/gi, "hi"));

// Replace con función
const numeros = "1 2 3 4 5";
const duplicados = numeros.replace(/\d/g, match => match * 2);
console.log(duplicados);

// Replace múltiples ocurrencias
const csv = "nombre,edad,nombre";
console.log(csv.replace(/nombre/g, "name"));

// ReplaceAll (si existe)
const frase = "sol sol sol";
console.log(frase.replaceAll("sol", "luna"));

// Replace en variables
let url = "https://ejemplo.com/usuario/123";
url = url.replace("usuario", "perfil");
console.log(url);

// Replace con expresiones regulares
const email = "usuario@dominio.com";
console.log(email.replace(/@.*/, "@example.com"));

/*
output
adiós mundo, hola javascript
perro perro perro
hi hi hi
2 4 6 8 10
name,edad,name
luna luna luna
https://ejemplo.com/perfil/123
usuario@example.com
*/
