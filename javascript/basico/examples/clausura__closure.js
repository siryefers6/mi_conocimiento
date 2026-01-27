/**
 * Objetivo: mantener estado privado con closures
 * Referencia: función anidada
 * Tipo: patrón
 * Nivel: intermedio
 */

// Closure básico
function crearContador() {
    let contador = 0;
    
    return function() {
        contador++;
        return contador;
    };
}

const contador1 = crearContador();
console.log(contador1());
console.log(contador1());
console.log(contador1());

// Closure con múltiples métodos
function crearBilletera(saldoInicial) {
    let saldo = saldoInicial;
    
    return {
        depositar(cantidad) {
            saldo += cantidad;
            return saldo;
        },
        retirar(cantidad) {
            if (cantidad <= saldo) {
                saldo -= cantidad;
                return saldo;
            }
            return "Saldo insuficiente";
        },
        obtenerSaldo() {
            return saldo;
        }
    };
}

const billetera = crearBilletera(1000);
console.log("Saldo inicial:", billetera.obtenerSaldo());
console.log("Después de depositar 500:", billetera.depositar(500));
console.log("Después de retirar 200:", billetera.retirar(200));

// Closure con parámetro
function crearMultiplicador(factor) {
    return function(numero) {
        return numero * factor;
    };
}

const duplicar = crearMultiplicador(2);
const triplicar = crearMultiplicador(3);

console.log("Duplicar 5:", duplicar(5));
console.log("Triplicar 5:", triplicar(5));

// Closure con IIFE
const modulo = (function() {
    let datos = [];
    
    return {
        agregar(item) {
            datos.push(item);
        },
        obtener() {
            return datos;
        }
    };
})();

modulo.agregar("A");
modulo.agregar("B");
console.log("Datos del módulo:", modulo.obtener());

/*
output
1
2
3
Saldo inicial: 1000
Después de depositar 500: 1500
Después de retirar 200: 1300
Duplicar 5: 10
Triplicar 5: 15
Datos del módulo: [ 'A', 'B' ]
*/
