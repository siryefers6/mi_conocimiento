/**
 * Objetivo: iterar array elemento a elemento
 * Referencia: for...of
 * Tipo: keyword
 * Nivel: básico
 */

// For of con array
const numeros = [1, 2, 3, 4, 5];

for (const num of numeros) {
    console.log(num);
}

// For of con strings
const palabra = "hola";

for (const letra of palabra) {
    console.log(letra);
}

// For of con operación
const precios = [10, 20, 30, 40];

for (const precio of precios) {
    console.log("Precio: $" + precio);
}

// For of con array de objetos
const personas = [
    { nombre: "Ana", edad: 25 },
    { nombre: "Bruno", edad: 30 },
    { nombre: "Carlos", edad: 28 }
];

for (const persona of personas) {
    console.log(persona.nombre + " tiene " + persona.edad + " años");
}

// For of con break
const items = [10, 20, 30, 40, 50];

for (const item of items) {
    if (item === 30) {
        break;
    }
    console.log(item);
}

/*
output
1
2
3
4
5
h
o
l
a
Precio: $10
Precio: $20
Precio: $30
Precio: $40
Ana tiene 25 años
Bruno tiene 30 años
Carlos tiene 28 años
10
20
*/
