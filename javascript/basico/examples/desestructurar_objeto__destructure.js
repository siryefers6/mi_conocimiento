/**
 * Objetivo: extraer propiedades específicas de un objeto
 * Referencia: {a, b} = objeto
 * Tipo: keyword
 * Nivel: intermedio
 */

// Desestructuración básica
const persona = { nombre: "Juan", edad: 30, ciudad: "Madrid" };
const { nombre, edad, ciudad } = persona;
console.log(nombre, edad, ciudad);

// Desestructuración con nuevo nombre
const { nombre: n, edad: a } = persona;
console.log(n, a);

// Desestructuración con valores por defecto
const { pais = "España" } = persona;
console.log(pais);

// Desestructuración parcial
const { nombre: nom, edad: ed } = persona;
console.log(nom, ed);

// Desestructuración anidada
const empleado = {
    nombre: "Elena",
    contacto: {
        email: "elena@example.com",
        telefono: "123456789"
    }
};

const { contacto: { email } } = empleado;
console.log(email);

// Rest en objetos
const { nombre: name, ...resto } = persona;
console.log(name);
console.log(resto);

// Desestructuración en parámetros
function mostrar({ nombre, edad }) {
    console.log(`${nombre} tiene ${edad} años`);
}

mostrar(persona);

/*
output
Juan 30 Madrid
Juan 30
España
Juan 30
elena@example.com
Juan
{ edad: 30, ciudad: 'Madrid' }
Juan tiene 30 años
*/
