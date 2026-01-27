/**
 * Objetivo: obtener las claves de un objeto
 * Referencia: Object.keys()
 * Tipo: método
 * Nivel: intermedio
 */

// Object.keys básico
const persona = { nombre: "Juan", edad: 30, ciudad: "Madrid" };
const claves = Object.keys(persona);
console.log(claves);

// Object.keys con array
const colores = ["rojo", "verde", "azul"];
console.log(Object.keys(colores));

// Object.keys vacío
const vacio = {};
console.log(Object.keys(vacio));

// Object.keys para iterar
const config = { debug: true, timeout: 5000, maxRetries: 3 };
for (const clave of Object.keys(config)) {
    console.log(`${clave}: ${config[clave]}`);
}

// Object.keys con map
const producto = { nombre: "Laptop", precio: 999, stock: 5 };
const valores = Object.keys(producto).map(clave => producto[clave]);
console.log(valores);

// Object.keys con filter
const usuario = { nombre: "Elena", edad: 28, password: "secret", email: "elena@ex.com" };
const publicKeys = Object.keys(usuario).filter(k => k !== "password");
console.log(publicKeys);

// Object.keys.length
const datos = { a: 1, b: 2, c: 3 };
console.log("Cantidad de propiedades:", Object.keys(datos).length);

/*
output
[ 'nombre', 'edad', 'ciudad' ]
[ '0', '1', '2' ]
[]
debug: true
timeout: 5000
maxRetries: 3
[ 'Laptop', 999, 5 ]
[ 'nombre', 'edad', 'email' ]
Cantidad de propiedades: 3
*/
