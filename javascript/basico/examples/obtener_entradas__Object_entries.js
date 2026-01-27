/**
 * Objetivo: obtener pares clave-valor de un objeto
 * Referencia: Object.entries()
 * Tipo: método
 * Nivel: intermedio
 */

// Object.entries básico
const persona = { nombre: "Juan", edad: 30, ciudad: "Madrid" };
const entradas = Object.entries(persona);
console.log(entradas);

// Object.entries con desestructuración
for (const [clave, valor] of Object.entries(persona)) {
    console.log(`${clave}: ${valor}`);
}

// Object.entries con map
const config = { debug: true, timeout: 5000, maxRetries: 3 };
const items = Object.entries(config).map(([k, v]) => `${k}=${v}`);
console.log(items);

// Object.entries con filter
const usuario = { nombre: "Elena", edad: 28, activo: true, premium: false };
const activos = Object.entries(usuario)
    .filter(([k, v]) => v === true)
    .map(([k]) => k);
console.log("Propiedades verdaderas:", activos);

// Object.entries con reduce
const datos = { a: 1, b: 2, c: 3 };
const objeto = Object.entries(datos).reduce((obj, [k, v]) => {
    obj[k] = v * 2;
    return obj;
}, {});
console.log(objeto);

// Object.entries con array
const numeros = [10, 20, 30];
const conIndices = Object.entries(numeros);
console.log(conIndices);

// Object.entries vacío
const vacio = {};
console.log(Object.entries(vacio));

/*
output
[ [ 'nombre', 'Juan' ], [ 'edad', 30 ], [ 'ciudad', 'Madrid' ] ]
nombre: Juan
edad: 30
ciudad: Madrid
[ 'debug=true', 'timeout=5000', 'maxRetries=3' ]
Propiedades verdaderas: [ 'activo' ]
{ a: 2, b: 4, c: 6 }
[ [ '0', 10 ], [ '1', 20 ], [ '2', 30 ] ]
[]
*/
