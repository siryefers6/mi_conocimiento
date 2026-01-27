/**
 * Objetivo: condicional en una línea
 * Referencia: ? :
 * Tipo: operador
 * Nivel: intermedio
 */

// Ternario básico
const edad = 20;
const puede = edad >= 18 ? "Sí" : "No";
console.log(puede);

// Ternario con números
const numero = 10;
const resultado = numero > 5 ? "Mayor" : "Menor";
console.log(resultado);

// Ternario anidado
const calificacion = 85;
const resultado2 = calificacion >= 90 ? "Excelente" :
                   calificacion >= 80 ? "Bueno" :
                   calificacion >= 70 ? "Aceptable" :
                   "Insuficiente";
console.log(resultado2);

// Ternario en variable
const dia = "lunes";
const mensaje = dia === "viernes" ? "¡Casi es fin de semana!" : "Día de trabajo";
console.log(mensaje);

// Ternario en array
const activo = true;
const estado = [activo ? "Activo" : "Inactivo"];
console.log(estado);

// Ternario en función
const obtenerEstado = (valor) => valor ? "Encendido" : "Apagado";
console.log(obtenerEstado(true));
console.log(obtenerEstado(false));

// Ternario con operaciones
const x = 10;
const y = 20;
const max = x > y ? x : y;
console.log("Máximo:", max);

// Ternario como alternativa a if/else
const nombre = null;
const nombreMostrado = nombre ? nombre : "Anónimo";
console.log(nombreMostrado);

/*
output
Sí
Mayor
Bueno
¡Casi es fin de semana!
[ 'Activo' ]
Encendido
Apagado
Máximo: 20
Anónimo
*/
