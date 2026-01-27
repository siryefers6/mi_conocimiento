/**
 * Objetivo: iterar sobre las claves de un objeto
 * Referencia: for...in
 * Tipo: keyword
 * Nivel: básico
 */

// For in básico
const persona = {
    nombre: "Diego",
    edad: 31,
    ciudad: "Sevilla"
};

for (const clave in persona) {
    console.log(clave + ": " + persona[clave]);
}

// For in con array (no recomendado, pero funciona)
const colores = ["rojo", "verde", "azul"];

for (const indice in colores) {
    console.log(indice + ": " + colores[indice]);
}

// For in con objeto anidado
const empleado = {
    nombre: "Gabriela",
    contacto: {
        email: "gabriela@example.com",
        telefono: "555-1234"
    },
    activo: true
};

for (const clave in empleado) {
    console.log(clave + " =", empleado[clave]);
}

// For in con condición
const config = {
    debug: true,
    timeout: 5000,
    maxAttempts: 3,
    language: "es"
};

for (const opcion in config) {
    if (config[opcion] === true) {
        console.log(opcion + " está habilitado");
    }
}

/*
output
nombre: Diego
edad: 31
ciudad: Sevilla
0: rojo
1: verde
2: azul
nombre = Gabriela
contacto = { email: 'gabriela@example.com', telefono: '555-1234' }
activo = true
debug está habilitado
*/
