/**
 * Objetivo: crear y usar strings
 * Referencia: ""  ''
 * Tipo: literal
 * Nivel: básico
 */

// String con comillas dobles
const nombre = "Juan";
console.log(nombre);

// String con comillas simples
const apellido = 'García';
console.log(apellido);

// String vacío
const vacio = "";
console.log(vacio.length);

// String con caracteres especiales
const textoEspecial = "Hola \"Mundo\" con 'comillas'";
console.log(textoEspecial);

// String con saltos de línea
const parrafo = "Primera línea\nSegunda línea\nTercera línea";
console.log(parrafo);

// String con tabulación
const indentado = "Nombre:\tJuan\nEdad:\t25";
console.log(indentado);

// String con concatenación
const mensaje = "Hola" + " " + nombre + " " + apellido;
console.log(mensaje);

// String de múltiples líneas
const multilinea = "Este es un texto\n" +
                   "que ocupa\n" +
                   "varias líneas";
console.log(multilinea);

/*
output
Juan
García
0
Hola "Mundo" con 'comillas'
Primera línea
Segunda línea
Tercera línea
Nombre:	Juan
Edad:	25
Hola Juan García
Este es un texto
que ocupa
varias líneas
*/
