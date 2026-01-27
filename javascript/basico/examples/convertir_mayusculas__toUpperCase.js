/**
 * Objetivo: convertir string a mayúsculas
 * Referencia: toUpperCase()
 * Tipo: método
 * Nivel: intermedio
 */

// ToUpperCase básico
const texto = "hola";
console.log(texto.toUpperCase());

// ToUpperCase con puntuación
const frase = "hola mundo!";
console.log(frase.toUpperCase());

// ToUpperCase con números
const mixto = "hola123mundo";
console.log(mixto.toUpperCase());

// ToUpperCase en variables
const nombre = "juan";
const apellido = "garcía";
const nombreCompleto = nombre.toUpperCase() + " " + apellido.toUpperCase();
console.log(nombreCompleto);

// ToUpperCase en array
const palabras = ["sol", "luna", "estrella"];
const mayusculas = palabras.map(p => p.toUpperCase());
console.log(mayusculas);

// ToUpperCase en condicional
const entrada = "hola";
if (entrada.toUpperCase() === "HOLA") {
    console.log("Las palabras coinciden (case-insensitive)");
}

// ToUpperCase con caracteres especiales
const especial = "café, ñoño";
console.log(especial.toUpperCase());

/*
output
HOLA
HOLA MUNDO!
HOLA123MUNDO
JUAN GARCÍA
[ 'SOL', 'LUNA', 'ESTRELLA' ]
Las palabras coinciden (case-insensitive)
CAFÉ, ÑOÑO
*/
