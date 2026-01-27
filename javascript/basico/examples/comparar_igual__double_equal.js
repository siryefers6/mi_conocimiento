/**
 * Objetivo: comparar igualdad flexible
 * Referencia: ==
 * Tipo: operador
 * Nivel: básico
 */

// Iguales tipos
console.log(5 == 5);
console.log("hola" == "hola");
console.log(true == true);

// Desiguales
console.log(5 == 10);
console.log("hola" == "mundo");

// Conversión de tipos (loose equality)
console.log(5 == "5");  // true (string se convierte a número)
console.log(true == 1); // true (booleano se convierte a número)
console.log(false == 0); // true
console.log(null == undefined); // true

// Arrays y objetos
console.log([1] == [1]); // false (referencias diferentes)

// Variables
const a = 10;
const b = "10";
console.log(a == b);

// En condicionales
const edad = "25";
if (edad == 25) {
    console.log("Tienes 25 años (loose equality)");
}

// Comparaciones con null/undefined
console.log(null == null);
console.log(undefined == undefined);

/*
output
true
true
true
false
false
true
true
true
true
false
true
Tienes 25 años (loose equality)
true
true
*/
