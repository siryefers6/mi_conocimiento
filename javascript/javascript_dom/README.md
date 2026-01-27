# JavaScript - Manipulación del DOM

Referencia rápida de conceptos, métodos y patrones para manipular el Document Object Model (DOM) en JavaScript con ejemplos ejecutables.

---

## Acceso a Elementos

### Seleccionar Elementos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Seleccionar por ID | `document.getElementById()` | método | Obtener elemento por ID | [ver](examples/seleccionar_por_id__getElementById.js) |
| Seleccionar por clase | `document.getElementsByClassName()` | método | Obtener elementos por clase | [ver](examples/seleccionar_por_clase__getElementsByClassName.js) |
| Seleccionar por etiqueta | `document.getElementsByTagName()` | método | Obtener elementos por tipo | [ver](examples/seleccionar_por_etiqueta__getElementsByTagName.js) |
| Seleccionar con CSS (uno) | `document.querySelector()` | método | Primer elemento por selector CSS | [ver](examples/seleccionar_uno__querySelector.js) |
| Seleccionar con CSS (todos) | `document.querySelectorAll()` | método | Todos los elementos por selector CSS | [ver](examples/seleccionar_todos__querySelectorAll.js) |

---

## Contenido y Texto

### Modificar Contenido

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| HTML interno | `element.innerHTML` | propiedad | Modificar contenido HTML | [ver](examples/modificar_html__innerHTML.js) |
| Texto interno | `element.textContent` | propiedad | Obtener/modificar texto plano | [ver](examples/modificar_texto__textContent.js) |
| Contenido de entrada | `element.value` | propiedad | Obtener/modificar valor de input | [ver](examples/obtener_valor_input__value.js) |

---

## Atributos

### Obtener y Modificar Atributos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Obtener atributo | `element.getAttribute()` | método | Leer atributo HTML | [ver](examples/obtener_atributo__getAttribute.js) |
| Establecer atributo | `element.setAttribute()` | método | Escribir atributo HTML | [ver](examples/establecer_atributo__setAttribute.js) |
| Eliminar atributo | `element.removeAttribute()` | método | Quitar atributo | [ver](examples/eliminar_atributo__removeAttribute.js) |
| Propiedad de atributo | `element.atributo` | propiedad | Acceso directo a atributo | [ver](examples/acceder_atributo_directo__property.js) |

---

## Estilos

### Modificar Estilos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Estilos en línea | `element.style.propiedad` | propiedad | Modificar CSS directamente | [ver](examples/modificar_estilos__style.js) |
| Obtener estilos computados | `getComputedStyle()` | método | Leer estilos aplicados | [ver](examples/obtener_estilos__getComputedStyle.js) |

---

## Clases CSS

### Manipular Clases

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Lista de clases | `element.classList` | objeto | Gestor de clases | [ver](examples/acceder_clases__classList.js) |
| Agregar clase | `classList.add()` | método | Añadir una clase | [ver](examples/agregar_clase__add.js) |
| Eliminar clase | `classList.remove()` | método | Quitar una clase | [ver](examples/eliminar_clase__remove.js) |
| Alternar clase | `classList.toggle()` | método | Añadir/quitar clase | [ver](examples/alternar_clase__toggle.js) |
| Verificar clase | `classList.contains()` | método | Comprobar si tiene clase | [ver](examples/verificar_clase__contains.js) |

---

## Creación y Eliminación de Elementos

### Crear Elementos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Crear elemento | `document.createElement()` | método | Generar nuevo elemento | [ver](examples/crear_elemento__createElement.js) |
| Insertar al final | `element.appendChild()` | método | Añadir elemento hijo | [ver](examples/insertar_al_final__appendChild.js) |
| Insertar antes | `element.insertBefore()` | método | Insertar elemento antes | [ver](examples/insertar_antes__insertBefore.js) |
| Eliminar elemento | `element.removeChild()` | método | Quitar elemento hijo | [ver](examples/eliminar_elemento__removeChild.js) |
| Eliminar (método directo) | `element.remove()` | método | Quitar elemento (moderno) | [ver](examples/eliminar_directo__remove.js) |
| Reemplazar elemento | `element.replaceChild()` | método | Sustituir elemento | [ver](examples/reemplazar_elemento__replaceChild.js) |

---

## Navegación del DOM

### Recorrer el Árbol DOM

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Elemento padre | `element.parentElement` | propiedad | Obtener padre | [ver](examples/obtener_padre__parentElement.js) |
| Primer hijo | `element.firstElementChild` | propiedad | Obtener primer hijo | [ver](examples/obtener_primer_hijo__firstElementChild.js) |
| Último hijo | `element.lastElementChild` | propiedad | Obtener último hijo | [ver](examples/obtener_ultimo_hijo__lastElementChild.js) |
| Todos los hijos | `element.children` | propiedad | Obtener hijos elemento | [ver](examples/obtener_hijos__children.js) |
| Siguiente hermano | `element.nextElementSibling` | propiedad | Obtener siguiente | [ver](examples/obtener_siguiente__nextElementSibling.js) |
| Anterior hermano | `element.previousElementSibling` | propiedad | Obtener anterior | [ver](examples/obtener_anterior__previousElementSibling.js) |

---

## Eventos

### Escuchar Eventos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Escuchar evento | `addEventListener()` | método | Registrar manejador | [ver](examples/escuchar_evento__addEventListener.js) |
| Evento click | `click` | evento | Clic en elemento | [ver](examples/evento_click__click.js) |
| Evento cambio | `change` | evento | Cambio de valor | [ver](examples/evento_cambio__change.js) |
| Evento entrada | `input` | evento | Entrada de texto | [ver](examples/evento_entrada__input.js) |
| Evento envío | `submit` | evento | Envío de formulario | [ver](examples/evento_envio__submit.js) |
| Evento mouseover | `mouseover` | evento | Ratón sobre elemento | [ver](examples/evento_mouseover__mouseover.js) |
| Evento keydown | `keydown` | evento | Tecla presionada | [ver](examples/evento_keydown__keydown.js) |
| Remover escuchador | `removeEventListener()` | método | Desregistrar manejador | [ver](examples/remover_escuchador__removeEventListener.js) |
| Objeto evento | `event` | objeto | Información del evento | [ver](examples/objeto_evento__event.js) |
| Prevenir comportamiento | `event.preventDefault()` | método | Bloquear acción default | [ver](examples/prevenir_default__preventDefault.js) |

---

## Formularios

### Interacción con Formularios

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Acceder formulario | `document.forms` | propiedad | Obtener formularios | [ver](examples/acceder_formulario__forms.js) |
| Obtener valor input | `input.value` | propiedad | Leer valor de campo | [ver](examples/leer_input__value.js) |
| Validar formulario | `form.checkValidity()` | método | Comprobar validez | [ver](examples/validar_formulario__checkValidity.js) |
| Enviar formulario | `form.submit()` | método | Enviar datos | [ver](examples/enviar_formulario__submit.js) |
| Resetear formulario | `form.reset()` | método | Limpiar campos | [ver](examples/resetear_formulario__reset.js) |

---

## Información del Elemento

### Obtener Propiedades y Dimensiones

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Ancho y alto | `element.offsetWidth/Height` | propiedad | Dimensiones totales | [ver](examples/obtener_dimensiones__offsetWidth.js) |
| Posición absoluta | `element.getBoundingClientRect()` | método | Coordenadas en viewport | [ver](examples/obtener_posicion__getBoundingClientRect.js) |
| Contenedor padre | `element.offsetParent` | propiedad | Padre posicionado | [ver](examples/obtener_padre_posicionado__offsetParent.js) |

---

## Animaciones y Transiciones

### Efectos Básicos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Mostrar/ocultar | `element.style.display` | propiedad | Controlar visibilidad | [ver](examples/mostrar_ocultar__display.js) |
| Opacidad | `element.style.opacity` | propiedad | Transparencia | [ver](examples/cambiar_opacidad__opacity.js) |
| requestAnimationFrame | `requestAnimationFrame()` | función | Animar suave | [ver](examples/animar_suave__requestAnimationFrame.js) |
| setTimeout | `setTimeout()` | función | Retardar ejecución | [ver](examples/retrasar__setTimeout.js) |

---

## Carga de Archivos

### Lectura de Archivos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Input tipo archivo | `<input type="file">` | elemento | Seleccionar archivo | [ver](examples/input_archivo__file.js) |
| Acceder a archivos | `input.files` | propiedad | Obtener archivos subidos | [ver](examples/acceder_archivos__files.js) |
| FileReader | `new FileReader()` | clase | Leer contenido archivo | [ver](examples/leer_archivo__FileReader.js) |
| Leer como texto | `reader.readAsText()` | método | Cargar como texto | [ver](examples/leer_texto__readAsText.js) |
| Leer como Data URL | `reader.readAsDataURL()` | método | Convertir a Data URL | [ver](examples/leer_data_url__readAsDataURL.js) |
| Evento carga | `load` | evento | Archivo cargado | [ver](examples/evento_carga__load.js) |

---

## Utilidades DOM

### Métodos Auxiliares

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Clonar elemento | `element.cloneNode()` | método | Duplicar elemento | [ver](examples/clonar_elemento__cloneNode.js) |
| Contiene elemento | `element.contains()` | método | Verificar contenencia | [ver](examples/verificar_contenencia__contains.js) |
| Buscar selector | `element.closest()` | método | Buscar ancestro | [ver](examples/buscar_ancestro__closest.js) |
| Elemento activo | `document.activeElement` | propiedad | Elemento con foco | [ver](examples/obtener_activo__activeElement.js) |
| Establecer foco | `element.focus()` | método | Dar foco al elemento | [ver](examples/establecer_foco__focus.js) |

---
