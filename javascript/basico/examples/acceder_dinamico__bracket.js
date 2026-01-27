/**
 * Objetivo: acceder propiedades dinámicamente con corchetes
 * Referencia: objeto[clave]
 * Tipo: operador
 * Nivel: básico
 */

const persona = {
    nombre: "Marco",
    edad: 32,
    ciudad: "Valencia"
};

// Acceso con corchetes
console.log(persona["nombre"]);
console.log(persona["edad"]);

// Con variable
const propiedad = "ciudad";
console.log(persona[propiedad]);

// Cambiar propiedad dinámicamente
const clave = "edad";
persona[clave] = 33;
console.log(persona.edad);

// Recorrer propiedades
const datos = { x: 10, y: 20, z: 30 };
for (let key in datos) {
    console.log(key + " = " + datos[key]);
}

// Agregar propiedad dinámicamente
const obj = { a: 1 };
const nuevaPropiedad = "b";
obj[nuevaPropiedad] = 2;
console.log(obj);

// Propiedades con espacios
const config = {
    "max-width": 1200,
    "background-color": "blue"
};
console.log(config["max-width"]);

/*
output
Marco
32
Valencia
33
x = 10
y = 20
z = 30
{ a: 1, b: 2 }
1200
*/
