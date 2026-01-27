/**
 * Objetivo: capturar errores de promesas
 * Referencia: promise.catch()
 * Tipo: método
 * Nivel: intermedio
 */

// Catch básico
const promesaFallida = new Promise((resolve, reject) => {
    reject("Error detectado");
});

promesaFallida
    .then(resultado => console.log(resultado))
    .catch(error => console.log("Capturado:", error));

// Catch en cadena de then
Promise.resolve(10)
    .then(n => {
        if (n < 5) {
            throw new Error("Número muy pequeño");
        }
        return n * 2;
    })
    .then(resultado => console.log("Resultado:", resultado))
    .catch(error => console.log("Error:", error.message));

// Catch captura errores de cualquier then anterior
Promise.resolve(3)
    .then(n => {
        if (n < 5) {
            throw new Error("Número inválido");
        }
        return n * 2;
    })
    .then(resultado => console.log("Resultado:", resultado))
    .catch(error => console.log("Error capturado:", error.message));

// Catch con recuperación
Promise.reject("Primer error")
    .catch(error => {
        console.log("Primer catch:", error);
        return "Recuperado";
    })
    .then(resultado => console.log("Continuando:", resultado));

// Catch con finally
Promise.resolve("Datos")
    .then(datos => console.log(datos))
    .catch(error => console.log("Error:", error))
    .finally(() => console.log("Finalmente"));

/*
output
Capturado: Error detectado
Resultado: 20
Error: Número inválido
Primer catch: Primer error
Continuando: Recuperado
Datos
Finalmente
*/
