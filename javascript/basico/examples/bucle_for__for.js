/**
 * Objetivo: iterar un número específico de veces
 * Referencia: for
 * Tipo: keyword
 * Nivel: básico
 */

// Bucle for básico
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// Bucle con strings
for (let i = 1; i <= 3; i++) {
    console.log("Iteración " + i);
}

// Iterar sobre array
const numeros = [10, 20, 30];

for (let i = 0; i < numeros.length; i++) {
    console.log(numeros[i]);
}

// Bucle decreciente
for (let i = 3; i > 0; i--) {
    console.log(i);
}

/*
output
0
1
2
3
4
Iteración 1
Iteración 2
Iteración 3
10
20
30
3
2
1
*/
