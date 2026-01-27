/**
 * Objetivo: encadenar promesas
 * Referencia: promise.then()
 * Tipo: método
 * Nivel: intermedio
 */

// Then básico
const promesa = new Promise(resolve => {
    resolve(5);
});

promesa
    .then(resultado => {
        console.log("Primer then:", resultado);
        return resultado * 2;
    })
    .then(resultado => {
        console.log("Segundo then:", resultado);
        return resultado + 10;
    })
    .then(resultado => {
        console.log("Tercer then:", resultado);
    });

// Then con funciones separadas
function paso1(valor) {
    return valor * 2;
}

function paso2(valor) {
    return valor + 10;
}

function paso3(valor) {
    return valor * 3;
}

Promise.resolve(5)
    .then(paso1)
    .then(paso2)
    .then(paso3)
    .then(resultado => console.log("Resultado final:", resultado));

// Then con promesas
function obtenerUsuario(id) {
    return Promise.resolve({ id: id, nombre: "Juan" });
}

function obtenerPosts(usuario) {
    return Promise.resolve([
        { id: 1, titulo: "Post 1", usuario_id: usuario.id },
        { id: 2, titulo: "Post 2", usuario_id: usuario.id }
    ]);
}

obtenerUsuario(1)
    .then(usuario => {
        console.log("Usuario:", usuario.nombre);
        return obtenerPosts(usuario);
    })
    .then(posts => {
        console.log("Posts encontrados:", posts.length);
    });

/*
output
Primer then: 5
Segundo then: 10
Tercer then: 20
Resultado final: 60
Usuario: Juan
Posts encontrados: 2
*/
