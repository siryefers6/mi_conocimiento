/**
 * Objetivo: extraer propiedades en parámetros de función
 * Referencia: ({a, b}) => {}
 * Tipo: patrón
 * Nivel: intermedio
 */

// Desestructuración de objeto en parámetro
function mostrarPersona({ nombre, edad }) {
    console.log(`${nombre} tiene ${edad} años`);
}

mostrarPersona({ nombre: "Juan", edad: 30 });

// Desestructuración parcial
function saludar({ nombre, ciudad }) {
    console.log(`Hola ${nombre} de ${ciudad}`);
}

saludar({ nombre: "Elena", edad: 28, ciudad: "Madrid" });

// Desestructuración con valor por defecto
function crear({ tipo = "básico", activo = false }) {
    console.log(`Tipo: ${tipo}, Activo: ${activo}`);
}

crear({ tipo: "premium" });

// Desestructuración de array en parámetro
function sumarDos([a, b]) {
    return a + b;
}

console.log(sumarDos([10, 20]));

// Desestructuración anidada
function mostrarDatos({ usuario: { nombre, email } }) {
    console.log(`Usuario: ${nombre}, Email: ${email}`);
}

mostrarDatos({
    usuario: {
        nombre: "Marco",
        email: "marco@example.com"
    }
});

// Arrow function con desestructuración
const procesar = ({ id, valor }) => valor * 2;
console.log(procesar({ id: 1, valor: 10 }));

// Desestructuración con rest
function listar({ nombre, ...resto }) {
    console.log(`Nombre: ${nombre}`);
    console.log("Resto:", resto);
}

listar({ nombre: "Ana", edad: 25, ciudad: "Barcelona" });

/*
output
Juan tiene 30 años
Hola Elena de Madrid
Tipo: premium, Activo: false
30
Usuario: Marco, Email: marco@example.com
20
Nombre: Ana
Resto: { edad: 25, ciudad: 'Barcelona' }
*/
