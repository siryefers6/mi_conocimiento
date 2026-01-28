#!/usr/bin/env python3
"""
ÍNDICE MAESTRO - Python POO Chuleta
Ejecuta este script para ver un resumen de todos los ejemplos disponibles
"""

import os
import re

def extract_objetivo(filepath):
    """Extrae el objetivo del docstring del archivo"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'Objetivo: (.+?)\\n', content)
            if match:
                return match.group(1).strip()
    except:
        pass
    return "Sin descripción"

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(base_dir, 'examples')
    
    if not os.path.exists(examples_dir):
        print("❌ No se encontró el directorio 'examples/'")
        return
    
    # Agrupar por categoría
    categorias = {
        'Conceptos Fundamentales': [],
        'Métodos': [],
        'Propiedades': [],
        'Herencia': [],
        'Polimorfismo': [],
        'Métodos Especiales': [],
        'Composición': [],
        'Estructuras de Datos': [],
        'Patrones': [],
        'Dataclasses': []
    }
    
    archivos = sorted([f for f in os.listdir(examples_dir) if f.endswith('.py')])
    
    # Clasificar archivos
    for archivo in archivos:
        filepath = os.path.join(examples_dir, archivo)
        objetivo = extract_objetivo(filepath)
        
        if 'clase_' in archivo or 'objeto_' in archivo or 'instancia_' in archivo or 'atributo_' in archivo:
            categorias['Conceptos Fundamentales'].append((archivo, objetivo))
        elif 'metodo_' in archivo and 'especial' not in archivo:
            categorias['Métodos'].append((archivo, objetivo))
        elif 'propiedad_' in archivo or 'encapsulamiento_' in archivo:
            categorias['Propiedades'].append((archivo, objetivo))
        elif 'herencia_' in archivo:
            categorias['Herencia'].append((archivo, objetivo))
        elif 'polimorfismo_' in archivo or 'duck_' in archivo:
            categorias['Polimorfismo'].append((archivo, objetivo))
        elif 'especial_' in archivo or 'metodo_especial_' in archivo or '__' in archivo.split('__')[1]:
            categorias['Métodos Especiales'].append((archivo, objetivo))
        elif 'composicion_' in archivo or 'agregacion_' in archivo:
            categorias['Composición'].append((archivo, objetivo))
        elif 'estructura_' in archivo or 'generador_' in archivo:
            categorias['Estructuras de Datos'].append((archivo, objetivo))
        elif 'patron_' in archivo or 'singleton_' in archivo or 'factory_' in archivo or 'decorador_' in archivo or 'excepc_' in archivo or 'operadores_' in archivo or 'comparacion_' in archivo or 'encapsulamiento_' in archivo:
            categorias['Patrones'].append((archivo, objetivo))
        elif 'dataclass_' in archivo or 'typing_' in archivo or 'metaclass_' in archivo:
            categorias['Dataclasses'].append((archivo, objetivo))
        else:
            # Por defecto a Patrones
            categorias['Patrones'].append((archivo, objetivo))
    
    # Mostrar
    print("\\n" + "="*70)
    print("PYTHON POO - ÍNDICE MAESTRO DE EJEMPLOS".center(70))
    print("="*70 + "\\n")
    
    total_ejemplos = 0
    
    for categoria, archivos_cat in categorias.items():
        if archivos_cat:
            print(f"\\n📚 {categoria.upper()}")
            print("─" * 70)
            for i, (archivo, objetivo) in enumerate(archivos_cat, 1):
                print(f"  {i:2d}. {archivo:50s} - {objetivo[:18]}")
            total_ejemplos += len(archivos_cat)
    
    print("\\n" + "="*70)
    print(f"Total de ejemplos: {total_ejemplos}".rjust(70))
    print("="*70 + "\\n")
    
    print("💡 TIP: Ejecuta cualquier ejemplo con:")
    print("   python examples/nombre_archivo.py")
    print()

if __name__ == '__main__':
    main()
