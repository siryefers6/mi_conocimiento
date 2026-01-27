/**
 * Objetivo: eliminar espacios en blanco al inicio y final
 * Referencia: trim()
 * Tipo: método
 * Nivel: intermedio
 */

// Trim básico
const conEspacios = "  hola  ";
console.log("'" + conEspacios + "'");
console.log("'" + conEspacios.trim() + "'");

// Trim solo inicio
const trimStart = "  texto";
console.log("'" + trimStart.trimStart() + "'");

// Trim solo final
const trimEnd = "texto  ";
console.log("'" + trimEnd.trimEnd() + "'");

// Trim con entrada de usuario
const entrada = "  Juan García  ";
const limpio = entrada.trim();
console.log("Entrada: '" + entrada + "'");
console.log("Limpio: '" + limpio + "'");

// Trim en array de strings
const palabras = ["  hola", "mundo  ", "  desde  "];
const trimmed = palabras.map(p => p.trim());
console.log(trimmed);

// Trim antes de split
const csv = "  Juan, 25, Madrid  ";
const datos = csv.split(",").map(d => d.trim());
console.log(datos);

// Verificar si está vacío después de trim
const texto = "   ";
if (texto.trim() === "") {
    console.log("El texto está vacío después de trim");
}

/*
output
'  hola  '
'hola'
'texto'
'texto'
Entrada: '  Juan García  '
Limpio: 'Juan García'
[ 'hola', 'mundo', 'desde' ]
[ 'Juan', '25', 'Madrid' ]
El texto está vacío después de trim
*/
