# FastAPI - Chuleta Completa

**Descripción**: Guía completa de FastAPI con ejemplos prácticos y ejecutables para construir APIs REST modernas con Python.

**Requisitos**: 
```bash
pip install fastapi uvicorn pydantic python-multipart python-jose[cryptography] passlib
```

**Ejecución de ejemplos**:
```bash
uvicorn examples/archivo:app --reload
# Luego visita http://localhost:8000/docs para explorar la API
```

---

## 📚 Contenidos

### 1. Conceptos Fundamentales
Primera aplicación, rutas básicas, parámetros de ruta y query.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Primera aplicación | Crear tu primer endpoint | [ver](examples/app_basica__basico.py) |
| Rutas GET | Endpoints simples GET | [ver](examples/ruta_get__get.py) |
| Parámetros de ruta | Capturar parámetros en la URL | [ver](examples/parametro_ruta__path.py) |
| Parámetros de query | Parámetros opcionales en query string | [ver](examples/parametro_query__query.py) |
| Múltiples parámetros | Combinar ruta y query | [ver](examples/parametro_multiple__multiple.py) |
| Tipos de datos | Type hints y validación automática | [ver](examples/tipo_datos__typing.py) |
| Body request | Recibir JSON en el cuerpo | [ver](examples/body_basico__body.py) |

### 2. Métodos HTTP
POST, PUT, DELETE, PATCH y sus diferencias.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Método POST | Crear recursos | [ver](examples/metodo_post__post.py) |
| Método PUT | Reemplazar recursos completos | [ver](examples/metodo_put__put.py) |
| Método PATCH | Actualizar parcialmente | [ver](examples/metodo_patch__patch.py) |
| Método DELETE | Eliminar recursos | [ver](examples/metodo_delete__delete.py) |

### 3. Modelos y Validación
Pydantic, validación automática, modelos anidados.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Modelo Pydantic básico | Definir estructura de datos | [ver](examples/modelo_basico__pydantic.py) |
| Validación con Query() | Validadores en parámetros | [ver](examples/parametro_query_validado__query_validation.py) |
| Validación de campos | Validadores complejos | [ver](examples/validacion_campo__validator.py) |
| Modelos anidados | Estructuras complejas | [ver](examples/modelo_anidado__nested.py) |
| Valores por defecto | Parámetros opcionales | [ver](examples/modelo_defecto__default.py) |
| Validador personalizado | Lógica de validación custom | [ver](examples/validador_custom__custom_validator.py) |

### 4. Cuerpos de Solicitud
Request bodies, formularios, múltiples parámetros.

| Concepto | Descripción | Ejemplo |
|------básico | Recibir JSON | [ver](examples/body_basico__body.py) |
| Body múltiple | Varios parámetros body | [ver](examples/body_multiple__multiple.py) |
| Ejemplo en esquema | Documentación con ejemplos | [ver](examples/body_ejemplo__example.py) |
| Formularios HTML | Recibir form-data | [ver](examples/formulario_basico__form.py) |
| Archivos | Subir archivos | [ver](examples/archivo_subir__upload.py) |

### 5. Respuestas
Códigos HTTP, modelos de respuesta, excepciones.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Código de estado | Status codes personalizados | [ver](examples/respuesta_status__status_code.py) |
| Modelo de respuesta | Response model specification | [ver](examples/respuesta_modelo__response_model.py) |
| Respuesta lista | Arrays en respuestas | [ver](examples/respuesta_lista__list.py) |
| Excepción HTTP | HTTPException para errores | [ver](examples/excepcion_http__http_exception.py) |
| Respuesta HTML | Retornar contenido HTML | [ver](examples/respuesta_html__html.py) |
| Excepción HTTP | HTTPException para errores | [ver](examples/excepcion_http__http_exception
### 6. Dependencias
Inyección de dependencias, parámetros compartidos.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Dependencia simple | Función reutilizable | [ver](examples/dependencia_basica__dependency.py) |
| Dependencia con parámetros | Dependencias parametrizadas | [ver](examples/dependencia_param__parametrized.py) |
| Sub-dependencias | Dependencias anidadas | [ver](examples/dependencia_sub__subdependency.py) |
| Dependencia en query | Validar query con dependencias | [ver](examples/dependencia_query__query_dependency.py) |
| Guards de auth | Proteger endpoints | [ver](examples/auth_guard__guard.py) |

### 7. Autenticación y Seguridad
OAuth2, JWT, Bearer tokens, API Keys.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| API Key simple | Autenticación con API Key | [ver](examples/seguridad_apikey__api_key.py) |
| Bearer Token | Tokens en headers | [ver](examples/seguridad_bearer__bearer.py) |
| OAuth2 password | Flujo OAuth2 simple | [ver](examples/oauth2_password__oauth2.py) |
| JWT Token | JSON Web Tokens | [ver](examples/jwt_basico__jwt.py) |
| Autenticación persistente | Guards en endpoints | [ver](examples/auth_guard__guard.py) |

### 8. CORS y Middleware
Configuración de CORS, middleware personalizado.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| CORS básico | Habilitar CORS | [ver](examples/cors_basico__cors.py) |
| CORS avanzado | Configuración personalizada | [ver](examples/cors_avanzado__advanced.py) |
| Middleware simple | Custom middleware | [ver](examples/middleware_basico__middleware.py) |
| Middleware de timing | Medir tiempo de respuesta | [ver](examples/middleware_timing__timing.py) |

### 9. Documentación y OpenAPI
Documentación automática, customización de OpenAPI.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Documentación automática | /docs y /redoc | [ver](examples/docs_automatica__docs.py) |
| Descripciones en endpoints | Documentar funciones | [ver](examples/endpoint_descripcion__description.py) |
| Tags y ejemplos | Organizar docs | [ver](examples/docs_tags__tags.py) |
| OpenAPI personalizado | Customizar OpenAPI schema | [ver](examples/openapi_custom__custom.py) |

### 10. Testing
TestClient, tests unitarios, fixtures.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| TestClient básico | Probar endpoints | [ver](examples/test_basico__testclient.py) |
| Test GET | Probar métodos GET | [ver](examples/test_get__get.py) |
| Test POST | Probar métodos POST | [ver](examples/test_post__post.py) |
| Tests con fixtures | Fixtures para testing | [ver](examples/test_fixture__fixture.py) |
| Tests parametrizados | Múltiples casos | [ver](examples/test_parametrizado__parametrize.py) |

### 11. Estructura de Proyectos
Organización, routers, variables de entorno.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Routers | Organizar endpoints | [ver](examples/router_basico__router.py) |
| Estructura modular | Separar por funcionalidad | [ver](examples/estructura_modular__modular.py) |
| Variables de entorno | Configuración con .env | [ver](examples/config_env__environment.py) |
| Inicio y cierre | Lifespan events | [ver](examples/lifespan_eventos__lifespan.py) |

### 12. Características Avanzadas
Streaming, WebSockets, Background tasks.

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Tareas en background | Ejecutar después de responder | [ver](examples/background_task__background.py) |
| Respuesta streaming | Enviar datos gradualmente | [ver](examples/streaming_respuesta__streaming.py) |
| WebSocket simple | Conexiones bidireccionales | [ver](examples/websocket_basico__websocket.py) |

---

## 📊 Estadísticas

- **Total de ejemplos**: 40+
- **Conceptos cubiertos**: 50+
- **Nivel**: Básico a Avanzado
- **Tiempo aproximado**: 4-6 horas

## 🎯 Recomendación de aprendizaje

1. **Semana 1**: Conceptos Fundamentales → Métodos HTTP → Modelos
2. **Semana 2**: Cuerpos de solicitud → Respuestas → Dependencias
3. **Semana 3**: Autenticación → CORS → Documentación
4. **Semana 4**: Testing → Estructura de proyectos → Características avanzadas

## 🔗 Referencias

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [OpenAPI Spec](https://spec.openapis.org/)
- [OAuth2 RFC 6749](https://tools.ietf.org/html/rfc6749)

---

**Última actualización**: Enero 2026
