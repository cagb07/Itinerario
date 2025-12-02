"""
🧪 Script de Pruebas Automatizadas
Sistema de Control de Informes
"""

import os
import pandas as pd
from datetime import datetime

# Colores para terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_test(name, status, message=""):
    """Imprime resultado de test con colores"""
    if status == "PASS":
        print(f"{Colors.GREEN}✅ PASS{Colors.END} - {name}")
    elif status == "FAIL":
        print(f"{Colors.RED}❌ FAIL{Colors.END} - {name}: {message}")
    elif status == "WARN":
        print(f"{Colors.YELLOW}⚠️  WARN{Colors.END} - {name}: {message}")
    else:
        print(f"{Colors.BLUE}ℹ️  INFO{Colors.END} - {name}: {message}")

def test_archivos_principales():
    """Test 1: Verificar archivos principales"""
    print("\n" + "="*60)
    print("TEST 1: VERIFICACIÓN DE ARCHIVOS PRINCIPALES")
    print("="*60)
    
    archivos_requeridos = {
        "app.py": "Aplicación principal",
        "calendario_module.py": "Módulo de calendario",
        "requirements.txt": "Dependencias",
        ".streamlit/config.toml": "Configuración",
        "LISTADO-CON-FASES.csv": "Base de datos de centros",
        "seguimiento_informes.csv": "Datos de Kanban",
        "calendario.csv": "Datos de calendario"
    }
    
    total = len(archivos_requeridos)
    passed = 0
    
    for archivo, descripcion in archivos_requeridos.items():
        if os.path.exists(archivo):
            size = os.path.getsize(archivo)
            print_test(f"{descripcion} ({archivo})", "PASS", f"{size:,} bytes")
            passed += 1
        else:
            print_test(f"{descripcion} ({archivo})", "FAIL", "Archivo no encontrado")
    
    print(f"\nResultado: {passed}/{total} archivos encontrados")
    return passed == total

def test_scripts_inicio():
    """Test 2: Verificar scripts de inicio"""
    print("\n" + "="*60)
    print("TEST 2: VERIFICACIÓN DE SCRIPTS DE INICIO")
    print("="*60)
    
    scripts = {
        "INICIAR.bat": "Script principal de inicio",
        "INICIO_RAPIDO.bat": "Script de inicio rápido",
        "DETENER.bat": "Script para detener",
        "backup.bat": "Script de backup"
    }
    
    total = len(scripts)
    passed = 0
    
    for script, descripcion in scripts.items():
        if os.path.exists(script):
            print_test(f"{descripcion} ({script})", "PASS")
            passed += 1
        else:
            print_test(f"{descripcion} ({script})", "FAIL", "Script no encontrado")
    
    print(f"\nResultado: {passed}/{total} scripts encontrados")
    return passed == total

def test_estructura_csv_seguimiento():
    """Test 3: Verificar estructura de seguimiento_informes.csv"""
    print("\n" + "="*60)
    print("TEST 3: ESTRUCTURA DE seguimiento_informes.csv")
    print("="*60)
    
    try:
        df = pd.read_csv("seguimiento_informes.csv")
        
        columnas_requeridas = ["ID", "Centro", "Estado", "Fecha_Inicio", "Fecha_Fin", 
                               "Responsable", "Prioridad", "Observaciones"]
        
        print(f"Registros encontrados: {len(df)}")
        print(f"Columnas encontradas: {list(df.columns)}")
        
        passed = 0
        total = len(columnas_requeridas)
        
        for col in columnas_requeridas:
            if col in df.columns:
                print_test(f"Columna '{col}'", "PASS")
                passed += 1
            else:
                print_test(f"Columna '{col}'", "FAIL", "Columna faltante")
        
        # Verificar estados
        print("\n📊 Distribución por Estado:")
        if 'Estado' in df.columns:
            estados = df['Estado'].value_counts()
            for estado, count in estados.items():
                print(f"  {estado}: {count}")
        
        # Verificar observaciones
        if 'Observaciones' in df.columns:
            con_obs = df['Observaciones'].notna().sum()
            sin_obs = len(df) - con_obs
            print(f"\n💬 Observaciones:")
            print(f"  Con observaciones: {con_obs}")
            print(f"  Sin observaciones: {sin_obs}")
        
        print(f"\nResultado: {passed}/{total} columnas correctas")
        return passed == total
        
    except Exception as e:
        print_test("Lectura de CSV", "FAIL", str(e))
        return False

def test_estructura_csv_calendario():
    """Test 4: Verificar estructura de calendario.csv"""
    print("\n" + "="*60)
    print("TEST 4: ESTRUCTURA DE calendario.csv")
    print("="*60)
    
    try:
        df = pd.read_csv("calendario.csv")
        
        columnas_requeridas = ["ID_Cita", "Fecha", "Hora", "Centro", "Provincia", 
                               "Canton", "Categoria", "Prioridad", "Nota", "Estado", "Fecha_Creacion"]
        
        print(f"Citas encontradas: {len(df)}")
        print(f"Columnas encontradas: {list(df.columns)}")
        
        passed = 0
        total = len(columnas_requeridas)
        
        for col in columnas_requeridas:
            if col in df.columns:
                print_test(f"Columna '{col}'", "PASS")
                passed += 1
            else:
                print_test(f"Columna '{col}'", "FAIL", "Columna faltante")
        
        # Verificar distribución por fecha
        if 'Fecha' in df.columns:
            print("\n📅 Citas por Fecha:")
            fechas = df['Fecha'].value_counts().sort_index()
            for fecha, count in fechas.items():
                print(f"  {fecha}: {count} citas")
        
        print(f"\nResultado: {passed}/{total} columnas correctas")
        return passed == total
        
    except Exception as e:
        print_test("Lectura de CSV", "FAIL", str(e))
        return False

def test_integridad_datos():
    """Test 5: Verificar integridad de datos"""
    print("\n" + "="*60)
    print("TEST 5: INTEGRIDAD DE DATOS")
    print("="*60)
    
    tests_passed = 0
    total_tests = 0
    
    # Test 5.1: IDs únicos en seguimiento
    try:
        df_seg = pd.read_csv("seguimiento_informes.csv")
        total_tests += 1
        if df_seg['ID'].is_unique:
            print_test("IDs únicos en seguimiento", "PASS")
            tests_passed += 1
        else:
            duplicados = df_seg[df_seg['ID'].duplicated()]['ID'].tolist()
            print_test("IDs únicos en seguimiento", "FAIL", f"IDs duplicados: {duplicados}")
    except Exception as e:
        print_test("IDs únicos en seguimiento", "FAIL", str(e))
    
    # Test 5.2: IDs únicos en calendario
    try:
        df_cal = pd.read_csv("calendario.csv")
        total_tests += 1
        if df_cal['ID_Cita'].is_unique:
            print_test("IDs únicos en calendario", "PASS")
            tests_passed += 1
        else:
            duplicados = df_cal[df_cal['ID_Cita'].duplicated()]['ID_Cita'].tolist()
            print_test("IDs únicos en calendario", "FAIL", f"IDs duplicados: {duplicados}")
    except Exception as e:
        print_test("IDs únicos en calendario", "FAIL", str(e))
    
    # Test 5.3: Estados válidos
    try:
        estados_validos = ["Pendiente", "En Proceso", "Pausado", "Terminado"]
        total_tests += 1
        estados_invalidos = df_seg[~df_seg['Estado'].isin(estados_validos)]['Estado'].unique()
        if len(estados_invalidos) == 0:
            print_test("Estados válidos", "PASS")
            tests_passed += 1
        else:
            print_test("Estados válidos", "FAIL", f"Estados inválidos: {list(estados_invalidos)}")
    except Exception as e:
        print_test("Estados válidos", "FAIL", str(e))
    
    # Test 5.4: Fechas válidas
    try:
        total_tests += 1
        df_seg['Fecha_Inicio'] = pd.to_datetime(df_seg['Fecha_Inicio'], errors='coerce')
        fechas_invalidas = df_seg['Fecha_Inicio'].isna().sum()
        if fechas_invalidas == 0:
            print_test("Fechas válidas", "PASS")
            tests_passed += 1
        else:
            print_test("Fechas válidas", "WARN", f"{fechas_invalidas} fechas inválidas")
    except Exception as e:
        print_test("Fechas válidas", "FAIL", str(e))
    
    print(f"\nResultado: {tests_passed}/{total_tests} tests de integridad pasados")
    return tests_passed == total_tests

def test_documentacion():
    """Test 6: Verificar documentación"""
    print("\n" + "="*60)
    print("TEST 6: VERIFICACIÓN DE DOCUMENTACIÓN")
    print("="*60)
    
    docs = {
        "README.md": "Documentación principal",
        "DEPLOY.md": "Guía de despliegue",
        "QUICKSTART.md": "Inicio rápido",
        "MEJORAS_CALENDARIO.md": "Funcionalidades del calendario",
        "GESTION_CENTROS.md": "Gestión de centros",
        "KANBAN_MEJORADO.md": "Kanban mejorado",
        "KANBAN_PAUSADO.md": "Estado pausado",
        "REPORTES_KANBAN.md": "Sistema de reportes",
        "SCRIPTS_GUIA.md": "Guía de scripts",
        "SOLUCION_PERDIDA_DATOS.md": "Solución pérdida de datos",
        "PLAN_PRUEBAS.md": "Plan de pruebas"
    }
    
    total = len(docs)
    passed = 0
    
    for doc, descripcion in docs.items():
        if os.path.exists(doc):
            size = os.path.getsize(doc)
            print_test(f"{descripcion} ({doc})", "PASS", f"{size:,} bytes")
            passed += 1
        else:
            print_test(f"{descripcion} ({doc})", "WARN", "Documento no encontrado")
    
    print(f"\nResultado: {passed}/{total} documentos encontrados")
    return passed >= total * 0.8  # 80% de documentos requeridos

def test_backup_system():
    """Test 7: Verificar sistema de backup"""
    print("\n" + "="*60)
    print("TEST 7: SISTEMA DE BACKUP")
    print("="*60)
    
    tests_passed = 0
    total_tests = 0
    
    # Test 7.1: Script de backup existe
    total_tests += 1
    if os.path.exists("backup.bat"):
        print_test("Script backup.bat", "PASS")
        tests_passed += 1
    else:
        print_test("Script backup.bat", "FAIL", "Script no encontrado")
    
    # Test 7.2: Carpeta backups
    total_tests += 1
    if os.path.exists("backups"):
        backups = os.listdir("backups")
        print_test("Carpeta backups", "PASS", f"{len(backups)} backups encontrados")
        tests_passed += 1
    else:
        print_test("Carpeta backups", "INFO", "Carpeta no existe (se creará al ejecutar backup)")
        tests_passed += 1  # No es crítico
    
    # Test 7.3: Archivo backup temporal
    total_tests += 1
    if os.path.exists("seguimiento_informes.csv.backup"):
        print_test("Backup temporal", "INFO", "Existe backup temporal")
    else:
        print_test("Backup temporal", "INFO", "No hay backup temporal (normal)")
    tests_passed += 1  # No es crítico
    
    print(f"\nResultado: {tests_passed}/{total_tests} tests de backup pasados")
    return tests_passed >= total_tests * 0.7

def generar_reporte():
    """Genera reporte final de pruebas"""
    print("\n" + "="*80)
    print(" "*25 + "📊 REPORTE FINAL DE PRUEBAS")
    print("="*80)
    
    resultados = {
        "Archivos Principales": test_archivos_principales(),
        "Scripts de Inicio": test_scripts_inicio(),
        "Estructura CSV Seguimiento": test_estructura_csv_seguimiento(),
        "Estructura CSV Calendario": test_estructura_csv_calendario(),
        "Integridad de Datos": test_integridad_datos(),
        "Documentación": test_documentacion(),
        "Sistema de Backup": test_backup_system()
    }
    
    print("\n" + "="*80)
    print("RESUMEN DE RESULTADOS")
    print("="*80)
    
    total_tests = len(resultados)
    passed_tests = sum(resultados.values())
    
    for test_name, passed in resultados.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        color = Colors.GREEN if passed else Colors.RED
        print(f"{color}{status}{Colors.END} - {test_name}")
    
    print("\n" + "="*80)
    porcentaje = (passed_tests / total_tests) * 100
    print(f"TOTAL: {passed_tests}/{total_tests} tests pasados ({porcentaje:.1f}%)")
    
    if porcentaje == 100:
        print(f"{Colors.GREEN}🎉 ¡TODOS LOS TESTS PASARON!{Colors.END}")
        print("✅ El sistema está listo para usar")
    elif porcentaje >= 80:
        print(f"{Colors.YELLOW}⚠️  La mayoría de tests pasaron{Colors.END}")
        print("⚠️  Revisa los tests fallidos antes de usar en producción")
    else:
        print(f"{Colors.RED}❌ MUCHOS TESTS FALLARON{Colors.END}")
        print("❌ NO usar en producción hasta corregir los problemas")
    
    print("="*80)
    print(f"\nFecha de pruebas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Ubicación: {os.getcwd()}")
    print("\n📝 Para pruebas manuales, consulta: PLAN_PRUEBAS.md")
    print("="*80)

if __name__ == "__main__":
    print(f"{Colors.BLUE}")
    print("="*80)
    print(" "*20 + "🧪 SISTEMA DE PRUEBAS AUTOMATIZADAS")
    print(" "*20 + "Sistema de Control de Informes v2.0")
    print("="*80)
    print(f"{Colors.END}")
    
    generar_reporte()
