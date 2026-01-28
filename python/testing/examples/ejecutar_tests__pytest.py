"""
Objetivo: Cómo ejecutar tests con pytest
Referencia: pytest
Tipo: comando
Nivel: basico
"""

# COMANDOS PARA EJECUTAR TESTS:

# 1. Correr un archivo de tests:
#    pytest nombre_archivo.py

# 2. Correr con verbosidad:
#    pytest nombre_archivo.py -v

# 3. Correr con output detallado:
#    pytest nombre_archivo.py -vv

# 4. Mostrar print statements:
#    pytest nombre_archivo.py -s

# 5. Parar en el primer error:
#    pytest nombre_archivo.py -x

# 6. Correr solo tests con keyword:
#    pytest -k "suma" nombre_archivo.py

# 7. Correr solo markers:
#    pytest -m "fast" nombre_archivo.py

# 8. Coverage (necesita pytest-cov):
#    pytest --cov=. nombre_archivo.py

# 9. Modo watch (re-ejecuta al cambiar):
#    pytest-watch nombre_archivo.py

# 10. Generar reporte:
#     pytest --html=report.html nombre_archivo.py

"""
