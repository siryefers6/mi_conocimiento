/**
 * Objetivo: capturar y manejar excepciones
 * Referencia: try...catch
 * Tipo: keyword
 * Nivel: intermedio
 */

// Try/catch básico
try {
    throw new Error("Error intencional");
} catch (error) {
    console.log("Error capturado:", error.message);
}

// Try/catch con código válido
try {
    const resultado = 10 + 5;
    console.log("Resultado:", resultado);
} catch (error) {
    console.log("No hay error");
}

// Try/catch con división
try {
    const a = 10;
    const b = 0;
    if (b === 0) {
        throw new Error("No se puede dividir entre cero");
    }
    console.log(a / b);
} catch (error) {
    console.log("Error:", error.message);
}

// Try/catch/finally
try {
    console.log("Try");
    throw new Error("Error");
} catch (error) {
    console.log("Catch:", error.message);
} finally {
    console.log("Finally ejecutado");
}

// Try/catch con validación
try {
    const json = '{"nombre": "Juan"';
    const obj = JSON.parse(json);
} catch (error) {
    console.log("Error de parsing:", error.message);
}

// Try/catch anidado
try {
    try {
        throw new Error("Error interno");
    } catch (e) {
        console.log("Capturado en try interno:", e.message);
        throw new Error("Error propagado");
    }
} catch (error) {
    console.log("Capturado en try externo:", error.message);
}

/*
output
Error capturado: Error intencional
Resultado: 15
Error: No se puede dividir entre cero
Try
Catch: Error
Finally ejecutado
Error de parsing: Unexpected end of JSON input
Capturado en try interno: Error interno
Capturado en try externo: Error propagado
*/
