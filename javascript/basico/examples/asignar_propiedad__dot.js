/**
 * Objetivo: crear y reasignar propiedades de objetos
 * Referencia: objeto.propiedad = valor
 * Tipo: operador
 * Nivel: básico
 */

// Crear propiedades en objeto vacío
const usuario = {};

usuario.nombre = "Sofia";
usuario.edad = 24;
usuario.email = "sofia@example.com";

console.log(usuario);

// Reasignar propiedades
usuario.edad = 25;
console.log(usuario.edad);

// Agregar propiedades a objeto existente
const coche = {
    marca: "Audi",
    modelo: "A4"
};

coche.ano = 2023;
coche.color = "rojo";
console.log(coche);

// Asignar objeto como propiedad
const persona = { nombre: "Luis" };
persona.amigo = { nombre: "Miguel" };
console.log(persona);

// Asignar función como propiedad
const calculadora = {};
calculadora.sumar = function(a, b) {
    return a + b;
};

console.log(calculadora.sumar(5, 3));

// Propiedades con nombres especiales
const config = {};
config["max-size"] = 100;
config["is-active"] = true;
console.log(config);

/*
output
{ nombre: 'Sofia', edad: 24, email: 'sofia@example.com' }
25
{ marca: 'Audi', modelo: 'A4', ano: 2023, color: 'rojo' }
{ nombre: 'Luis', amigo: { nombre: 'Miguel' } }
8
{ 'max-size': 100, 'is-active': true }
*/
