"""
Objetivo: Crear decorador propio
Referencia: @decorator
Tipo: decorador
Nivel: basico
"""

def requerimiento_login(func):
    def envoltura(*args, **kwargs):
        print("Verificando login...")
        usuario = kwargs.get("usuario")
        if usuario != "admin":
            print("Acceso denegado")
            return None
        return func(*args, **kwargs)
    return envoltura

@requerimiento_login
def ver_datos(usuario=None):
    return "Datos confidenciales"

print(ver_datos(usuario="admin"))
print(ver_datos(usuario="visitante"))

"""output
Verificando login...
Datos confidenciales
Verificando login...
Acceso denegado
"""
