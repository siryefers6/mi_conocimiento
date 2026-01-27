/**
 * Objetivo: encontrar el primer elemento que cumple condición
 * Referencia: find()
 * Tipo: método
 * Nivel: intermedio
 */

// Find básico
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const primePar = numeros.find(n => n % 2 === 0);
console.log(primePar);

// Find no encontrado
const mayora100 = numeros.find(n => n > 100);
console.log(mayora100);

// Find con objetos
const usuarios = [
    { id: 1, nombre: "Ana", activo: true },
    { id: 2, nombre: "Bruno", activo: false },
    { id: 3, nombre: "Carlos", activo: true }
];

const usuario = usuarios.find(u => u.id === 2);
console.log(usuario);

// Find con strings
const palabras = ["sol", "luna", "mar", "montaña"];
const conM = palabras.find(p => p.includes("m"));
console.log(conM);

// Find buscando propiedad
const empleados = [
    { nombre: "Juan", departamento: "IT" },
    { nombre: "Elena", departamento: "HR" },
    { nombre: "Marco", departamento: "IT" }
];

const itEmployee = empleados.find(e => e.departamento === "IT");
console.log(itEmployee);

// Find con condicional
const edades = [10, 15, 18, 12, 25];
const primerMayorEdad = edades.find(e => e >= 18);
console.log(primerMayorEdad);

/*
output
2
undefined
{ id: 2, nombre: 'Bruno', activo: false }
montaña
{ nombre: 'Juan', departamento: 'IT' }
18
*/
