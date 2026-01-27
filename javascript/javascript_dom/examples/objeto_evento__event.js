// Objeto evento (información del evento)

// HTML: <button id="boton">Presionar</button>

const boton = document.getElementById('boton');

boton.addEventListener('click', function(evento) {
  // evento es un objeto que contiene información del evento
  
  console.log(evento);                // Objeto Event
  console.log(evento.type);           // "click"
  console.log(evento.target);         // El elemento que disparó el evento
  console.log(evento.currentTarget);  // El elemento con el escuchador
  console.log(evento.timeStamp);      // Cuándo sucedió
});

// Propiedades útiles del evento
documento.addEventListener('click', function(evento) {
  // Información de mouse
  console.log(evento.clientX);   // X en el viewport
  console.log(evento.clientY);   // Y en el viewport
  console.log(evento.pageX);     // X en la página
  console.log(evento.pageY);     // Y en la página
  
  // Información de teclas (en eventos de teclado)
  // console.log(evento.key);       // Carácter de la tecla
  // console.log(evento.code);      // Código de la tecla
  // console.log(evento.ctrlKey);   // ¿Ctrl presionado?
  // console.log(evento.shiftKey);  // ¿Mayús presionado?
  // console.log(evento.altKey);    // ¿Alt presionado?
});

// Métodos útiles del evento
boton.addEventListener('click', function(evento) {
  // Detener propagación (no suba a elementos padres)
  evento.stopPropagation();
  
  // Prevenir comportamiento por defecto
  evento.preventDefault();
});

// event.target vs event.currentTarget
const contenedor = document.getElementById('contenedor');

contenedor.addEventListener('click', function(evento) {
  console.log(evento.target);        // El elemento que hicieron clic
  console.log(evento.currentTarget);  // El elemento con el escuchador
});
