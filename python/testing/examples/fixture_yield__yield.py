"""
Objetivo: Fixture con setup y teardown
Referencia: yield
Tipo: keyword
Nivel: basico
"""

import pytest

@pytest.fixture
def archivo_temporal():
    """Fixture que prepara y limpia"""
    # SETUP: Crear archivo
    print("\\nCreando archivo...")
    archivo = open("temp.txt", "w")
    archivo.write("datos temporales")
    
    yield archivo  # El test usa el archivo aquí
    
    # TEARDOWN: Limpiar
    print("\\nCerrando archivo...")
    archivo.close()
    import os
    os.remove("temp.txt")

def test_archivo_existe(archivo_temporal):
    """Test que usa el archivo"""
    assert archivo_temporal.name == "temp.txt"

"""output
test_archivo_existe PASSED
Creando archivo...
Cerrando archivo...
"""
