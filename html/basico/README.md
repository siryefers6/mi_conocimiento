# HTML - Básico

Referencia rápida de elementos, atributos y conceptos fundamentales de HTML5 con ejemplos ejecutables.

---

## Estructura de Documento

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Declaración de tipo | `<!DOCTYPE>` | declaración | Indica versión HTML5 | [ver](examples/estructura_documento__doctype.html) |
| Elemento raíz | `<html>` | elemento | Contenedor principal | [ver](examples/estructura_documento__doctype.html) |
| Encabezado de documento | `<head>` | elemento | Metadatos y configuración | [ver](examples/estructura_documento__doctype.html) |
| Cuerpo del documento | `<body>` | elemento | Contenido visible | [ver](examples/estructura_documento__doctype.html) |
| Título de página | `<title>` | elemento | Nombre en pestaña y SEO | [ver](examples/estructura_documento__doctype.html) |
| Metadatos del documento | `<meta>` | elemento | Configuración de página | [ver](examples/metadatos_basicos__meta.html) |
| Conjunto de caracteres | `<meta charset>` | atributo | Codificación UTF-8 | [ver](examples/metadatos_basicos__meta.html) |
| Viewport responsivo | `<meta viewport>` | atributo | Configuración móvil | [ver](examples/metadatos_basicos__meta.html) |

---

## Encabezados y Secciones

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Encabezado nivel 1 | `<h1>` | elemento | Título principal (único) | [ver](examples/encabezados__h1.html) |
| Encabezado nivel 2 | `<h2>` | elemento | Subtítulo | [ver](examples/encabezados__h2.html) |
| Encabezado nivel 3 | `<h3>` | elemento | Subsección | [ver](examples/encabezados__h3.html) |
| Encabezado nivel 4 | `<h4>` | elemento | Detalle menor | [ver](examples/encabezados__h4.html) |
| Encabezado nivel 5 | `<h5>` | elemento | Nivel 5 (raro) | [ver](examples/encabezados__h5.html) |
| Encabezado nivel 6 | `<h6>` | elemento | Nivel 6 (mínimo) | [ver](examples/encabezados__h6.html) |
| Párrafo | `<p>` | elemento | Bloque de texto | [ver](examples/parrafo__p.html) |

---

## Texto y Formato

### Énfasis y Semántica

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Énfasis fuerte | `<strong>` | elemento | Importancia semántica | [ver](examples/formato_strong__strong.html) |
| Énfasis | `<em>` | elemento | Énfasis semántico | [ver](examples/formato_em__em.html) |
| Negrita (presentación) | `<b>` | elemento | Negrita sin semántica | [ver](examples/formato_b__b.html) |
| Cursiva (presentación) | `<i>` | elemento | Cursiva sin semántica | [ver](examples/formato_i__i.html) |
| Tachado | `<s>` | elemento | Texto irrelevante | [ver](examples/formato_s__s.html) |
| Texto pequeño | `<small>` | elemento | Comentarios, letras pequeñas | [ver](examples/formato_small__small.html) |
| Subíndice | `<sub>` | elemento | H₂O, fórmulas químicas | [ver](examples/formato_sub__sub.html) |
| Superíndice | `<sup>` | elemento | Exponentes, marcas registradas | [ver](examples/formato_sup__sup.html) |
| Código inline | `<code>` | elemento | Código en línea | [ver](examples/formato_code__code.html) |
| Código preformateado | `<pre>` | elemento | Mantiene espacios y saltos | [ver](examples/formato_pre__pre.html) |
| Cita | `<q>` | elemento | Cita corta inline | [ver](examples/formato_q__q.html) |
| Cita de bloque | `<blockquote>` | elemento | Cita extensa | [ver](examples/formato_blockquote__blockquote.html) |
| Marca/Resaltado | `<mark>` | elemento | Texto resaltado | [ver](examples/formato_mark__mark.html) |

### Saltos y Separadores

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Salto de línea | `<br>` | elemento | Fuerza salto de línea | [ver](examples/salto_br__br.html) |
| Separador horizontal | `<hr>` | elemento | Divide temáticamente | [ver](examples/separador_hr__hr.html) |

---

## Listas

### Listas No Ordenadas

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Lista no ordenada | `<ul>` | elemento | Listas con viñetas | [ver](examples/lista_ul__ul.html) |
| Elemento de lista | `<li>` | elemento | Elemento dentro de lista | [ver](examples/lista_ul__ul.html) |

### Listas Ordenadas

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Lista ordenada | `<ol>` | elemento | Listas numeradas | [ver](examples/lista_ol__ol.html) |

### Listas de Definición

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Lista de definición | `<dl>` | elemento | Pares término-definición | [ver](examples/lista_dl__dl.html) |
| Término | `<dt>` | elemento | Término a definir | [ver](examples/lista_dl__dl.html) |
| Definición | `<dd>` | elemento | Definición del término | [ver](examples/lista_dl__dl.html) |

---

## Enlaces

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Hipervínculo | `<a>` | elemento | Enlace a otra página | [ver](examples/enlace_a__a.html) |
| Atributo href | `href=""` | atributo | Destino del enlace | [ver](examples/enlace_a__a.html) |
| Enlace a ancla | `href="#id"` | atributo | Saltar a sección | [ver](examples/enlace_ancla__anchor.html) |
| Abrir en pestaña nueva | `target="_blank"` | atributo | Nueva pestaña/ventana | [ver](examples/enlace_target__target.html) |
| Enlace de descarga | `download` | atributo | Descargar archivo | [ver](examples/enlace_download__download.html) |
| Enlace de correo | `href="mailto:"` | atributo | Enviar email | [ver](examples/enlace_mailto__mailto.html) |
| Enlace de teléfono | `href="tel:"` | atributo | Llamada telefónica | [ver](examples/enlace_tel__tel.html) |

---

## Imágenes

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Imagen | `<img>` | elemento | Insertar imagen | [ver](examples/imagen_img__img.html) |
| Ruta de imagen | `src=""` | atributo | URL de la imagen | [ver](examples/imagen_img__img.html) |
| Texto alternativo | `alt=""` | atributo | Descripción para SEO/accesibilidad | [ver](examples/imagen_img__img.html) |
| Ancho de imagen | `width=""` | atributo | Especificar ancho | [ver](examples/imagen_dimensiones__width_height.html) |
| Alto de imagen | `height=""` | atributo | Especificar alto | [ver](examples/imagen_dimensiones__width_height.html) |
| Figura con leyenda | `<figure>` | elemento | Imagen con contexto | [ver](examples/figura_figure__figure.html) |
| Leyenda de figura | `<figcaption>` | elemento | Descripción de figura | [ver](examples/figura_figure__figure.html) |

---

## Tablas

### Estructura Básica

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Tabla | `<table>` | elemento | Contenedor de datos tabulares | [ver](examples/tabla_tabla__table.html) |
| Fila de tabla | `<tr>` | elemento | Fila (table row) | [ver](examples/tabla_tabla__table.html) |
| Celda de encabezado | `<th>` | elemento | Celda de encabezado | [ver](examples/tabla_tabla__table.html) |
| Celda de datos | `<td>` | elemento | Celda de datos | [ver](examples/tabla_tabla__table.html) |
| Encabezado de tabla | `<thead>` | elemento | Agrupa encabezados | [ver](examples/tabla_estructura__thead_tbody.html) |
| Cuerpo de tabla | `<tbody>` | elemento | Agrupa datos | [ver](examples/tabla_estructura__thead_tbody.html) |
| Pie de tabla | `<tfoot>` | elemento | Agrupa totales/resumen | [ver](examples/tabla_estructura__thead_tbody.html) |
| Título de tabla | `<caption>` | elemento | Descripción de tabla | [ver](examples/tabla_caption__caption.html) |

### Atributos de Tabla

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Fusión horizontal | `colspan` | atributo | Combinar columnas | [ver](examples/tabla_colspan__colspan.html) |
| Fusión vertical | `rowspan` | atributo | Combinar filas | [ver](examples/tabla_rowspan__rowspan.html) |
| Alcance de encabezado | `scope` | atributo | Define si es col/row | [ver](examples/tabla_scope__scope.html) |

---

## Formularios

### Estructura Básica

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Formulario | `<form>` | elemento | Contenedor de controles | [ver](examples/formulario_form__form.html) |
| Etiqueta | `<label>` | elemento | Etiqueta de control | [ver](examples/formulario_label__label.html) |
| Campo de entrada | `<input>` | elemento | Controles de usuario | [ver](examples/formulario_input_text__text.html) |
| Atributo name | `name=""` | atributo | Nombre del campo | [ver](examples/formulario_input_text__text.html) |
| Atributo id | `id=""` | atributo | Identificador único | [ver](examples/formulario_label__label.html) |
| Asociar label a input | `for=""` | atributo | Vincula label con input | [ver](examples/formulario_label__label.html) |

### Tipos de Input

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Texto | `type="text"` | atributo | Entrada de texto simple | [ver](examples/formulario_input_text__text.html) |
| Contraseña | `type="password"` | atributo | Oculta caracteres | [ver](examples/formulario_input_password__password.html) |
| Email | `type="email"` | atributo | Validación de email | [ver](examples/formulario_input_email__email.html) |
| Teléfono | `type="tel"` | atributo | Número de teléfono | [ver](examples/formulario_input_tel__tel.html) |
| Número | `type="number"` | atributo | Solo números | [ver](examples/formulario_input_number__number.html) |
| URL | `type="url"` | atributo | Validación de URL | [ver](examples/formulario_input_url__url.html) |
| Búsqueda | `type="search"` | atributo | Campo de búsqueda | [ver](examples/formulario_input_search__search.html) |
| Fecha | `type="date"` | atributo | Selector de fecha | [ver](examples/formulario_input_date__date.html) |
| Hora | `type="time"` | atributo | Selector de hora | [ver](examples/formulario_input_time__time.html) |
| Rango | `type="range"` | atributo | Deslizador | [ver](examples/formulario_input_range__range.html) |
| Color | `type="color"` | atributo | Selector de color | [ver](examples/formulario_input_color__color.html) |
| Checkbox | `type="checkbox"` | atributo | Múltiples selecciones | [ver](examples/formulario_input_checkbox__checkbox.html) |
| Radio | `type="radio"` | atributo | Una única selección | [ver](examples/formulario_input_radio__radio.html) |
| Envío | `type="submit"` | atributo | Botón enviar | [ver](examples/formulario_input_submit__submit.html) |
| Reinicio | `type="reset"` | atributo | Botón limpiar | [ver](examples/formulario_input_submit__submit.html) |
| Botón | `type="button"` | atributo | Botón personalizado | [ver](examples/formulario_input_button__button.html) |
| Archivo | `type="file"` | atributo | Seleccionar archivo | [ver](examples/formulario_input_file__file.html) |
| Oculto | `type="hidden"` | atributo | Campo no visible | [ver](examples/formulario_input_hidden__hidden.html) |

### Otros Controles de Formulario

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Área de texto | `<textarea>` | elemento | Texto multilínea | [ver](examples/formulario_textarea__textarea.html) |
| Lista desplegable | `<select>` | elemento | Selección única | [ver](examples/formulario_select__select.html) |
| Opción | `<option>` | elemento | Opción en select | [ver](examples/formulario_select__select.html) |
| Botón | `<button>` | elemento | Botón interactivo | [ver](examples/formulario_button__button.html) |
| Grupo de campos | `<fieldset>` | elemento | Agrupa controles | [ver](examples/formulario_fieldset__fieldset.html) |
| Leyenda de grupo | `<legend>` | elemento | Título de fieldset | [ver](examples/formulario_fieldset__fieldset.html) |
| Sugerencias autocomplete | `<datalist>` | elemento | Lista de sugerencias | [ver](examples/formulario_datalist__datalist.html) |

### Atributos de Validación

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Campo obligatorio | `required` | atributo | Valida no vacío | [ver](examples/formulario_validacion_required__required.html) |
| Valor mínimo | `min=""` | atributo | Límite inferior | [ver](examples/formulario_validacion_min_max__min_max.html) |
| Valor máximo | `max=""` | atributo | Límite superior | [ver](examples/formulario_validacion_min_max__min_max.html) |
| Longitud mínima | `minlength=""` | atributo | Caracteres mínimos | [ver](examples/formulario_validacion_minlength_maxlength__lengths.html) |
| Longitud máxima | `maxlength=""` | atributo | Caracteres máximos | [ver](examples/formulario_validacion_minlength_maxlength__lengths.html) |
| Patrón | `pattern=""` | atributo | Validación con regex | [ver](examples/formulario_validacion_pattern__pattern.html) |
| Placeholder | `placeholder=""` | atributo | Texto de ayuda | [ver](examples/formulario_validacion_placeholder__placeholder.html) |

---

## Contenido Embebido

### Multimedia

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Audio | `<audio>` | elemento | Reproduce audio | [ver](examples/multimedia_audio__audio.html) |
| Video | `<video>` | elemento | Reproduce video | [ver](examples/multimedia_video__video.html) |
| Fuente de media | `<source>` | elemento | Especifica archivo media | [ver](examples/multimedia_audio__audio.html) |
| Pista de subtítulos | `<track>` | elemento | Subtítulos/descripciones | [ver](examples/multimedia_video__video.html) |

### Contenido Externo

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Marco insertado | `<iframe>` | elemento | Incrustar página | [ver](examples/multimedia_video__video.html) |
| Objeto embebido | `<embed>` | elemento | Incrusta contenido | [ver](examples/multimedia_video__video.html) |
| Objeto | `<object>` | elemento | Recurso externo | [ver](examples/multimedia_video__video.html) |

---

## Contenedores Genéricos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| División de bloque | `<div>` | elemento | Contenedor genérico bloque | [ver](examples/contenedor_div__div.html) |
| Contenedor inline | `<span>` | elemento | Contenedor genérico inline | [ver](examples/contenedor_span__span.html) |

---

## Atributos Globales

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Identificador único | `id=""` | atributo | ID único del elemento | [ver](examples/atributo_id__id.html) |
| Clase CSS | `class=""` | atributo | Clases para estilos | [ver](examples/atributo_class__class.html) |
| Estilos inline | `style=""` | atributo | CSS directo | [ver](examples/atributo_style__style.html) |
| Título/tooltip | `title=""` | atributo | Información al pasar ratón | [ver](examples/atributo_style__style.html) |
| Atributo de datos | `data-*=""` | atributo | Datos personalizados | [ver](examples/atributo_style__style.html) |
| Idioma del contenido | `lang=""` | atributo | Idioma del elemento | [ver](examples/atributo_style__style.html) |
| Accesibilidad | `role=""` | atributo | Rol ARIA | [ver](examples/atributo_style__style.html) |

---

## Semántica HTML5

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Encabezado | `<header>` | elemento | Encabezado de página/sección | [ver](examples/semantica_header__header.html) |
| Navegación | `<nav>` | elemento | Navegación principal | [ver](examples/semantica_nav__nav.html) |
| Contenido principal | `<main>` | elemento | Contenido principal (único) | [ver](examples/semantica_main__main.html) |
| Artículo | `<article>` | elemento | Contenido independiente | [ver](examples/semantica_article__article.html) |
| Sección | `<section>` | elemento | Agrupación temática | [ver](examples/semantica_section__section.html) |
| Barra lateral | `<aside>` | elemento | Contenido relacionado | [ver](examples/semantica_aside__aside.html) |
| Pie de página | `<footer>` | elemento | Pie de página | [ver](examples/semantica_footer__footer.html) |
| Marca de tiempo | `<time>` | elemento | Fecha/hora semántica | [ver](examples/semantica_time__time.html) |
| Información de contacto | `<address>` | elemento | Detalles de contacto | [ver](examples/semantica_address__address.html) |

---

## Contenedores Genéricos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| División de bloque | `<div>` | elemento | Contenedor genérico bloque | [ver](examples/contenedor_div__div.html) |
| Contenedor inline | `<span>` | elemento | Contenedor genérico inline | [ver](examples/contenedor_span__span.html) |

---

## Guías de Uso

### Estructura Básica de una Página HTML

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título de la Página</title>
</head>
<body>
    <header>
        <h1>Título Principal</h1>
        <nav><!-- Navegación --></nav>
    </header>
    <main>
        <article>
            <h2>Artículo</h2>
            <p>Contenido...</p>
        </article>
    </main>
    <footer>
        <p>Pie de página</p>
    </footer>
</body>
</html>
```

### Diferencia entre Elementos Semánticos

- `<strong>` vs `<b>`: Strong = importancia, B = solo negrita
- `<em>` vs `<i>`: Em = énfasis, I = solo cursiva  
- `<article>` vs `<section>`: Article = contenido reutilizable, Section = agrupación temática
- `<main>` vs `<div>`: Main = contenido principal (único), div = genérico

### Validación HTML5

Siempre validar tu HTML en: https://validator.w3.org/

### Accesibilidad

- Usar `<label>` con atributo `for` en formularios
- Incluir `alt=""` en todas las imágenes
- Usar atributo `scope` en tablas
- Usar `<button>` en lugar de `<div>` para botones
- Usar texto descriptivo en enlaces

---

## Estadísticas

- **Total de conceptos**: 130+ elementos y atributos
- **Total de ejemplos**: 91 archivos HTML ejecutables
- **Líneas de código**: 4,365 líneas
- **Secciones principales**: 15 categorías

---

**Última actualización:** Enero 2024  
**Autor:** Experto en HTML5
