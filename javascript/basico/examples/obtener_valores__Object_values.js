/**
 * Objetivo: obtener los valores de un objeto
 * Referencia: Object.values()
 * Tipo: método
 * Nivel: intermedio
 */

// Object.values básico
const persona = { nombre: "Juan", edad: 30, ciudad: "Madrid" };
const valores = Object.values(persona);
console.log(valores);

// Object.values con array
const numeros = [10, 20, 30];
console.log(Object.values(numeros));

// Object.values vacío
const vacio = {};
console.log(Object.values(vacio));

// Object.values para sumar
const precios = { manzana: 2, banana: 1.5, cereza: 3 };
const total = Object.values(precios).reduce((a, b) => a + b, 0);
console.log("Total:", total);

// Object.values para procesar
const usuarios = { user1: 25, user2: 30, user3: 28 };
const promedioEdad = Object.values(usuarios).reduce((a, b) => a + b) / Object.keys(usuarios).length;
console.log("Promedio de edad:", promedioEdad);

// Object.values con map
const config = { width: 1024, height: 768, depth: 32 };
const valores2 = Object.values(config).map(v => v * 2);
console.log(valores2);

// Object.values con filter
const puntuaciones = { juan: 85, elena: 92, marco: 78 };
const altas = Object.values(puntuaciones).filter(p => p > 80);
console.log("Puntuaciones altas:", altas);

/*
output
[ 'Juan', 30, 'Madrid' ]
[ 10, 20, 30 ]
[]
Total: 6.5
Promedio de edad: 27.666666666666668
[ 2048, 1536, 64 ]
Puntuaciones altas: [ 85, 92 ]
*/
