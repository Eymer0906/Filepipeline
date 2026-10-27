# ============================================================
#  pruebas_demo.py  –  
# ============================================================
#  Este script simula dos escenarios:
#  1. Escenario EXITOSO: archivo procesado de principio a fin
#  2. Escenario ERROR: fallo de conexión a Drive controlado
# ============================================================

import os
import time
import shutil
from pathlib import Path

BASE_DIR = Path("C:/FilePipeline")
ENTRADA = BASE_DIR / "entrada"
BACKUP = BASE_DIR / "backup"

# Asegurar carpetas
ENTRADA.mkdir(parents=True, exist_ok=True)
BACKUP.mkdir(parents=True, exist_ok=True)

def limpiar():
    """Limpia carpetas para una demo limpia."""
    for f in ENTRADA.glob("*"):
        if f.is_file(): f.unlink()
    for f in BACKUP.glob("*"):
        if f.is_file(): f.unlink()
    print(" Carpetas limpiadas para la demo.")

def crear_archivo_prueba(nombre, contenido="Este es un archivo de prueba para FilePipeline."):
    """Crea un archivo de prueba en la carpeta entrada."""
    ruta = ENTRADA / nombre
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f" Archivo creado: {nombre}")
    return ruta

def escenario_exitoso():
    """
    DEMO 1: Escenario exitoso completo.
    Pasos para mostrar en el video:
    1. Mostrar carpeta entrada vacía
    2. Ejecutar este script (o soltar archivo manualmente)
    3. Mostrar logs del pipeline
    4. Mostrar archivo en backup/
    5. Mostrar registro en archivos.db (con DB Browser)
    6. Mostrar archivo en Google Drive
    7. Mostrar Dashboard en localhost:5000
    """
    print("\n" + "="*60)
    print("  DEMO 1: ESCENARIO EXITOSO")
    print("="*60)
    limpiar()

    # Crear archivo de prueba
    archivo = crear_archivo_prueba("demo_contrato.txt", 
        "CONTRATO DE SERVICIOS\n\nCliente: Empresa XYZ\nMonto: $50,000\nFecha: 2024-09-21")

    print("\n Ahora el pipeline detectará el archivo automáticamente...")
    print("   (Asegúrate de tener pipeline.py corriendo en otra terminal)")
    print("\n PASOS A MOSTRAR EN EL VIDEO:")
    print("   1. Mostrar carpeta entrada/ con el archivo")
    print("   2. Cambiar a terminal del pipeline → mostrar logs")
    print("   3. Mostrar carpeta backup/ → archivo movido")
    print("   4. Abrir DB Browser → mostrar tabla 'archivos'")
    print("   5. Abrir Google Drive → mostrar archivo subido")
    print("   6. Abrir navegador → localhost:5000 → mostrar dashboard")
    print("="*60)

def escenario_error():
    """
    DEMO 2: Escenario con error controlado (sin internet).
    Pasos para mostrar en el video:
    1. Desconectar WiFi / Ethernet
    2. Crear archivo de prueba
    3. Mostrar que el pipeline detecta y mueve el archivo
    4. Mostrar error en logs al intentar subir a Drive
    5. Mostrar BD: drive_id = NULL
    6. Mostrar Dashboard: estado 'Pendiente'
    7. Reconectar internet (opcional: mostrar reintento manual)
    """
    print("\n" + "="*60)
    print("  DEMO 2: ESCENARIO CON ERROR CONTROLADO")
    print("="*60)
    limpiar()

    print("\n  IMPORTANTE: Desconecta tu internet antes de continuar.")
    input("   Presiona ENTER cuando estés desconectado...")

    archivo = crear_archivo_prueba("demo_error.xlsx",
        "REPORTE\nVentas,Q3\nProducto A,15000\nProducto B,23000")

    print("\n El pipeline intentará procesar pero fallará al subir a Drive...")
    print("\n PASOS A MOSTRAR EN EL VIDEO:")
    print("   1. Mostrar icono de 'Sin conexión' en Windows")
    print("   2. Soltar archivo en entrada/")
    print("   3. Mostrar terminal del pipeline → error de red")
    print("   4. Abrir DB Browser → drive_id es NULL")
    print("   5. Dashboard → columna Drive muestra 'Pendiente'")
    print("   6. Reconectar internet (opcional)")
    print("="*60)

def escenario_dashboard():
    """
    DEMO 3: Navegación por el Dashboard Web.
    Muestra las consultas SQL predefinidas.
    """
    print("\n" + "="*60)
    print("  DEMO 3: DASHBOARD WEB")
    print("="*60)
    print("\n PASOS A MOSTRAR EN EL VIDEO:")
    print("   1. Abrir http://localhost:5000")
    print("   2. Mostrar KPIs: Total, Espacio, Drive, Tipos")
    print("   3. Mostrar tabla de archivos recientes")
    print("   4. Usar barra de búsqueda")
    print("   5. Mostrar gráfico de distribución por tipo")
    print("   6. Mostrar logs recientes")
    print("   7. Hacer clic en cada consulta SQL predefinida:")
    print("      • Últimos 20 archivos")
    print("      • Archivos NO subidos a Drive")
    print("      • Archivos por día (últimos 7)")
    print("      • Espacio total respaldado")
    print("="*60)

if __name__ == "__main__":
    print("="*60)
    print("  FilePipeline - Script de Pruebas para Video Académico")
    print("="*60)
    print("\nSelecciona el escenario a grabar:")
    print("  [1] Escenario EXITOSO")
    print("  [2] Escenario con ERROR controlado")
    print("  [3] Guía de navegación DASHBOARD")
    print("  [4] TODOS los escenarios (secuencial)")

    opcion = input("\nOpción (1-4): ").strip()

    if opcion == "1":
        escenario_exitoso()
    elif opcion == "2":
        escenario_error()
    elif opcion == "3":
        escenario_dashboard()
    elif opcion == "4":
        escenario_exitoso()
        time.sleep(2)
        escenario_error()
        time.sleep(2)
        escenario_dashboard()
    else:
        print("Opción no válida.")