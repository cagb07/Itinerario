"""
🔍 Script de Verificación y Sincronización de Centros
Asegura que todos los centros estén en el seguimiento
"""

import pandas as pd
import os
from datetime import datetime

def verificar_sincronizacion():
    """Verifica que todos los centros estén en el seguimiento"""
    
    print("="*80)
    print("🔍 VERIFICACIÓN DE SINCRONIZACIÓN DE CENTROS")
    print("="*80)
    print()
    
    # Cargar datos
    print("📂 Cargando datos...")
    
    # Cargar centros educativos
    if not os.path.exists("LISTADO-CON-FASES.csv"):
        print("❌ ERROR: No se encuentra LISTADO-CON-FASES.csv")
        return
    
    df_centros = pd.read_csv("LISTADO-CON-FASES.csv")
    print(f"✅ Centros cargados: {len(df_centros)}")
    
    # Mostrar columnas para debugging
    print(f"📋 Columnas encontradas: {list(df_centros.columns[:5])}...")
    
    # Normalizar nombres de columnas
    df_centros.columns = df_centros.columns.str.upper().str.strip()
    
    # Identificar columna de nombre - buscar en varias posibles
    nombre_col = None
    
    # Opción 1: Buscar columna con "NOMBRE" en el nombre
    for col in df_centros.columns:
        if 'NOMBRE' in col:
            nombre_col = col
            print(f"✅ Columna de nombre encontrada: {nombre_col}")
            break
    
    # Opción 2: Si no se encuentra, buscar columnas con texto (no números)
    if not nombre_col:
        print("⚠️  No se encontró columna 'NOMBRE', buscando columna con nombres de centros...")
        
        # Mostrar primeras filas para ver estructura
        print("\n📊 Primeras 3 filas del CSV:")
        print(df_centros.head(3).to_string())
        print()
        
        # Buscar columna que contenga texto largo (nombres de centros)
        for col in df_centros.columns:
            if df_centros[col].dtype == 'object':  # Es texto
                # Verificar que tiene valores y no son muy cortos
                sample_values = df_centros[col].dropna().head(5)
                if len(sample_values) > 0:
                    avg_length = sample_values.astype(str).str.len().mean()
                    if avg_length > 10:  # Nombres de centros suelen ser largos
                        nombre_col = col
                        print(f"✅ Columna de nombre detectada automáticamente: {nombre_col}")
                        print(f"   Ejemplos: {list(sample_values[:3])}")
                        break
    
    if not nombre_col:
        print("❌ ERROR: No se pudo identificar la columna de nombres")
        print("📋 Columnas disponibles:")
        for i, col in enumerate(df_centros.columns, 1):
            print(f"   {i}. {col} (tipo: {df_centros[col].dtype})")
        print()
        print("💡 Por favor, indica el número de la columna que contiene los nombres de centros:")
        try:
            col_num = int(input("Número de columna: ").strip()) - 1
            if 0 <= col_num < len(df_centros.columns):
                nombre_col = df_centros.columns[col_num]
                print(f"✅ Usando columna: {nombre_col}")
            else:
                print("❌ Número inválido")
                return
        except:
            print("❌ Entrada inválida")
            return
    
    # Cargar seguimiento
    if os.path.exists("seguimiento_informes.csv"):
        df_seguimiento = pd.read_csv("seguimiento_informes.csv")
        print(f"✅ Seguimiento cargado: {len(df_seguimiento)} informes")
    else:
        df_seguimiento = pd.DataFrame(columns=["ID", "Centro", "Estado", "Fecha_Inicio", 
                                                "Fecha_Fin", "Responsable", "Prioridad", "Observaciones"])
        print("⚠️  Archivo de seguimiento no existe, se creará nuevo")
    
    print()
    print("="*80)
    print("📊 ANÁLISIS DE COBERTURA")
    print("="*80)
    print()
    
    # Obtener lista de centros únicos
    centros_totales = set(df_centros[nombre_col].dropna().unique())
    centros_en_seguimiento = set(df_seguimiento['Centro'].dropna().unique()) if not df_seguimiento.empty else set()
    
    print(f"📚 Total de centros en base de datos: {len(centros_totales)}")
    print(f"📋 Centros en seguimiento: {len(centros_en_seguimiento)}")
    print()
    
    # Centros faltantes
    centros_faltantes = centros_totales - centros_en_seguimiento
    
    if centros_faltantes:
        print(f"⚠️  CENTROS FALTANTES EN SEGUIMIENTO: {len(centros_faltantes)}")
        print()
        print("="*80)
        print("🔧 OPCIONES DE SINCRONIZACIÓN")
        print("="*80)
        print()
        print("1. Agregar centros faltantes como 'Pendiente'")
        print("2. Ver lista de centros faltantes")
        print("3. Exportar lista de centros faltantes a CSV")
        print("4. Salir sin cambios")
        print()
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            agregar_centros_faltantes(df_centros, df_seguimiento, centros_faltantes, nombre_col)
        elif opcion == "2":
            mostrar_centros_faltantes(centros_faltantes)
        elif opcion == "3":
            exportar_centros_faltantes(df_centros, centros_faltantes, nombre_col)
        elif opcion == "4":
            print("✅ Saliendo sin cambios")
        else:
            print("❌ Opción inválida")
    else:
        print("✅ TODOS LOS CENTROS ESTÁN EN EL SEGUIMIENTO")
        print()
        print("📊 Distribución por Estado:")
        if not df_seguimiento.empty and 'Estado' in df_seguimiento.columns:
            estados = df_seguimiento['Estado'].value_counts()
            for estado, count in estados.items():
                print(f"  {estado}: {count}")

def agregar_centros_faltantes(df_centros, df_seguimiento, centros_faltantes, nombre_col):
    """Agrega centros faltantes al seguimiento como Pendiente"""
    
    print()
    print("="*80)
    print("➕ AGREGANDO CENTROS FALTANTES AL SEGUIMIENTO")
    print("="*80)
    print()
    
    # Crear backup
    if os.path.exists("seguimiento_informes.csv"):
        backup_name = f"seguimiento_informes_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df_seguimiento.to_csv(backup_name, index=False)
        print(f"💾 Backup creado: {backup_name}")
    
    # Obtener siguiente ID
    if not df_seguimiento.empty:
        max_id = df_seguimiento['ID'].max()
    else:
        max_id = 0
    
    # Crear nuevos registros
    nuevos_registros = []
    
    for i, centro in enumerate(sorted(centros_faltantes), start=1):
        # Obtener datos del centro
        centro_data = df_centros[df_centros[nombre_col] == centro]
        
        if not centro_data.empty:
            centro_data = centro_data.iloc[0]
            
            nuevo_registro = {
                "ID": max_id + i,
                "Centro": centro,
                "Estado": "Pendiente",
                "Fecha_Inicio": datetime.now().strftime("%Y-%m-%d"),
                "Fecha_Fin": None,
                "Responsable": "Sistema",
                "Prioridad": "Media",
                "Observaciones": f"Centro agregado automáticamente el {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            }
            
            nuevos_registros.append(nuevo_registro)
    
    # Crear DataFrame con nuevos registros
    df_nuevos = pd.DataFrame(nuevos_registros)
    
    # Combinar con seguimiento existente
    df_seguimiento_actualizado = pd.concat([df_seguimiento, df_nuevos], ignore_index=True)
    
    # Guardar
    df_seguimiento_actualizado.to_csv("seguimiento_informes.csv", index=False, encoding='utf-8')
    
    print(f"✅ {len(nuevos_registros)} centros agregados al seguimiento")
    print(f"📊 Total de informes ahora: {len(df_seguimiento_actualizado)}")
    print()
    print("="*80)
    print("✅ SINCRONIZACIÓN COMPLETADA")
    print("="*80)
    print()
    print("📋 Distribución actualizada por Estado:")
    estados = df_seguimiento_actualizado['Estado'].value_counts()
    for estado, count in estados.items():
        print(f"  {estado}: {count}")
    print()
    print("💡 Recuerda: Los centros agregados están en estado 'Pendiente'")
    print("   Puedes cambiar su estado desde el Kanban en la aplicación")

def mostrar_centros_faltantes(centros_faltantes):
    """Muestra lista de centros faltantes"""
    
    print()
    print("="*80)
    print(f"📋 LISTA DE CENTROS FALTANTES ({len(centros_faltantes)})")
    print("="*80)
    print()
    
    for i, centro in enumerate(sorted(centros_faltantes), start=1):
        print(f"{i:3d}. {centro}")
    
    print()
    print("="*80)

def exportar_centros_faltantes(df_centros, centros_faltantes, nombre_col):
    """Exporta centros faltantes a CSV"""
    
    print()
    print("="*80)
    print("📥 EXPORTANDO CENTROS FALTANTES")
    print("="*80)
    print()
    
    # Filtrar centros faltantes
    df_faltantes = df_centros[df_centros[nombre_col].isin(centros_faltantes)]
    
    # Nombre del archivo
    filename = f"centros_faltantes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    # Exportar
    df_faltantes.to_csv(filename, index=False, encoding='utf-8')
    
    print(f"✅ Archivo exportado: {filename}")
    print(f"📊 Centros exportados: {len(df_faltantes)}")
    print()
    print("💡 Puedes usar este archivo para:")
    print("   - Revisar qué centros faltan")
    print("   - Importarlos manualmente desde la aplicación")
    print("   - Hacer seguimiento de centros pendientes")

def generar_reporte_completo():
    """Genera reporte completo de sincronización"""
    
    print()
    print("="*80)
    print("📊 REPORTE COMPLETO DE SINCRONIZACIÓN")
    print("="*80)
    print()
    
    # Cargar datos
    if not os.path.exists("LISTADO-CON-FASES.csv"):
        print("❌ ERROR: No se encuentra LISTADO-CON-FASES.csv")
        return
    
    df_centros = pd.read_csv("LISTADO-CON-FASES.csv")
    df_centros.columns = df_centros.columns.str.upper().str.strip()
    
    nombre_col = None
    for col in df_centros.columns:
        if 'NOMBRE' in col:
            nombre_col = col
            break
    
    if os.path.exists("seguimiento_informes.csv"):
        df_seguimiento = pd.read_csv("seguimiento_informes.csv")
    else:
        df_seguimiento = pd.DataFrame()
    
    # Estadísticas
    total_centros = len(df_centros)
    centros_en_seguimiento = len(df_seguimiento) if not df_seguimiento.empty else 0
    
    print(f"📚 Total de Centros: {total_centros}")
    print(f"📋 En Seguimiento: {centros_en_seguimiento}")
    print(f"📊 Cobertura: {(centros_en_seguimiento/total_centros*100):.1f}%")
    print()
    
    if not df_seguimiento.empty and 'Estado' in df_seguimiento.columns:
        print("📈 Distribución por Estado:")
        estados = df_seguimiento['Estado'].value_counts()
        for estado, count in estados.items():
            porcentaje = (count / centros_en_seguimiento * 100)
            print(f"  {estado}: {count} ({porcentaje:.1f}%)")
        print()
    
    if not df_seguimiento.empty and 'Responsable' in df_seguimiento.columns:
        print("👥 Distribución por Responsable:")
        responsables = df_seguimiento['Responsable'].value_counts()
        for responsable, count in responsables.items():
            print(f"  {responsable}: {count}")
        print()
    
    # Guardar reporte
    reporte_filename = f"reporte_sincronizacion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(reporte_filename, 'w', encoding='utf-8') as f:
        f.write("REPORTE DE SINCRONIZACIÓN DE CENTROS\n")
        f.write("="*80 + "\n\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total de Centros: {total_centros}\n")
        f.write(f"En Seguimiento: {centros_en_seguimiento}\n")
        f.write(f"Cobertura: {(centros_en_seguimiento/total_centros*100):.1f}%\n\n")
        
        if not df_seguimiento.empty and 'Estado' in df_seguimiento.columns:
            f.write("Distribución por Estado:\n")
            for estado, count in estados.items():
                f.write(f"  {estado}: {count}\n")
    
    print(f"💾 Reporte guardado: {reporte_filename}")
    print("="*80)

if __name__ == "__main__":
    print()
    print("🔍 SISTEMA DE VERIFICACIÓN Y SINCRONIZACIÓN DE CENTROS")
    print("   Evita pérdida de información asegurando que todos los")
    print("   centros educativos estén en el sistema de seguimiento")
    print()
    
    try:
        verificar_sincronizacion()
        print()
        print("¿Deseas generar un reporte completo? (s/n): ", end="")
        if input().strip().lower() == 's':
            generar_reporte_completo()
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
    
    print()
    input("Presiona Enter para salir...")
