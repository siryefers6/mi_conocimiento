/**
 * Objetivo: transformar cada elemento de un array
 * Referencia: map()
 * Tipo: método
 * Nivel: intermedio
 */

// Map básico
const numeros = [1, 2, 3, 4, 5];
const dobles = numeros.map(n => n * 2);
console.log(dobles);

// Map con strings
const nombres = ["ana", "bruno", "carlos"];
const mayusculas = nombres.map(n => n.toUpperCase());
console.log(mayusculas);

// Map con objetos
const usuarios = [
    { nombre: "Juan", edad: 25 },
    { nombre: "Elena", edad: 30 },
    { nombre: "Marco", edad: 28 }
];

const edades = usuarios.map(u => u.edad);
console.log(edades);

// Map con función personalizada
function cuadrado(numero) {
    return numero * numero;
}

const cuadrados = [1, 2, 3, 4].map(cuadrado);
console.log(cuadrados);

// Map con índice
const items = ["a", "b", "c"];
const conIndice = items.map((item, indice) => `${indice}: ${item}`);
console.log(conIndice);

/*
output
[ 2, 4, 6, 8, 10 ]
[ 'ANA', 'BRUNO', 'CARLOS' ]
[ 25, 30, 28 ]
[ 1, 4, 9, 16 ]
[ '0: a', '1: b', '2: c' ]
*/
