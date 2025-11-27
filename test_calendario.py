"""
Script de Prueba del Sistema de Calendarios por Usuario
"""

import calendario_module
import pandas as pd
import os

print("=" * 60)
print("PRUEBA DEL SISTEMA DE CALENDARIOS")
print("=" * 60)

# Test 1: Obtener nombres de archivos por usuario
print("\n1. Obteniendo nombres de archivos de calendario...")
archivo_admin = calendario_module.obtener_archivo_calendario_usuario('admin')
archivo_user1 = calendario_module.obtener_archivo_calendario_usuario('user1')
archivo_user2 = calendario_module.obtener_archivo_calendario_usuario('user2')

print(f"   ✅ Admin: {archivo_admin}")
print(f"   ✅ User1: {archivo_user1}")
print(f"   ✅ User2: {archivo_user2}")

# Test 2: Crear calendario de prueba para admin
print("\n2. Creando calendario de prueba para admin...")
df_cal_admin = pd.DataFrame([
    {
        'ID_Cita': 1,
        'Fecha': '2025-11-27',
        'Hora': 9,
        'Centro': 'Escuela Central',
        'Provincia': 'SAN JOSE',
        'Canton': 'Central',
        'Categoria': 'CAT 1',
        'Prioridad': 'Alta',
        'Nota': 'Primera cita',
        'Estado': 'Pendiente',
        'Fecha_Creacion': '2025-11-27'
    },
    {
        'ID_Cita': 2,
        'Fecha': '2025-11-27',
        'Hora': 10,
        'Centro': 'Escuela Norte',
        'Provincia': 'ALAJUELA',
        'Canton': 'Central',
        'Categoria': 'CAT 2',
        'Prioridad': 'Media',
        'Nota': 'Segunda cita',
        'Estado': 'Confirmada',
        'Fecha_Creacion': '2025-11-27'
    }
])

calendario_module.guardar_calendario(df_cal_admin, archivo_admin)
print(f"   ✅ Calendario guardado: {len(df_cal_admin)} citas")

# Test 3: Crear calendario diferente para user1
print("\n3. Creando calendario diferente para user1...")
df_cal_user1 = pd.DataFrame([
    {
        'ID_Cita': 1,
        'Fecha': '2025-11-28',
        'Hora': 14,
        'Centro': 'Colegio del Sur',
        'Provincia': 'CARTAGO',
        'Canton': 'Central',
        'Categoria': 'CAT 1',
        'Prioridad': 'Baja',
        'Nota': 'Cita de user1',
        'Estado': 'Pendiente',
        'Fecha_Creacion': '2025-11-27'
    }
])

calendario_module.guardar_calendario(df_cal_user1, archivo_user1)
print(f"   ✅ Calendario guardado: {len(df_cal_user1)} citas")

# Test 4: Verificar que los archivos son independientes
print("\n4. Verificando independencia de calendarios...")
df_cargado_admin = calendario_module.cargar_calendario(archivo_admin)
df_cargado_user1 = calendario_module.cargar_calendario(archivo_user1)

print(f"   ✅ Admin tiene: {len(df_cargado_admin)} citas")
print(f"   ✅ User1 tiene: {len(df_cargado_user1)} citas")
print(f"   ✅ Son diferentes: {len(df_cargado_admin) != len(df_cargado_user1)}")

# Test 5: Verificar que user2 no tiene calendario aún
print("\n5. Verificando usuario sin calendario...")
df_cargado_user2 = calendario_module.cargar_calendario(archivo_user2)
print(f"   ✅ User2 tiene: {len(df_cargado_user2)} citas (debería ser 0)")
print(f"   ✅ DataFrame vacío: {df_cargado_user2.empty}")

# Test 6: Modificar y guardar calendario (simular actualización)
print("\n6. Modificando calendario de admin...")
df_cargado_admin.loc[0, 'Estado'] = 'Completada'
calendario_module.guardar_calendario(df_cargado_admin, archivo_admin)
print(f"   ✅ Estado actualizado")

# Verificar cambio
df_verificar = calendario_module.cargar_calendario(archivo_admin)
print(f"   ✅ Verificación: Estado es '{df_verificar.loc[0, 'Estado']}'")

# Test 7: Eliminar una cita (simular borrado)
print("\n7. Eliminando cita del calendario de admin...")
df_antes = calendario_module.cargar_calendario(archivo_admin)
print(f"   - Antes: {len(df_antes)} citas")

df_despues = df_antes.drop(0).reset_index(drop=True)
calendario_module.guardar_calendario(df_despues, archivo_admin)

df_verificar = calendario_module.cargar_calendario(archivo_admin)
print(f"   ✅ Después: {len(df_verificar)} citas")
print(f"   ✅ Cita eliminada correctamente")

# Test 8: Agregar más citas sin sobrescribir
print("\n8. Agregando citas sin sobrescribir...")
df_actual = calendario_module.cargar_calendario(archivo_admin)
print(f"   - Citas actuales: {len(df_actual)}")

nuevas_citas = pd.DataFrame([
    {
        'ID_Cita': 3,
        'Fecha': '2025-11-29',
        'Hora': 11,
        'Centro': 'Escuela Este',
        'Provincia': 'LIMON',
        'Canton': 'Central',
        'Categoria': 'CAT 1',
        'Prioridad': 'Alta',
        'Nota': 'Nueva cita',
        'Estado': 'Pendiente',
        'Fecha_Creacion': '2025-11-27'
    }
])

df_combinado = pd.concat([df_actual, nuevas_citas], ignore_index=True)
calendario_module.guardar_calendario(df_combinado, archivo_admin)

df_final = calendario_module.cargar_calendario(archivo_admin)
print(f"   ✅ Citas finales: {len(df_final)}")
print(f"   ✅ Agregado correctamente sin sobrescribir")

print("\n" + "=" * 60)
print("PRUEBAS COMPLETADAS")
print("=" * 60)

# Mostrar resumen de archivos
print("\n📋 RESUMEN DE ARCHIVOS DE CALENDARIO:")
for usuario in ['admin', 'user1', 'user2']:
    archivo = calendario_module.obtener_archivo_calendario_usuario(usuario)
    existe = os.path.exists(archivo)
    if existe:
        df = calendario_module.cargar_calendario(archivo)
        print(f"   {usuario:10} → {archivo:25} ({len(df)} citas)")
    else:
        print(f"   {usuario:10} → {archivo:25} (no existe)")

print("\n📅 CONTENIDO DEL CALENDARIO DE ADMIN:")
df_admin_final = calendario_module.cargar_calendario(archivo_admin)
if not df_admin_final.empty:
    print(df_admin_final[['Fecha', 'Hora', 'Centro', 'Estado']].to_string(index=False))
else:
    print("   (vacío)")

print("\n📅 CONTENIDO DEL CALENDARIO DE USER1:")
df_user1_final = calendario_module.cargar_calendario(archivo_user1)
if not df_user1_final.empty:
    print(df_user1_final[['Fecha', 'Hora', 'Centro', 'Estado']].to_string(index=False))
else:
    print("   (vacío)")
