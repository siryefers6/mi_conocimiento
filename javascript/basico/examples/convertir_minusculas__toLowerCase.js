/**
 * Objetivo: convertir string a minúsculas
 * Referencia: toLowerCase()
 * Tipo: método
 * Nivel: intermedio
 */

// ToLowerCase básico
const texto = "HOLA";
console.log(texto.toLowerCase());

// ToLowerCase con puntuación
const frase = "HOLA MUNDO!";
console.log(frase.toLowerCase());

// ToLowerCase con números
const mixto = "HOLA123MUNDO";
console.log(mixto.toLowerCase());

// ToLowerCase en variables
const nombre = "JUAN";
const apellido = "GARCÍA";
const nombreCompleto = (nombre + " " + apellido).toLowerCase();
console.log(nombreCompleto);

// ToLowerCase en array
const palabras = ["SOL", "LUNA", "ESTRELLA"];
const minusculas = palabras.map(p => p.toLowerCase());
console.log(minusculas);

// ToLowerCase en condicional (case-insensitive)
const entrada = "JAVASCRIPT";
if (entrada.toLowerCase() === "javascript") {
    console.log("Las palabras coinciden (case-insensitive)");
}

// ToLowerCase para normalizar
const email = "USUARIO@EXAMPLE.COM";
const emailNormalizado = email.toLowerCase();
console.log(emailNormalizado);

/*
output
hola
hola mundo!
hola123mundo
juan garcía
[ 'sol', 'luna', 'estrella' ]
Las palabras coinciden (case-insensitive)
usuario@example.com
*/
