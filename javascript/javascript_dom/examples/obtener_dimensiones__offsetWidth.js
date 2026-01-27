// Obtener dimensiones del elemento

// HTML: <div id="caja">Contenido</div>
// CSS: #caja { width: 200px; height: 100px; padding: 10px; }

const caja = document.getElementById('caja');

// offsetWidth: ancho total (incluye border y padding)
console.log(caja.offsetWidth);  // 220 (200 + 10*2 padding)

// offsetHeight: alto total (incluye border y padding)
console.log(caja.offsetHeight); // 120 (100 + 10*2 padding)

// clientWidth: ancho sin border (con padding)
console.log(caja.clientWidth);  // 220 (200 + 10*2 padding)

// clientHeight: alto sin border (con padding)
console.log(caja.clientHeight); // 120 (100 + 10*2 padding)

// scrollWidth: ancho del contenido (si hay scroll)
console.log(caja.scrollWidth);

// scrollHeight: alto del contenido (si hay scroll)
console.log(caja.scrollHeight);

// Diferencia entre offsetWidth y clientWidth:
// offsetWidth incluye border
// clientWidth no incluye border

// Obtener posición relativa al padre
console.log(caja.offsetLeft);   // X relativa al padre
console.log(caja.offsetTop);    // Y relativa al padre

// Posición relativa a toda la página
const rect = caja.getBoundingClientRect();
console.log(rect.width);        // Ancho
console.log(rect.height);       // Alto
console.log(rect.top);          // Distancia desde arriba de la ventana
console.log(rect.left);         // Distancia desde la izquierda
