/**
 * Objetivo: obtener el residuo de una división
 * Referencia: %
 * Tipo: operador
 * Nivel: básico
 */

// Módulo básico
console.log(10 % 3);
console.log(20 % 5);
console.log(7 % 2);

// Detectar números pares
console.log(4 % 2);
console.log(7 % 2);

const numero = 12;
if (numero % 2 === 0) {
    console.log("Es par");
} else {
    console.log("Es impar");
}

// Detectar números impares
const numero2 = 15;
if (numero2 % 2 !== 0) {
    console.log("Es impar");
}

// Ciclos con módulo
for (let i = 1; i <= 10; i++) {
    if (i % 3 === 0) {
        console.log(i + " es divisible por 3");
    }
}

// Obtener últimos dígitos
console.log(12345 % 10);    // 5
console.log(12345 % 100);   // 45
console.log(12345 % 1000);  // 345

// Con números negativos
console.log(-7 % 2);
console.log(7 % -2);

/*
output
1
0
1
0
1
Es par
Es impar
3 es divisible por 3
6 es divisible por 3
9 es divisible por 3
5
45
345
-1
1
*/
