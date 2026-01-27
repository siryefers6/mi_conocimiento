/**
 * Objetivo: convertir objeto a JSON
 * Referencia: JSON.stringify()
 * Tipo: método
 * Nivel: intermedio
 */

// JSON.stringify básico
const usuario = { nombre: "Juan", edad: 30 };
const json = JSON.stringify(usuario);
console.log(json);
console.log(typeof json);

// JSON.stringify con array
const colores = ["rojo", "verde", "azul"];
console.log(JSON.stringify(colores));

// JSON.stringify con indentación
const persona = { nombre: "Elena", edad: 28, ciudad: "Madrid" };
const jsonFormateado = JSON.stringify(persona, null, 2);
console.log(jsonFormateado);

// JSON.stringify con nested objects
const empleado = {
    nombre: "Marco",
    contacto: {
        email: "marco@example.com",
        telefono: "123456789"
    }
};
console.log(JSON.stringify(empleado));

// JSON.stringify con null
console.log(JSON.stringify(null));

// JSON.stringify con array
const numeros = [1, 2, 3, 4, 5];
console.log(JSON.stringify(numeros));

// JSON.stringify con valores falsy
const datos = { a: 1, b: undefined, c: 3 };
console.log(JSON.stringify(datos));

// JSON.stringify reemplazar valores
const config = { host: "localhost", port: 3000, password: "secret" };
console.log(JSON.stringify(config, (k, v) => k === "password" ? "****" : v));

/*
output
{"nombre":"Juan","edad":30}
string
["rojo","verde","azul"]
{
  "nombre": "Elena",
  "edad": 28,
  "ciudad": "Madrid"
}
{"nombre":"Marco","contacto":{"email":"marco@example.com","telefono":"123456789"}}
null
[1,2,3,4,5]
{"a":1,"c":3}
{"host":"localhost","port":3000,"password":"****"}
*/
