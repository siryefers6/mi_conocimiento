/**
 * Objetivo: saltar a la siguiente iteración
 * Referencia: continue
 * Tipo: keyword
 * Nivel: básico
 */

// Continue en for: saltar números pares
for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) {
        continue;
    }
    console.log(i);
}

console.log("---");

// Continue evitando valores específicos
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] === 5 || numeros[i] === 8) {
        continue;
    }
    console.log(numeros[i]);
}

console.log("---");

// Continue en while
let contador = 0;

while (contador < 6) {
    contador++;
    if (contador === 3) {
        continue;
    }
    console.log("Contador: " + contador);
}

/*
output
1
3
5
7
9
---
1
2
3
4
6
7
9
10
---
Contador: 1
Contador: 2
Contador: 4
Contador: 5
Contador: 6
*/
