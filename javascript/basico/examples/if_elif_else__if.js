/**
 * Objetivo: múltiples condiciones secuenciales
 * Referencia: if...else if...else
 * Tipo: keyword
 * Nivel: básico
 */

// Múltiples condiciones
const calificacion = 85;

if (calificacion >= 90) {
    console.log("Sobresaliente");
} else if (calificacion >= 80) {
    console.log("Notable");
} else if (calificacion >= 70) {
    console.log("Bien");
} else if (calificacion >= 60) {
    console.log("Aprobado");
} else {
    console.log("Suspenso");
}

// Otra aplicación
const dia = "miércoles";

if (dia === "lunes") {
    console.log("Inicio de semana");
} else if (dia === "viernes") {
    console.log("Casi fin de semana");
} else if (dia === "sábado" || dia === "domingo") {
    console.log("Fin de semana");
} else {
    console.log("Día de semana");
}

/*
output
Notable
Día de semana
*/
