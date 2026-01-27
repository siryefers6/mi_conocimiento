/**
 * Objetivo: repetir código mientras se cumpla una condición
 * Referencia: while
 * Tipo: keyword
 * Nivel: básico
 */

// While básico
let contador = 0;

while (contador < 3) {
    console.log("Contador: " + contador);
    contador++;
}

// While con condición variable
let creditos = 5;

while (creditos > 0) {
    console.log("Créditos restantes: " + creditos);
    creditos--;
}

// While con lógica
let entrada = "";
let intentos = 0;

// Simulación (en el navegador pedirías input)
let intentosMaximos = 2;
while (entrada !== "contraseña" && intentos < intentosMaximos) {
    entrada = "intento"; // Cambiar para evitar bucle infinito
    intentos++;
    console.log("Intento " + intentos);
}

/*
output
Contador: 0
Contador: 1
Contador: 2
Créditos restantes: 5
Créditos restantes: 4
Créditos restantes: 3
Créditos restantes: 2
Créditos restantes: 1
Intento 1
Intento 2
*/
