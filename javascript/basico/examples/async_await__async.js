/**
 * Objetivo: usar async/await para código asincrónico
 * Referencia: async / await
 * Tipo: keyword
 * Nivel: intermedio
 */

// Async/await básico
async function obtenerDatos() {
    return "Datos obtenidos";
}

obtenerDatos().then(resultado => console.log(resultado));

// Await con Promise
async function ejemplo() {
    const promesa = new Promise(resolve => {
        setTimeout(() => resolve("¡Listo!"), 100);
    });
    
    const resultado = await promesa;
    console.log(resultado);
}

ejemplo();

// Await múltiples promesas secuenciales
async function procesarSecuencial() {
    const paso1 = await Promise.resolve(10);
    console.log("Paso 1:", paso1);
    
    const paso2 = await Promise.resolve(paso1 * 2);
    console.log("Paso 2:", paso2);
    
    const paso3 = await Promise.resolve(paso2 + 5);
    console.log("Paso 3:", paso3);
}

procesarSecuencial();

// Await con múltiples promesas paralelas
async function paralelo() {
    const [resultado1, resultado2] = await Promise.all([
        Promise.resolve(10),
        Promise.resolve(20)
    ]);
    console.log("Paralelo:", resultado1 + resultado2);
}

paralelo();

// Async siempre retorna promesa
async function retornaValor() {
    return 42;
}

retornaValor().then(valor => console.log("Valor:", valor));

/*
output
Datos obtenidos
¡Listo!
Paso 1: 10
Paso 2: 20
Paso 3: 25
Paralelo: 30
Valor: 42
*/
