// Cambiar opacidad (transparencia)

// HTML: <div id="elemento">Contenido</div>

const elemento = document.getElementById('elemento');

// Establecer opacidad (0 = totalmente transparente, 1 = totalmente opaco)
elemento.style.opacity = '0.5'; // 50% transparente

elemento.style.opacity = '0';   // Invisible (pero ocupa espacio)
elemento.style.opacity = '1';   // Totalmente visible

// Desvanecer gradualmente
let opacidad = 1;

function desvanecer() {
  const intervalo = setInterval(function() {
    opacidad -= 0.1;
    elemento.style.opacity = opacidad;
    
    if (opacidad <= 0) {
      clearInterval(intervalo);
    }
  }, 100);
}

// Aparecer gradualmente
let opacidad2 = 0;

function aparecer() {
  elemento.style.opacity = '0';
  const intervalo = setInterval(function() {
    opacidad2 += 0.1;
    elemento.style.opacity = opacidad2;
    
    if (opacidad2 >= 1) {
      clearInterval(intervalo);
    }
  }, 100);
}

// Usar transiciones CSS es mejor
// CSS: .elemento { transition: opacity 0.3s; }
// JavaScript: elemento.style.opacity = '0.5';

elemento.addEventListener('mouseover', function() {
  elemento.style.opacity = '0.7';
});

elemento.addEventListener('mouseout', function() {
  elemento.style.opacity = '1';
});

// Diferencia opacidad vs visibility
// opacity: 0.5 - semitransparente (eventos siguen funcionando)
// visibility: hidden - invisible (eventos no funcionan)
