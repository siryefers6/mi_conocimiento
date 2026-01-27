// Acceder a formularios

// HTML: <form id="login" name="formulario-login">
//   <input type="text" name="usuario">
//   <input type="password" name="clave">
//   <button type="submit">Entrar</button>
// </form>
// <form id="registro">
//   <input type="email" name="email">
// </form>

// Obtener todos los formularios
const formularios = document.forms;
console.log(formularios);           // HTMLCollection de formularios
console.log(formularios.length);    // Cantidad de formularios

// Acceder a formulario específico por índice
const primerFormulario = formularios[0];

// Acceder a formulario por ID
const login = document.getElementById('login');

// Acceder a formulario por nombre (atributo name)
const loginPorNombre = document.forms['formulario-login'];

// Acceder a campos dentro del formulario
const usuario = login.elements.usuario;
const clave = login.elements.clave;

// Obtener valores
console.log(usuario.value);
console.log(clave.value);

// Modificar valores
usuario.value = 'juan';
clave.value = 'password123';

// Acceder a campos por índice también
const primerCampo = login.elements[0];
console.log(primerCampo.value);

// Iterar todos los campos
for (let i = 0; i < login.elements.length; i++) {
  console.log(login.elements[i].name, login.elements[i].value);
}
