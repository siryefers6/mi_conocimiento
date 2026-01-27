/**
 * Objetivo: crear objetos con propiedades
 * Referencia: {}
 * Tipo: literal
 * Nivel: básico
 */

// Objeto vacío
const vacio = {};
console.log(vacio);

// Objeto con propiedades
const persona = {
    nombre: "Juan",
    edad: 30,
    ciudad: "Madrid"
};
console.log(persona);

// Objeto con diferentes tipos de datos
const mixto = {
    nombre: "Ana",
    edad: 25,
    activo: true,
    hobbies: ["leer", "deportes"],
    contacto: {
        email: "ana@example.com",
        telefono: "123456789"
    }
};
console.log(mixto);

// Objeto con métodos
const coche = {
    marca: "Toyota",
    modelo: "Camry",
    ano: 2023,
    encender: function() {
        return "El coche está encendido";
    }
};
console.log(coche);
console.log(coche.encender());

// Objeto con constructor
const obj = new Object();
obj.propiedad = "valor";
console.log(obj);

/*
output
{}
{ nombre: 'Juan', edad: 30, ciudad: 'Madrid' }
{
  nombre: 'Ana',
  edad: 25,
  activo: true,
  hobbies: [ 'leer', 'deportes' ],
  contacto: { email: 'ana@example.com', telefono: '123456789' }
}
{
  marca: 'Toyota',
  modelo: 'Camry',
  ano: 2023,
  encender: [Function: encender]
}
El coche está encendido
{ propiedad: 'valor' }
*/
