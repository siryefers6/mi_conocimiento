/**
 * Objetivo: acceder propiedades de objetos con punto
 * Referencia: objeto.propiedad
 * Tipo: operador
 * Nivel: básico
 */

const persona = {
    nombre: "Elena",
    edad: 28,
    ciudad: "Barcelona",
    profesion: "Ingeniera"
};

// Acceso con punto
console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.ciudad);

// Reasignar propiedad
persona.edad = 29;
console.log(persona.edad);

// Propiedad anidada
const empleado = {
    nombre: "Carlos",
    contacto: {
        email: "carlos@example.com",
        telefono: "987654321"
    },
    direccion: {
        calle: "Calle Principal",
        numero: 123,
        ciudad: "Madrid"
    }
};

console.log(empleado.contacto.email);
console.log(empleado.direccion.ciudad);

// Propiedades inexistentes
console.log(persona.pais);

// Con método
const coche = {
    marca: "BMW",
    velocidad: 0,
    acelerar: function() {
        this.velocidad += 20;
        return this.velocidad;
    }
};

console.log(coche.acelerar());

/*
output
Elena
28
Barcelona
29
carlos@example.com
Madrid
undefined
20
*/
