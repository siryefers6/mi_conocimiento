/**
 * Objetivo: crear una promesa básica
 * Referencia: new Promise()
 * Tipo: clase
 * Nivel: intermedio
 */

// Promise básica
const miPromesa = new Promise((resolve, reject) => {
    const exito = true;
    
    if (exito) {
        resolve("Operación exitosa");
    } else {
        reject("Error en la operación");
    }
});

miPromesa
    .then(resultado => console.log(resultado))
    .catch(error => console.log(error));

// Promise con timeout
const promesaConDelay = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Completado después de 100ms");
    }, 100);
});

promesaConDelay.then(msg => console.log(msg));

// Promise con lógica
function obtenerDatos(id) {
    return new Promise((resolve, reject) => {
        if (id > 0) {
            resolve({ id: id, nombre: "Usuario" });
        } else {
            reject("ID inválido");
        }
    });
}

obtenerDatos(5)
    .then(datos => console.log("Datos:", datos))
    .catch(error => console.log("Error:", error));

// Promise que rechaza
const promesaRechazada = new Promise((resolve, reject) => {
    reject("Algo salió mal");
});

promesaRechazada
    .then(res => console.log(res))
    .catch(err => console.log("Capturado:", err));

// Promise siempre cumplida (setTimeout)
function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

esperar(50).then(() => console.log("Espera terminada"));

/*
output
Operación exitosa
Completado después de 100ms
Datos: { id: 5, nombre: 'Usuario' }
Capturado: Algo salió mal
Espera terminada
*/
