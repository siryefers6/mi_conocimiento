// Crear nuevo elemento HTML

// Crear un nuevo párrafo
const parrafo = document.createElement('p');
parrafo.textContent = 'Este es un nuevo párrafo';

// Crear un nuevo div
const div = document.createElement('div');
div.innerHTML = '<h2>Nuevo contenido</h2>';

// Crear un nuevo botón
const boton = document.createElement('button');
boton.textContent = 'Presionar';
boton.className = 'boton-primario';

// El elemento creado aún no está en el DOM
// Necesita ser insertado

// Crear un listado
const lista = document.createElement('ul');
const item1 = document.createElement('li');
item1.textContent = 'Elemento 1';
const item2 = document.createElement('li');
item2.textContent = 'Elemento 2';

// Agregar ítems a la lista
lista.appendChild(item1);
lista.appendChild(item2);

// Crear elemento con atributos
const enlace = document.createElement('a');
enlace.href = 'https://ejemplo.com';
enlace.textContent = 'Ir a ejemplo';
enlace.setAttribute('target', '_blank');

// Crear imagen
const imagen = document.createElement('img');
imagen.src = 'foto.jpg';
imagen.alt = 'Foto';
imagen.className = 'imagen-perfil';
