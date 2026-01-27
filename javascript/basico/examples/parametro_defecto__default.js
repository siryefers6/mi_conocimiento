/**
 * Objetivo: asignar valores por defecto a parámetros
 * Referencia: = valor
 * Tipo: operador
 * Nivel: básico
 */

// Parámetro con valor por defecto
function saludar(nombre = "Usuario") {
    console.log("Hola, " + nombre);
}

saludar("Juan");
saludar();

// Múltiples parámetros con defecto
function crearUsuario(nombre = "Anónimo", edad = 18, ciudad = "Sin ciudad") {
    return {
        nombre: nombre,
        edad: edad,
        ciudad: ciudad
    };
}

console.log(crearUsuario("Ana", 25, "Madrid"));
console.log(crearUsuario("Carlos"));
console.log(crearUsuario("Elena", 30));

// Arrow function con defecto
const multiplicar = (a = 1, b = 1) => a * b;

console.log(multiplicar(5, 4));
console.log(multiplicar(5));
console.log(multiplicar());

/*
output
Hola, Juan
Hola, Usuario
{ nombre: 'Ana', edad: 25, ciudad: 'Madrid' }
{ nombre: 'Carlos', edad: 18, ciudad: 'Sin ciudad' }
{ nombre: 'Elena', edad: 30, ciudad: 'Madrid' }
20
5
1
*/
