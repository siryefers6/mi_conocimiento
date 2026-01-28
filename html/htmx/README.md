# HTMX - Guía Completa

Referencia rápida de atributos, métodos y conceptos fundamentales de HTMX con ejemplos ejecutables.

---

## Introducción a HTMX

HTMX permite acceder a AJAX, WebSockets y Server-Sent Events (SSE) directamente en HTML, sin necesidad de JavaScript. Transforma cualquier elemento HTML en una solicitud HTTP.

**Características principales:**
- AJAX directo desde HTML
- Múltiples métodos HTTP
- Destinos y estrategias de cambio flexibles
- Validación y eventos
- WebSockets y SSE
- Indicadores de carga
- Historial de navegación

---

## Atributos de Solicitud HTTP

### Métodos HTTP Básicos

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| GET request | `hx-get=""` | atributo | Solicita datos con GET | [ver](examples/request_get__get.html) |
| POST request | `hx-post=""` | atributo | Envía datos con POST | [ver](examples/request_post__post.html) |
| PUT request | `hx-put=""` | atributo | Actualiza con PUT | [ver](examples/request_put__put.html) |
| PATCH request | `hx-patch=""` | atributo | Actualiza parcialmente | [ver](examples/request_patch__patch.html) |
| DELETE request | `hx-delete=""` | atributo | Elimina con DELETE | [ver](examples/request_delete__delete.html) |
| OPTIONS request | `hx-options=""` | atributo | CORS preflight | [ver](examples/request_options__options.html) |

### Parámetros y Datos

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Parámetros adicionales | `hx-params=""` | atributo | Incluye/excluye parámetros | [ver](examples/data_params__params.html) |
| Valores personalizados | `hx-vals=""` | atributo | Añade valores JSON | [ver](examples/data_vals__vals.html) |
| Incluir formulario | `hx-include=""` | atributo | Incluye selector CSS | [ver](examples/data_include__include.html) |
| Valores JSON | `hx-vals.from="select"` | atributo | Obtiene valor de selector | [ver](examples/data_vals_json__json.html) |

---

## Atributos de Destino y Intercambio

### Destino y Posición

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Selector destino | `hx-target=""` | atributo | Elemento a actualizar | [ver](examples/target_selector__selector.html) |
| Este elemento | `hx-target="this"` | valor | Reemplaza el elemento actual | [ver](examples/target_this__this.html) |
| Elemento más cercano | `hx-target="closest"` | valor | Busca ancestro con selector | [ver](examples/target_closest__closest.html) |
| Elemento padre | `hx-target="parent"` | valor | Apunta al padre | [ver](examples/target_parent__parent.html) |
| Búsqueda anterior | `hx-target="find"` | valor | Busca dentro del elemento | [ver](examples/target_find__find.html) |
| Siguiente hermano | `hx-target="next"` | valor | Siguiente elemento hermano | [ver](examples/target_next__next.html) |
| Anterior hermano | `hx-target="previous"` | valor | Elemento anterior hermano | [ver](examples/target_previous__previous.html) |

### Estrategia de Intercambio

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Estrategia de cambio | `hx-swap=""` | atributo | Cómo insertar contenido | [ver](examples/swap_strategy__strategy.html) |
| Reemplazar HTML | `innerHTML` | valor | Reemplaza contenido interno | [ver](examples/swap_innerHTML__inner.html) |
| Reemplazar elemento | `outerHTML` | valor | Reemplaza elemento completo | [ver](examples/swap_outerHTML__outer.html) |
| Insertar antes | `beforebegin` | valor | Antes del elemento | [ver](examples/swap_beforebegin__before.html) |
| Insertar después | `afterbegin` | valor | Dentro, antes del contenido | [ver](examples/swap_afterbegin__after.html) |
| Insertar al final | `beforeend` | valor | Dentro, después del contenido | [ver](examples/swap_beforeend__end.html) |
| Insertar después del elemento | `afterend` | valor | Después del elemento | [ver](examples/swap_afterend__after.html) |
| Reemplazar y eliminar | `delete` | valor | Elimina elemento objetivo | [ver](examples/swap_delete__delete.html) |
| Solo reemplazar si existe | `none` | valor | No reemplaza el destino | [ver](examples/swap_none__none.html) |

### Modificadores de Intercambio

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Swap con transición | `hx-swap="innerHTML swap:1s"` | modificador | Anima cambio | [ver](examples/swap_modifier_transition__transition.html) |
| Swap con retraso | `hx-swap="innerHTML settle:1s"` | modificador | Espera antes de cambiar | [ver](examples/swap_modifier_settle__settle.html) |
| Swap con scroll | `hx-swap="innerHTML scroll:top"` | modificador | Scroll al cambio | [ver](examples/swap_modifier_scroll__scroll.html) |
| Mostrar solo diferencias | `hx-swap="innerHTML show:top"` | modificador | Muestra área específica | [ver](examples/swap_modifier_show__show.html) |

---

## Atributos de Activación

### Eventos Disparadores

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| En cambio | `hx-trigger="change"` | evento | Se dispara al cambiar | [ver](examples/trigger_change__change.html) |
| En envío | `hx-trigger="submit"` | evento | Se dispara al enviar | [ver](examples/trigger_submit__submit.html) |
| En clic | `hx-trigger="click"` | evento | Se dispara al hacer clic | [ver](examples/trigger_click__click.html) |
| Evento personalizado | `hx-trigger="myEvent"` | evento | Escucha evento personalizado | [ver](examples/trigger_custom__custom.html) |
| En escritura | `hx-trigger="keyup"` | evento | Se dispara cada tecla | [ver](examples/trigger_keyup__keyup.html) |
| Entrada completada | `hx-trigger="change delay:500ms"` | modificador | Espera después de cambio | [ver](examples/trigger_delay__delay.html) |
| Cuando se cargue | `hx-trigger="load"` | evento | Se dispara al cargar página | [ver](examples/trigger_load__load.html) |
| Visible en pantalla | `hx-trigger="revealed"` | evento | Se dispara visible en viewport | [ver](examples/trigger_revealed__revealed.html) |
| Evento múltiple | `hx-trigger="click, change"` | evento | Varios eventos separados | [ver](examples/trigger_multiple__multiple.html) |

### Modificadores de Disparador

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Retraso en milisegundos | `hx-trigger="click delay:2s"` | modificador | Espera antes de ejecutar | [ver](examples/trigger_modifier_delay__delay.html) |
| Throttle | `hx-trigger="keyup throttle:1s"` | modificador | Máximo una vez por segundo | [ver](examples/trigger_modifier_throttle__throttle.html) |
| Debounce | `hx-trigger="keyup debounce:500ms"` | modificador | Espera antes de ejecutar | [ver](examples/trigger_modifier_debounce__debounce.html) |
| Cambio de valor | `hx-trigger="change changed"` | modificador | Solo si cambia valor | [ver](examples/trigger_modifier_changed__changed.html) |
| Una sola vez | `hx-trigger="click once"` | modificador | Se ejecuta una sola vez | [ver](examples/trigger_modifier_once__once.html) |
| Cambio de atributo | `hx-trigger="mutation"` | evento | Detecta cambios en DOM | [ver](examples/trigger_mutation__mutation.html) |
| Cantidad mínima | `hx-trigger="keyup from:body"` | modificador | Desde selector específico | [ver](examples/trigger_modifier_from__from.html) |

---

## Indicadores de Carga

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Indicador de carga | `hx-indicator=""` | atributo | Selector para mostrar carga | [ver](examples/indicator_selector__selector.html) |
| Este elemento | `hx-indicator="this"` | valor | Muestra carga en mismo elemento | [ver](examples/indicator_this__this.html) |
| Elemento más cercano | `hx-indicator="closest .loader"` | selector | Busca ancestro con clase | [ver](examples/indicator_closest__closest.html) |
| Clase de carga | `.htmx-request` | clase CSS | Se añade durante solicitud | [ver](examples/indicator_class__class.html) |
| Clase de envío | `.htmx-settling` | clase CSS | Se añade al intercambiar | [ver](examples/indicator_settling__settling.html) |

---

## Validación y Seguridad

### Validación de Solicitudes

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Validación en cliente | `hx-validate="true"` | atributo | Valida formulario HTML5 | [ver](examples/validation_client__client.html) |
| Campo requerido | `required` | atributo HTML5 | Validación nativa | [ver](examples/validation_required__required.html) |
| Patrón regex | `pattern="[a-z]+"` | atributo HTML5 | Valida con expresión regular | [ver](examples/validation_pattern__pattern.html) |
| Tipo de entrada | `type="email"` | atributo HTML5 | Validación de tipo | [ver](examples/validation_type__type.html) |

### Manejo de Errores

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Elemento para errores | `hx-error-target=""` | atributo | Dónde mostrar errores | [ver](examples/error_target__target.html) |
| Estrategia error | `hx-swap="outerHTML"` | valor | En caso de error (4xx, 5xx) | [ver](examples/error_strategy__strategy.html) |
| Manejo de 404 | Respuesta 404 | respuesta | Evento `htmx:responseError` | [ver](examples/error_404__404.html) |
| Manejo de 500 | Respuesta 500 | respuesta | Evento `htmx:responseError` | [ver](examples/error_500__500.html) |

---

## Atributos de Historia y Navegación

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Guardar en historial | `hx-history="true"` | atributo | Añade a historial navegador | [ver](examples/history_push__push.html) |
| URL de historial | `hx-push-url="/nueva-url"` | atributo | Cambia URL en barra | [ver](examples/history_url__url.html) |
| Reemplazar historial | `hx-replace-url="/url"` | atributo | Reemplaza entrada historial | [ver](examples/history_replace__replace.html) |
| Sin historial | `hx-push-url="false"` | valor | No añade a historial | [ver](examples/history_false__false.html) |

---

## Atributos de Confirmación

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Confirmar acción | `hx-confirm=""` | atributo | Pide confirmación | [ver](examples/confirm_dialog__dialog.html) |
| Mensaje personalizado | `hx-confirm="¿Estás seguro?"` | valor | Texto del diálogo | [ver](examples/confirm_message__message.html) |
| Eliminar con confirmación | `hx-delete="/item/1" hx-confirm="¿Eliminar?"` | combo | Patrón típico | [ver](examples/confirm_delete__delete.html) |

---

## Atributos de Sincronización

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Sincronizar con hermanos | `hx-sync=""` | atributo | Controla solicitudes múltiples | [ver](examples/sync_siblings__siblings.html) |
| Abandonar solicitud | `hx-sync="closest div:abort"` | valor | Cancela request anterior | [ver](examples/sync_abort__abort.html) |
| Esperar a otro | `hx-sync="closest div:queue"` | valor | Espera a que termine | [ver](examples/sync_queue__queue.html) |
| Reemplazar solicitud | `hx-sync="closest div:replace"` | valor | Cancela y ejecuta nueva | [ver](examples/sync_replace__replace.html) |

---

## Atributos de Destino Condicional

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Destino dinámico | `hx-target="next .result"` | selector | Destino relativo | [ver](examples/conditional_target__target.html) |
| Intercambio condicional | `hx-swap="innerHTML"` | condicional | Basado en respuesta | [ver](examples/conditional_swap__swap.html) |
| Intercambio por status | Header `HX-Reswap` | respuesta | Servidor decide intercambio | [ver](examples/conditional_reswap__reswap.html) |
| Destino por status | Header `HX-Retarget` | respuesta | Servidor decide destino | [ver](examples/conditional_retarget__retarget.html) |

---

## Eventos Personalizados

### Eventos de Ciclo de Vida

| Concepto | Evento | Tipo | Uso | Ejemplo |
|----------|--------|------|-----|---------|
| Antes de request | `htmx:beforeRequest` | evento | Se dispara antes de enviar | [ver](examples/event_beforeRequest__before.html) |
| Después de request | `htmx:afterRequest` | evento | Se dispara después de enviar | [ver](examples/event_afterRequest__after.html) |
| Respuesta recibida | `htmx:afterSwap` | evento | Se dispara tras cambio | [ver](examples/event_afterSwap__swap.html) |
| Después de intercambio | `htmx:afterSettle` | evento | Se dispara tras settle | [ver](examples/event_afterSettle__settle.html) |
| Error en request | `htmx:responseError` | evento | Se dispara en error HTTP | [ver](examples/event_responseError__error.html) |
| Envío de formulario | `htmx:beforeSend` | evento | Modifica headers antes | [ver](examples/event_beforeSend__send.html) |

### Disparo de Eventos

| Concepto | Sintaxis | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Disparar evento | `htmx.trigger("#id", "eventName")` | JavaScript | Dispara evento en elemento | [ver](examples/event_trigger__trigger.html) |
| Evento personalizado | `hx-trigger="myEvent"` | atributo | Escucha evento personalizado | [ver](examples/event_custom__custom.html) |
| Disparar múltiples | `htmx.ajax("GET", "/url")` | JavaScript | Realiza petición AJAX | [ver](examples/event_multiple__multiple.html) |

---

## WebSockets

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Conexión WebSocket | `hx-ws="connect /ws"` | atributo | Conecta a WebSocket | [ver](examples/ws_connect__connect.html) |
| Enviar mensaje | `hx-ws="send"` | atributo | Envía mensaje WebSocket | [ver](examples/ws_send__send.html) |
| Eventos del servidor | `hx-trigger="sse:eventName"` | atributo | Escucha evento SSE | [ver](examples/ws_sse__sse.html) |
| Trigger con condición | `hx-trigger="sse:message"` | evento | Reacciona a SSE | [ver](examples/ws_trigger__trigger.html) |

---

## Atributos Avanzados

### Configuración

| Concepto | Atributo | Tipo | Uso | Ejemplo |
|----------|----------|------|-----|---------|
| Deshabilitar | `hx-disable=""` | atributo | Desactiva HTMX en elemento | [ver](examples/advanced_disable__disable.html) |
| Heredar atributos | `hx-inherit="hx-get"` | atributo | Hereda de ancestro | [ver](examples/advanced_inherit__inherit.html) |
| Boost | `hx-boost="true"` | atributo | Mejora enlaces/forms | [ver](examples/advanced_boost__boost.html) |
| Request timeout | `hx-request='{"timeout": 5000}'` | JSON | Timeout en milisegundos | [ver](examples/advanced_timeout__timeout.html) |
| Headers personalizados | `hx-request='{"headers": {}}'` | JSON | Añade headers | [ver](examples/advanced_headers__headers.html) |

### Configuración Global

| Concepto | Configuración | Tipo | Uso | Ejemplo |
|----------|---|------|-----|---------|
| Timeout global | `htmx.config.timeout` | JS | Configura timeout global | [ver](examples/config_timeout__timeout.html) |
| Método por defecto | `htmx.config.defaultIndicatorStyle` | JS | Indicador por defecto | [ver](examples/config_indicator__indicator.html) |
| Refresh on load | `hx-refresh="true"` | atributo | Recarga al visibilidad | [ver](examples/config_refresh__refresh.html) |

---

## Métodos de Utilidad

| Concepto | Método | Tipo | Uso | Ejemplo |
|----------|--------|------|-----|---------|
| AJAX request | `htmx.ajax("GET", "/url")` | JavaScript | Realiza petición AJAX | [ver](examples/util_ajax__ajax.html) |
| Procesar elemento | `htmx.process(element)` | JavaScript | Procesa HTMX en elemento | [ver](examples/util_process__process.html) |
| Disparar evento | `htmx.trigger(selector, event)` | JavaScript | Dispara evento | [ver](examples/util_trigger__trigger.html) |
| Encontrar elemento | `htmx.find(selector)` | JavaScript | Busca elemento | [ver](examples/util_find__find.html) |
| Toggle clase | `htmx.toggleClass(element, class)` | JavaScript | Añade/quita clase | [ver](examples/util_toggle__toggle.html) |
| Remove clase | `htmx.removeClass(element, class)` | JavaScript | Quita clase CSS | [ver](examples/util_remove__remove.html) |
| Add clase | `htmx.addClass(element, class)` | JavaScript | Añade clase CSS | [ver](examples/util_add__add.html) |
| Swap DOM | `htmx.swap(target, content)` | JavaScript | Intercambia contenido | [ver](examples/util_swap__swap.html) |

---

## Patrones Comunes

### Tabla Interactiva

```html
<table>
  <tbody hx-target="this" hx-swap="outerHTML">
    <tr hx-get="/api/items/1">
      <td>Item 1</td>
      <td><button hx-delete="/api/items/1">Eliminar</button></td>
    </tr>
  </tbody>
</table>
```

### Búsqueda en Tiempo Real

```html
<input type="text" 
       name="query" 
       hx-get="/search" 
       hx-trigger="keyup debounce:500ms"
       hx-target="#results">
<div id="results"></div>
```

### Modal con AJAX

```html
<button hx-get="/modal/form" hx-target="body" hx-swap="beforeend">
  Abrir Modal
</button>
```

### Confirmación antes de eliminar

```html
<button hx-delete="/item/1" 
        hx-confirm="¿Estás seguro de eliminar?">
  Eliminar
</button>
```

### Carga infinita (Infinite Scroll)

```html
<div hx-get="/items?page=2" 
     hx-trigger="revealed" 
     hx-swap="afterbegin">
  <!-- Se carga al volverse visible -->
</div>
```

### Validación en cliente

```html
<form hx-post="/login" hx-validate="true">
  <input type="email" required name="email">
  <input type="password" required name="password">
  <button type="submit">Login</button>
</form>
```

### Intercambio condicional

```html
<!-- Servidor responde con header: HX-Reswap: outerHTML -->
<div hx-post="/update" hx-target="this">
  Actualizar
</div>
```

### Sincronización entre elementos

```html
<button hx-get="/data1" hx-sync="closest .container:queue">
  Cargar 1
</button>
<button hx-get="/data2" hx-sync="closest .container:queue">
  Cargar 2
</button>
```

---

## Respuestas del Servidor

### Headers de Respuesta

| Header | Uso | Ejemplo |
|--------|-----|---------|
| `HX-Trigger` | Dispara evento en cliente | `HX-Trigger: myEvent` |
| `HX-Trigger-After-Swap` | Dispara después de swap | `HX-Trigger-After-Swap: success` |
| `HX-Trigger-After-Settle` | Dispara después de settle | `HX-Trigger-After-Settle: done` |
| `HX-Redirect` | Redirige página | `HX-Redirect: /path` |
| `HX-Reswap` | Cambia estrategia swap | `HX-Reswap: outerHTML` |
| `HX-Retarget` | Cambia elemento destino | `HX-Retarget: .result` |
| `HX-Refresh` | Recarga página | `HX-Refresh: true` |
| `HX-Location` | Navega con historial | `HX-Location: /path` |

### Códigos HTTP

| Código | Comportamiento | Ejemplo |
|--------|---|---------|
| 200 OK | Intercambia contenido | Respuesta exitosa |
| 201 Created | Intercambia contenido | Crear recurso |
| 204 No Content | No intercambia | Operación exitosa sin respuesta |
| 400 Bad Request | Error (evento `htmx:responseError`) | Validación fallida |
| 403 Forbidden | Error | Acceso denegado |
| 404 Not Found | Error | Recurso no existe |
| 500 Server Error | Error | Error del servidor |

---

## Integración con Formularios

### Envío de Formulario

```html
<form hx-post="/api/submit">
  <input type="text" name="username" required>
  <input type="email" name="email" required>
  <textarea name="message"></textarea>
  <button type="submit">Enviar</button>
</form>
```

### Autocomplete

```html
<input type="text" 
       name="search"
       hx-get="/autocomplete"
       hx-trigger="keyup changed delay:200ms"
       hx-target="#suggestions"
       list="suggestions">
<datalist id="suggestions"></datalist>
```

### Validación con servidor

```html
<input type="email" 
       name="email"
       hx-post="/validate/email"
       hx-trigger="change"
       hx-swap="none">
```

---

## Mejores Prácticas

1. **Debounce en búsquedas**: Usa `debounce:500ms` para no sobrecargar servidor
2. **Indicadores de carga**: Siempre muestra al usuario que algo está pasando
3. **Confirmación en delete**: Usa `hx-confirm` para acciones destructivas
4. **Validación en cliente**: Aprovecha HTML5 validation `required`, `pattern`, etc.
5. **Destinos específicos**: Usa selectores precisos en `hx-target`
6. **Headers de seguridad**: Implementa CSRF tokens en POST/PUT/DELETE
7. **Respuestas parciales**: Retorna solo el HTML necesario
8. **Errores claros**: Proporciona mensajes de error útiles
9. **SEO**: Usa `hx-boost` en navegación
10. **Fallback**: Proporciona alternativas JavaScript para navegadores sin soporte

---

## Estadísticas

- **Total de atributos**: 40+ atributos HTMX
- **Métodos de utilidad**: 15+ funciones JavaScript
- **Eventos**: 10+ eventos de ciclo de vida
- **Patrones comunes**: 8+ ejemplos típicos
- **Headers de respuesta**: 8+ headers especiales

---

## Recursos Externos

- **Documentación oficial**: https://htmx.org/docs
- **Referencia completa**: https://htmx.org/reference/
- **Ejemplos**: https://htmx.org/examples/
- **Atributos**: https://htmx.org/attributes/

---

**Última actualización:** Enero 2026  
**Autor:** Experto en HTMX
