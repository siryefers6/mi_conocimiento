/**
 * Objetivo: salir de un bucle antes de completarse
 * Referencia: break
 * Tipo: keyword
 * Nivel: básico
 */

// Break en for
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);
}

// Break al buscar elemento
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let encontrado = false;

for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] === 6) {
        console.log("Encontrado en índice", i);
        encontrado = true;
        break;
    }
}

// Break en while
let entrada = "";
let intento = 0;

while (true) {
    intento++;
    console.log("Intento " + intento);
    if (intento === 3) {
        break;
    }
}

/*
output
0
1
2
3
4
Encontrado en índice 5
Intento 1
Intento 2
Intento 3
*/
