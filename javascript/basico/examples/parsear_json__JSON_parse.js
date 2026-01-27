/**
 * Objetivo: convertir JSON a objeto
 * Referencia: JSON.parse()
 * Tipo: método
 * Nivel: intermedio
 */

// JSON.parse básico
const jsonString = '{"nombre":"Juan","edad":30}';
const objeto = JSON.parse(jsonString);
console.log(objeto);
console.log(objeto.nombre);

// JSON.parse con array
const jsonArray = '[1,2,3,4,5]';
const array = JSON.parse(jsonArray);
console.log(array);

// JSON.parse con nested objects
const jsonComplejo = '{"usuario":{"nombre":"Elena","edad":28}}';
const datos = JSON.parse(jsonComplejo);
console.log(datos.usuario.nombre);

// JSON.parse con try/catch
const jsonInvalido = '{"nombre":"Juan"'; // JSON inválido
try {
    const resultado = JSON.parse(jsonInvalido);
} catch (error) {
    console.log("Error de parsing:", error.message);
}

// JSON.parse con revisor
const jsonDatos = '{"numero":10,"string":"texto"}';
const revisor = (clave, valor) => {
    if (typeof valor === "number") {
        return valor * 2;
    }
    return valor;
};
console.log(JSON.parse(jsonDatos, revisor));

// JSON.parse para validar
const jsonValido = '{"email":"user@example.com","activo":true}';
const usuario = JSON.parse(jsonValido);
console.log("Usuario parseado:", usuario);

// Ciclo completo: stringify y parse
const original = { nombre: "Marco", edad: 32 };
const json = JSON.stringify(original);
const recuperado = JSON.parse(json);
console.log("Original:", original);
console.log("Recuperado:", recuperado);

/*
output
{ nombre: 'Juan', edad: 30 }
Juan
[ 1, 2, 3, 4, 5 ]
Elena
Error de parsing: Unexpected end of JSON input
{ numero: 20, string: 'texto' }
Usuario parseado: { email: 'user@example.com', activo: true }
Original: { nombre: 'Marco', edad: 32 }
Recuperado: { nombre: 'Marco', edad: 32 }
*/
