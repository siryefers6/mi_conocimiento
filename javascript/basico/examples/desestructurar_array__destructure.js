/**
 * Objetivo: extraer valores específicos de un array
 * Referencia: [a, b] = array
 * Tipo: keyword
 * Nivel: intermedio
 */

// Desestructuración básica
const colores = ["rojo", "verde", "azul"];
const [color1, color2, color3] = colores;
console.log(color1, color2, color3);

// Desestructuración saltando elementos
const numeros = [1, 2, 3, 4, 5];
const [primero, , tercero] = numeros;
console.log(primero, tercero);

// Desestructuración con rest
const [a, b, ...resto] = [10, 20, 30, 40, 50];
console.log(a, b);
console.log(resto);

// Desestructuración con valores por defecto
const [x = 100, y = 200, z = 300] = [1, 2];
console.log(x, y, z);

// Desestructuración anidada
const datos = ["Ana", [25, "Madrid"]];
const [nombre, [edad, ciudad]] = datos;
console.log(nombre, edad, ciudad);

// Intercambiar variables
let var1 = "a";
let var2 = "b";
[var1, var2] = [var2, var1];
console.log(var1, var2);

// Retorno de múltiples valores
function coordenadas() {
    return [10, 20];
}

const [x2, y2] = coordenadas();
console.log("Posición:", x2, y2);

/*
output
rojo verde azul
1 3
[ 30, 40, 50 ]
1 2 300
Ana 25 Madrid
b a
Posición: 10 20
*/
