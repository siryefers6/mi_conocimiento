/**
 * Objetivo: usar función como argumento (callback)
 * Referencia: fn(callback)
 * Tipo: patrón
 * Nivel: intermedio
 */

// Callback básico
function procesarDatos(datos, callback) {
    console.log("Procesando...");
    callback(datos);
}

function mostrar(resultado) {
    console.log("Resultado:", resultado);
}

procesarDatos("Datos importantes", mostrar);

// Callback con array
function recorrer(arr, callback) {
    for (let i = 0; i < arr.length; i++) {
        callback(arr[i], i);
    }
}

recorrer(["a", "b", "c"], (item, indice) => {
    console.log(`${indice}: ${item}`);
});

// Callback con error
function dividir(a, b, callback) {
    if (b === 0) {
        callback(new Error("No se puede dividir entre cero"));
    } else {
        callback(null, a / b);
    }
}

dividir(10, 2, (error, resultado) => {
    if (error) {
        console.log("Error:", error.message);
    } else {
        console.log("División:", resultado);
    }
});

// Callback en setTimeout
function despuesDeUnTiempo(callback) {
    setTimeout(() => {
        callback("¡Listo!");
    }, 100);
}

despuesDeUnTiempo(resultado => console.log(resultado));

// Callback en filter
const numeros = [1, 2, 3, 4, 5];
const pares = numeros.filter(n => n % 2 === 0);
console.log("Pares:", pares);

/*
output
Procesando...
Resultado: Datos importantes
0: a
1: b
2: c
División: 5
¡Listo!
Pares: [ 2, 4 ]
*/
