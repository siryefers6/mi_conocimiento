# Tailwind CSS v4.1 - Guía Completa

Referencia rápida de utilidades, características y conceptos fundamentales de Tailwind CSS v4.1 con ejemplos ejecutables.

---

## Instalación y Configuración

### Instalación rápida

```bash
npm install -D tailwindcss
npx tailwindcss init
```

### Configuración básica (tailwind.config.js)

```javascript
module.exports = {
  content: ['./src/**/*.{html,js}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### CDN (para demostración)

```html
<script src="https://cdn.tailwindcss.com"></script>
```

---

## Utilidades de Layout

### Display

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Block | `block` | display | Elemento como bloque | [ver](examples/layout_display__block.html) |
| Inline | `inline` | display | Elemento en línea | [ver](examples/layout_display__inline.html) |
| Inline-block | `inline-block` | display | Elemento en línea con bloque | [ver](examples/layout_display__inline-block.html) |
| Flex | `flex` | display | Flexbox container | [ver](examples/layout_display__flex.html) |
| Grid | `grid` | display | CSS Grid container | [ver](examples/layout_display__grid.html) |
| Hidden | `hidden` | display | Ocultar elemento | [ver](examples/layout_display__hidden.html) |
| Contents | `contents` | display | Sin crear caja | [ver](examples/layout_display__contents.html) |
| Table | `table` | display | Comportamiento tabla | [ver](examples/layout_display__table.html) |

### Flexbox - Dirección

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Fila | `flex-row` | dirección | Flex horizontal | [ver](examples/flexbox_flex-row__row.html) |
| Fila inversa | `flex-row-reverse` | dirección | Flex horizontal invertido | [ver](examples/flexbox_flex-row-reverse__row-rev.html) |
| Columna | `flex-col` | dirección | Flex vertical | [ver](examples/flexbox_flex-col__col.html) |
| Columna inversa | `flex-col-reverse` | dirección | Flex vertical invertido | [ver](examples/flexbox_flex-col-reverse__col-rev.html) |

### Flexbox - Justificación

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Inicio | `justify-start` | alineación | Contenido al inicio | [ver](examples/flexbox_justify-start__start.html) |
| Centro | `justify-center` | alineación | Contenido al centro | [ver](examples/flexbox_justify-center__center.html) |
| Fin | `justify-end` | alineación | Contenido al fin | [ver](examples/flexbox_justify-end__end.html) |
| Espaciado entre | `justify-between` | alineación | Espaciado uniforme | [ver](examples/flexbox_justify-between__between.html) |
| Espaciado alrededor | `justify-around` | alineación | Espacio alrededor | [ver](examples/flexbox_justify-around__around.html) |
| Espaciado igual | `justify-evenly` | alineación | Espacio igual | [ver](examples/flexbox_justify-evenly__evenly.html) |

### Flexbox - Alineación

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Inicio | `items-start` | alineación | Alineación al inicio | [ver](examples/flexbox_items-start__start.html) |
| Centro | `items-center` | alineación | Alineación al centro | [ver](examples/flexbox_items-center__center.html) |
| Fin | `items-end` | alineación | Alineación al fin | [ver](examples/flexbox_items-end__end.html) |
| Estirado | `items-stretch` | alineación | Estirado completo | [ver](examples/flexbox_items-stretch__stretch.html) |
| Línea base | `items-baseline` | alineación | Alineación línea base | [ver](examples/flexbox_items-baseline__baseline.html) |

### Flexbox - Envolvimiento

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Sin envolver | `flex-nowrap` | envolvimiento | Sin salto de línea | [ver](examples/flexbox_flex-nowrap__nowrap.html) |
| Envolver | `flex-wrap` | envolvimiento | Con salto de línea | [ver](examples/flexbox_flex-wrap__wrap.html) |
| Envolver inverso | `flex-wrap-reverse` | envolvimiento | Salto inverso | [ver](examples/flexbox_flex-wrap-reverse__wrap-rev.html) |

### Flexbox - Flex Grow/Shrink

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Grow auto | `flex-1` | tamaño | Crece proporcionalmente | [ver](examples/flexbox_flex-1__grow.html) |
| Grow inicial | `flex-initial` | tamaño | Tamaño inicial | [ver](examples/flexbox_flex-initial__initial.html) |
| Sin flex | `flex-none` | tamaño | No se expande ni reduce | [ver](examples/flexbox_flex-none__none.html) |
| Auto | `flex-auto` | tamaño | Se expande y reduce | [ver](examples/flexbox_flex-auto__auto.html) |

### Grid - Columnas

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| 1 columna | `grid-cols-1` | columnas | Una sola columna | [ver](examples/grid_grid-cols-1__col1.html) |
| 2 columnas | `grid-cols-2` | columnas | Dos columnas | [ver](examples/grid_grid-cols-2__col2.html) |
| 3 columnas | `grid-cols-3` | columnas | Tres columnas | [ver](examples/grid_grid-cols-3__col3.html) |
| 4 columnas | `grid-cols-4` | columnas | Cuatro columnas | [ver](examples/grid_grid-cols-4__col4.html) |
| 6 columnas | `grid-cols-6` | columnas | Seis columnas | [ver](examples/grid_grid-cols-6__col6.html) |
| 12 columnas | `grid-cols-12` | columnas | Doce columnas | [ver](examples/grid_grid-cols-12__col12.html) |
| Automático | `grid-cols-none` | columnas | Definir manualmente | [ver](examples/grid_grid-cols-none__auto.html) |

### Grid - Filas

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| 2 filas | `grid-rows-2` | filas | Dos filas | [ver](examples/grid_grid-rows-2__row2.html) |
| 3 filas | `grid-rows-3` | filas | Tres filas | [ver](examples/grid_grid-rows-3__row3.html) |
| 4 filas | `grid-rows-4` | filas | Cuatro filas | [ver](examples/grid_grid-rows-4__row4.html) |

### Grid - Alineación

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Justificar inicio | `justify-items-start` | alineación | Items al inicio | [ver](examples/grid_justify-items-start__start.html) |
| Justificar centro | `justify-items-center` | alineación | Items al centro | [ver](examples/grid_justify-items-center__center.html) |
| Justificar fin | `justify-items-end` | alineación | Items al fin | [ver](examples/grid_justify-items-end__end.html) |
| Items inicio | `items-start` | alineación | Alineación vertical inicio | [ver](examples/grid_items-start__start.html) |
| Items centro | `items-center` | alineación | Alineación vertical centro | [ver](examples/grid_items-center__center.html) |
| Items fin | `items-end` | alineación | Alineación vertical fin | [ver](examples/grid_items-end__end.html) |

### Posicionamiento

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Relativo | `relative` | posición | Posición relativa | [ver](examples/position_relative__relative.html) |
| Absoluto | `absolute` | posición | Posición absoluta | [ver](examples/position_absolute__absolute.html) |
| Fijo | `fixed` | posición | Posición fija | [ver](examples/position_fixed__fixed.html) |
| Pegajoso | `sticky` | posición | Posición sticky | [ver](examples/position_sticky__sticky.html) |

### Posicionamiento - Offset

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Top 0 | `top-0` | offset | Arriba | [ver](examples/position_top-0__top.html) |
| Right 0 | `right-0` | offset | Derecha | [ver](examples/position_right-0__right.html) |
| Bottom 0 | `bottom-0` | offset | Abajo | [ver](examples/position_bottom-0__bottom.html) |
| Left 0 | `left-0` | offset | Izquierda | [ver](examples/position_left-0__left.html) |
| Inset 0 | `inset-0` | offset | Todos lados | [ver](examples/position_inset-0__inset.html) |

### Z-Index

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Auto | `z-auto` | apilamiento | Apilamiento automático | [ver](examples/zindex_z-auto__auto.html) |
| 0 | `z-0` | apilamiento | Z-index 0 | [ver](examples/zindex_z-0__zero.html) |
| 10 | `z-10` | apilamiento | Z-index 10 | [ver](examples/zindex_z-10__ten.html) |
| 20 | `z-20` | apilamiento | Z-index 20 | [ver](examples/zindex_z-20__twenty.html) |
| 50 | `z-50` | apilamiento | Z-index 50 | [ver](examples/zindex_z-50__fifty.html) |

### Overflow

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Visible | `overflow-visible` | desbordamiento | Visible | [ver](examples/overflow_overflow-visible__visible.html) |
| Oculto | `overflow-hidden` | desbordamiento | Oculto | [ver](examples/overflow_overflow-hidden__hidden.html) |
| Scroll | `overflow-scroll` | desbordamiento | Con scroll | [ver](examples/overflow_overflow-scroll__scroll.html) |
| Auto | `overflow-auto` | desbordamiento | Auto scroll | [ver](examples/overflow_overflow-auto__auto.html) |
| X scroll | `overflow-x-auto` | desbordamiento | Scroll horizontal | [ver](examples/overflow_overflow-x-auto__x.html) |
| Y scroll | `overflow-y-auto` | desbordamiento | Scroll vertical | [ver](examples/overflow_overflow-y-auto__y.html) |

---

## Espaciado y Tamaño

### Padding

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| p-1 a p-96 | `p-*` | padding | Padding uniforme | [ver](examples/spacing_padding__padding.html) |
| px (horizontal) | `px-*` | padding | Padding izq/der | [ver](examples/spacing_padding-x__px.html) |
| py (vertical) | `py-*` | padding | Padding arriba/abajo | [ver](examples/spacing_padding-y__py.html) |
| pt (top) | `pt-*` | padding | Padding arriba | [ver](examples/spacing_padding-top__pt.html) |
| pb (bottom) | `pb-*` | padding | Padding abajo | [ver](examples/spacing_padding-bottom__pb.html) |
| pl (left) | `pl-*` | padding | Padding izquierda | [ver](examples/spacing_padding-left__pl.html) |
| pr (right) | `pr-*` | padding | Padding derecha | [ver](examples/spacing_padding-right__pr.html) |

### Margin

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| m-1 a m-96 | `m-*` | margen | Margen uniforme | [ver](examples/spacing_margin__margin.html) |
| mx (horizontal) | `mx-*` | margen | Margen izq/der | [ver](examples/spacing_margin-x__mx.html) |
| my (vertical) | `my-*` | margen | Margen arriba/abajo | [ver](examples/spacing_margin-y__my.html) |
| mt (top) | `mt-*` | margen | Margen arriba | [ver](examples/spacing_margin-top__mt.html) |
| mb (bottom) | `mb-*` | margen | Margen abajo | [ver](examples/spacing_margin-bottom__mb.html) |
| ml (left) | `ml-*` | margen | Margen izquierda | [ver](examples/spacing_margin-left__ml.html) |
| mr (right) | `mr-*` | margen | Margen derecha | [ver](examples/spacing_margin-right__mr.html) |
| Margen negativo | `-m-*` | margen | Margen negativo | [ver](examples/spacing_margin-negative__neg.html) |

### Ancho (Width)

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| w-1/2 | `w-1/2` | ancho | 50% ancho | [ver](examples/spacing_width-half__half.html) |
| w-1/3 | `w-1/3` | ancho | 33% ancho | [ver](examples/spacing_width-third__third.html) |
| w-1/4 | `w-1/4` | ancho | 25% ancho | [ver](examples/spacing_width-quarter__quarter.html) |
| w-full | `w-full` | ancho | 100% ancho | [ver](examples/spacing_width-full__full.html) |
| w-screen | `w-screen` | ancho | Ancho ventana | [ver](examples/spacing_width-screen__screen.html) |
| w-auto | `w-auto` | ancho | Ancho automático | [ver](examples/spacing_width-auto__auto.html) |
| w-96 | `w-96` | ancho | Valor específico | [ver](examples/spacing_width-fixed__fixed.html) |
| min-w | `min-w-*` | ancho | Ancho mínimo | [ver](examples/spacing_min-w__min.html) |
| max-w | `max-w-*` | ancho | Ancho máximo | [ver](examples/spacing_max-w__max.html) |

### Alto (Height)

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| h-full | `h-full` | alto | 100% alto | [ver](examples/spacing_height-full__full.html) |
| h-screen | `h-screen` | alto | Alto ventana | [ver](examples/spacing_height-screen__screen.html) |
| h-auto | `h-auto` | alto | Alto automático | [ver](examples/spacing_height-auto__auto.html) |
| min-h | `min-h-*` | alto | Alto mínimo | [ver](examples/spacing_min-h__min.html) |
| max-h | `max-h-*` | alto | Alto máximo | [ver](examples/spacing_max-h__max.html) |

### Gap

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| gap-1 a gap-96 | `gap-*` | espaciado | Espacio entre items | [ver](examples/spacing_gap__gap.html) |
| gap-x (horizontal) | `gap-x-*` | espaciado | Espacio horizontal | [ver](examples/spacing_gap-x__gapx.html) |
| gap-y (vertical) | `gap-y-*` | espaciado | Espacio vertical | [ver](examples/spacing_gap-y__gapy.html) |

---

## Tipografía

### Tamaño de Fuente

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| xs | `text-xs` | tamaño | Muy pequeño | [ver](examples/typography_text-xs__xs.html) |
| sm | `text-sm` | tamaño | Pequeño | [ver](examples/typography_text-sm__sm.html) |
| base | `text-base` | tamaño | Base (16px) | [ver](examples/typography_text-base__base.html) |
| lg | `text-lg` | tamaño | Grande | [ver](examples/typography_text-lg__lg.html) |
| xl | `text-xl` | tamaño | Muy grande | [ver](examples/typography_text-xl__xl.html) |
| 2xl | `text-2xl` | tamaño | Enorme | [ver](examples/typography_text-2xl__2xl.html) |
| 3xl | `text-3xl` | tamaño | Gigante | [ver](examples/typography_text-3xl__3xl.html) |
| 4xl | `text-4xl` | tamaño | Ultra | [ver](examples/typography_text-4xl__4xl.html) |
| 5xl | `text-5xl` | tamaño | Máximo | [ver](examples/typography_text-5xl__5xl.html) |

### Peso de Fuente

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Thin | `font-thin` | peso | 100 | [ver](examples/typography_font-thin__thin.html) |
| Extralight | `font-extralight` | peso | 200 | [ver](examples/typography_font-extralight__extra.html) |
| Light | `font-light` | peso | 300 | [ver](examples/typography_font-light__light.html) |
| Normal | `font-normal` | peso | 400 | [ver](examples/typography_font-normal__normal.html) |
| Medium | `font-medium` | peso | 500 | [ver](examples/typography_font-medium__medium.html) |
| Semibold | `font-semibold` | peso | 600 | [ver](examples/typography_font-semibold__semi.html) |
| Bold | `font-bold` | peso | 700 | [ver](examples/typography_font-bold__bold.html) |
| Extrabold | `font-extrabold` | peso | 800 | [ver](examples/typography_font-extrabold__extrabold.html) |
| Black | `font-black` | peso | 900 | [ver](examples/typography_font-black__black.html) |

### Alineación de Texto

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Izquierda | `text-left` | alineación | Alineado izquierda | [ver](examples/typography_text-left__left.html) |
| Centro | `text-center` | alineación | Alineado centro | [ver](examples/typography_text-center__center.html) |
| Derecha | `text-right` | alineación | Alineado derecha | [ver](examples/typography_text-right__right.html) |
| Justificado | `text-justify` | alineación | Alineado justificado | [ver](examples/typography_text-justify__justify.html) |

### Color de Texto

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| text-slate-900 | `text-slate-900` | color | Texto oscuro | [ver](examples/typography_text-color__color.html) |
| text-red-500 | `text-red-500` | color | Texto rojo | [ver](examples/typography_text-red__red.html) |
| text-blue-600 | `text-blue-600` | color | Texto azul | [ver](examples/typography_text-blue__blue.html) |
| text-green-500 | `text-green-500` | color | Texto verde | [ver](examples/typography_text-green__green.html) |

### Altura de Línea

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| leading-none | `leading-none` | altura | Mínima | [ver](examples/typography_leading-none__none.html) |
| leading-tight | `leading-tight` | altura | Comprimida | [ver](examples/typography_leading-tight__tight.html) |
| leading-normal | `leading-normal` | altura | Normal | [ver](examples/typography_leading-normal__normal.html) |
| leading-relaxed | `leading-relaxed` | altura | Relajada | [ver](examples/typography_leading-relaxed__relaxed.html) |
| leading-loose | `leading-loose` | altura | Suelta | [ver](examples/typography_leading-loose__loose.html) |

### Decoración de Texto

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Subrayado | `underline` | decoración | Con línea | [ver](examples/typography_underline__underline.html) |
| Tachado | `line-through` | decoración | Tachado | [ver](examples/typography_line-through__strike.html) |
| Mayúsculas | `uppercase` | transformación | Todo mayúsculas | [ver](examples/typography_uppercase__upper.html) |
| Minúsculas | `lowercase` | transformación | Todo minúsculas | [ver](examples/typography_lowercase__lower.html) |
| Capitalizar | `capitalize` | transformación | Primera letra grande | [ver](examples/typography_capitalize__cap.html) |

---

## Colores y Efectos

### Paleta de Colores

| Concepto | Clases | Tipo | Uso | Ejemplo |
|----------|--------|------|-----|---------|
| Slate | `bg-slate-*`, `text-slate-*` | color | Gris neutral | [ver](examples/colors_slate__slate.html) |
| Red | `bg-red-*`, `text-red-*` | color | Rojo | [ver](examples/colors_red__red.html) |
| Orange | `bg-orange-*`, `text-orange-*` | color | Naranja | [ver](examples/colors_orange__orange.html) |
| Yellow | `bg-yellow-*`, `text-yellow-*` | color | Amarillo | [ver](examples/colors_yellow__yellow.html) |
| Green | `bg-green-*`, `text-green-*` | color | Verde | [ver](examples/colors_green__green.html) |
| Blue | `bg-blue-*`, `text-blue-*` | color | Azul | [ver](examples/colors_blue__blue.html) |
| Indigo | `bg-indigo-*`, `text-indigo-*` | color | Índigo | [ver](examples/colors_indigo__indigo.html) |
| Purple | `bg-purple-*`, `text-purple-*` | color | Púrpura | [ver](examples/colors_purple__purple.html) |
| Pink | `bg-pink-*`, `text-pink-*` | color | Rosa | [ver](examples/colors_pink__pink.html) |

### Fondo (Background)

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Fondo color | `bg-blue-500` | fondo | Color de fondo | [ver](examples/effects_bg-color__color.html) |
| Gradiente | `bg-gradient-to-r` | gradiente | Gradiente a derecha | [ver](examples/effects_gradient-right__right.html) |
| Gradiente abajo | `bg-gradient-to-b` | gradiente | Gradiente hacia abajo | [ver](examples/effects_gradient-down__down.html) |
| From-color | `from-blue-500` | gradiente | Color inicio gradiente | [ver](examples/effects_gradient-from__from.html) |
| To-color | `to-purple-500` | gradiente | Color fin gradiente | [ver](examples/effects_gradient-to__to.html) |

### Bordes

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Border 1px | `border` | borde | Borde 1px | [ver](examples/effects_border__border.html) |
| Border 2px | `border-2` | borde | Borde 2px | [ver](examples/effects_border-2__border2.html) |
| Border color | `border-blue-500` | borde | Color del borde | [ver](examples/effects_border-color__color.html) |
| Border-t | `border-t` | borde | Solo arriba | [ver](examples/effects_border-top__top.html) |
| Border-b | `border-b` | borde | Solo abajo | [ver](examples/effects_border-bottom__bottom.html) |
| Border-l | `border-l` | borde | Solo izquierda | [ver](examples/effects_border-left__left.html) |
| Border-r | `border-r` | borde | Solo derecha | [ver](examples/effects_border-right__right.html) |

### Radio de Esquinas (Border Radius)

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Redondeado | `rounded` | esquinas | 0.25rem esquinas | [ver](examples/effects_rounded__rounded.html) |
| Muy redondeado | `rounded-md` | esquinas | 0.375rem esquinas | [ver](examples/effects_rounded-md__md.html) |
| Muy muy redondeado | `rounded-lg` | esquinas | 0.5rem esquinas | [ver](examples/effects_rounded-lg__lg.html) |
| Círculo | `rounded-full` | esquinas | Completamente redondeado | [ver](examples/effects_rounded-full__full.html) |

### Sombras

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Sombra pequeña | `shadow-sm` | sombra | Sombra sutil | [ver](examples/effects_shadow-sm__sm.html) |
| Sombra normal | `shadow` | sombra | Sombra estándar | [ver](examples/effects_shadow__shadow.html) |
| Sombra grande | `shadow-lg` | sombra | Sombra pronunciada | [ver](examples/effects_shadow-lg__lg.html) |
| Sombra XL | `shadow-xl` | sombra | Sombra muy pronunciada | [ver](examples/effects_shadow-xl__xl.html) |
| Sombra color | `shadow-blue-500/50` | sombra | Sombra con color | [ver](examples/effects_shadow-color__color.html) |

### Opacidad

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| opacity-0 | `opacity-0` | transparencia | Invisible | [ver](examples/effects_opacity-0__zero.html) |
| opacity-50 | `opacity-50` | transparencia | Semi-transparente | [ver](examples/effects_opacity-50__half.html) |
| opacity-100 | `opacity-100` | transparencia | Opaco | [ver](examples/effects_opacity-100__full.html) |

---

## Responsive Design

### Breakpoints

| Concepto | Breakpoint | Ancho | Uso | Ejemplo |
|----------|------------|-------|-----|---------|
| sm | `sm:` | 640px | Tablets pequeñas | [ver](examples/responsive_sm__sm.html) |
| md | `md:` | 768px | Tablets | [ver](examples/responsive_md__md.html) |
| lg | `lg:` | 1024px | Laptops | [ver](examples/responsive_lg__lg.html) |
| xl | `xl:` | 1280px | Desktops | [ver](examples/responsive_xl__xl.html) |
| 2xl | `2xl:` | 1536px | Desktops grandes | [ver](examples/responsive_2xl__2xl.html) |

### Media Queries

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Mobile first | `md:bg-blue-500` | responsive | Base mobile, cambio en md | [ver](examples/responsive_mobile-first__mobile.html) |
| Oscuro | `dark:bg-gray-900` | modo | Estilos en dark mode | [ver](examples/responsive_dark-mode__dark.html) |
| Landscape | `landscape:text-2xl` | orientación | Paisaje | [ver](examples/responsive_landscape__landscape.html) |
| Portrait | `portrait:text-base` | orientación | Retrato | [ver](examples/responsive_portrait__portrait.html) |

---

## Dark Mode

### Modo Oscuro

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Dark text | `dark:text-white` | modo | Texto blanco en oscuro | [ver](examples/darkmode_text__text.html) |
| Dark background | `dark:bg-gray-900` | modo | Fondo oscuro | [ver](examples/darkmode_bg__bg.html) |
| Dark border | `dark:border-gray-700` | modo | Borde oscuro | [ver](examples/darkmode_border__border.html) |
| Dark toggle | Usar `dark` clase | configuración | Activar modo oscuro | [ver](examples/darkmode_toggle__toggle.html) |

---

## Animaciones y Transformaciones

### Transiciones

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Transición | `transition` | transición | Transición por defecto | [ver](examples/animations_transition__transition.html) |
| Duration 75ms | `duration-75` | duración | 75 milisegundos | [ver](examples/animations_duration-75__75.html) |
| Duration 100ms | `duration-100` | duración | 100 milisegundos | [ver](examples/animations_duration-100__100.html) |
| Duration 150ms | `duration-150` | duración | 150 milisegundos | [ver](examples/animations_duration-150__150.html) |
| Duration 300ms | `duration-300` | duración | 300 milisegundos | [ver](examples/animations_duration-300__300.html) |
| Duration 500ms | `duration-500` | duración | 500 milisegundos | [ver](examples/animations_duration-500__500.html) |

### Transform

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Scale | `scale-75` | transformación | Escala 75% | [ver](examples/animations_scale__scale.html) |
| Rotate | `rotate-45` | transformación | Rotación 45° | [ver](examples/animations_rotate__rotate.html) |
| Translate X | `translate-x-2` | transformación | Mover horizontal | [ver](examples/animations_translate-x__transx.html) |
| Translate Y | `translate-y-2` | transformación | Mover vertical | [ver](examples/animations_translate-y__transy.html) |
| Skew | `skew-x-12` | transformación | Sesgar | [ver](examples/animations_skew__skew.html) |

### Animaciones Predefinidas

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Bounce | `animate-bounce` | animación | Rebota | [ver](examples/animations_animate-bounce__bounce.html) |
| Ping | `animate-ping` | animación | Efecto ping | [ver](examples/animations_animate-ping__ping.html) |
| Pulse | `animate-pulse` | animación | Latido | [ver](examples/animations_animate-pulse__pulse.html) |
| Spin | `animate-spin` | animación | Gira | [ver](examples/animations_animate-spin__spin.html) |

### Hover, Focus y States

| Concepto | Clase | Tipo | Uso | Ejemplo |
|----------|-------|------|-----|---------|
| Hover | `hover:bg-blue-600` | estado | Al pasar | [ver](examples/animations_hover__hover.html) |
| Focus | `focus:outline-blue-500` | estado | Al enfoque | [ver](examples/animations_focus__focus.html) |
| Active | `active:scale-95` | estado | Al click | [ver](examples/animations_active__active.html) |
| Disabled | `disabled:opacity-50` | estado | Deshabilitado | [ver](examples/animations_disabled__disabled.html) |
| Group hover | `group-hover:text-white` | estado | Grupo al hover | [ver](examples/animations_group-hover__group.html) |

---

## Patrones Comunes

### Navbar Responsivo

```html
<nav class="bg-blue-600 text-white p-4">
  <div class="flex justify-between items-center">
    <h1 class="text-2xl font-bold">Logo</h1>
    <div class="hidden md:flex gap-4">
      <a href="#" class="hover:bg-blue-700 px-3 py-2 rounded">Home</a>
      <a href="#" class="hover:bg-blue-700 px-3 py-2 rounded">About</a>
    </div>
  </div>
</nav>
```

### Card Component

```html
<div class="bg-white rounded-lg shadow-md p-6 max-w-sm">
  <h2 class="text-xl font-bold mb-2">Título</h2>
  <p class="text-gray-600 mb-4">Descripción</p>
  <button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
    Acción
  </button>
</div>
```

### Grid de Productos

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition">
    <img src="image.jpg" class="w-full h-48 object-cover">
    <div class="p-4">
      <h3 class="font-bold text-lg">Producto</h3>
      <p class="text-gray-600">$99.99</p>
    </div>
  </div>
</div>
```

### Formulario

```html
<form class="max-w-md mx-auto space-y-4">
  <div>
    <label class="block text-sm font-medium mb-1">Email</label>
    <input type="email" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-blue-500">
  </div>
  <button type="submit" class="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 rounded font-medium">
    Enviar
  </button>
</form>
```

### Hero Section

```html
<section class="bg-gradient-to-r from-blue-500 to-purple-600 text-white py-20 px-4">
  <div class="max-w-4xl mx-auto text-center">
    <h1 class="text-4xl md:text-5xl font-bold mb-4">Bienvenido</h1>
    <p class="text-lg md:text-xl mb-8">Descripción atractiva</p>
    <button class="bg-white text-blue-600 px-8 py-3 rounded-lg font-bold hover:bg-gray-100">
      Comenzar
    </button>
  </div>
</section>
```

### Modal

```html
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
  <div class="bg-white rounded-lg p-6 max-w-sm">
    <h2 class="text-2xl font-bold mb-4">Modal</h2>
    <p class="text-gray-600 mb-6">Contenido del modal</p>
    <button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
      Cerrar
    </button>
  </div>
</div>
```

---

## Mejores Prácticas

1. **Mobile first**: Comienza con estilos mobile y agrega breakpoints responsivos
2. **Reutilización**: Crea componentes reutilizables con `@apply` en CSS personalizado
3. **Dark mode**: Siempre considera el modo oscuro con prefijo `dark:`
4. **Accesibilidad**: Usa focus states y contraste adecuado
5. **Performance**: Usa purge CSS para remover clases no utilizadas
6. **Extensión**: Personaliza la configuración en `tailwind.config.js`
7. **BEM opcional**: Puedes usar naming para componentes complejos
8. **Flexibilidad**: Aprovecha valores arbitrarios como `w-[500px]`
9. **Componentes**: Agrupa clases repetidas con `@apply` en CSS
10. **Testing**: Prueba en diferentes dispositivos y navegadores

---

## Paleta de Colores Escala

| Nivel | Valor | Uso |
|-------|-------|-----|
| 50 | Más claro | Fondos ligeros |
| 100 | Muy claro | Bordes suaves |
| 200 | Claro | Fondo secundario |
| 300 | Más claro | Bordes normales |
| 400 | Medio-claro | Texto secundario |
| 500 | Medio | Base de color |
| 600 | Medio-oscuro | Hover principal |
| 700 | Oscuro | Estados activos |
| 800 | Más oscuro | Texto fuerte |
| 900 | Muy oscuro | Máximo contraste |

---

## Referencia Rápida de Spacing

```
0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 
60, 64, 72, 80, 96
```

---

## Estadísticas

- **Utilidades Tailwind**: 1000+ clases
- **Colores**: 9+ paletas con 10 niveles
- **Breakpoints**: 5 breakpoints principales
- **Animaciones**: 4+ animaciones predefinidas
- **Configurabilidad**: Totalmente personalizable

---

## Recursos Externos

- **Documentación oficial**: https://tailwindcss.com
- **Configuración**: https://tailwindcss.com/docs/configuration
- **Ejemplos interactivos**: https://play.tailwindcss.com
- **Comunidad**: https://tailwindcss.com/community

---

**Última actualización:** Enero 2026  
**Versión:** Tailwind CSS v4.1  
**Autor:** Experto en Tailwind CSS
