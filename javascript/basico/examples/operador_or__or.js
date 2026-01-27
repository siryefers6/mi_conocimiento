/**
 * Objetivo: usar operador lógico OR
 * Referencia: ||
 * Tipo: operador
 * Nivel: básico
 */

// OR básico
console.log(true || true);
console.log(true || false);
console.log(false || true);
console.log(false || false);

// OR con comparaciones
const esFinDeSemana = false;
const esVacaciones = true;

if (esFinDeSemana || esVacaciones) {
    console.log("No hay que trabajar");
}

// OR con múltiples condiciones
const edad = 12;
const esEstudiante = true;

if (edad < 18 || esEstudiante) {
    console.log("Tienes descuento");
}

// OR cortocircuito
const x = 5;
const y = 10;

console.log(x > 10 || y > 5);
console.log(x > 10 || y < 5);

// OR para valores por defecto
const nombre = null;
const nombrePorDefecto = nombre || "Usuario anónimo";
console.log(nombrePorDefecto);

const descripcion = "Desarrollador";
const descPorDefecto = descripcion || "Sin descripción";
console.log(descPorDefecto);

/*
output
true
true
true
false
No hay que trabajar
Tienes descuento
true
false
Usuario anónimo
Desarrollador
*/
