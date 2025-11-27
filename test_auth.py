"""
Script de Prueba del Sistema de Autenticación
"""

import auth_module
import os

print("=" * 60)
print("PRUEBA DEL SISTEMA DE AUTENTICACIÓN")
print("=" * 60)

# Test 1: Cargar usuarios (debería crear el archivo si no existe)
print("\n1. Cargando usuarios...")
df_usuarios = auth_module.cargar_usuarios()
print(f"   ✅ Usuarios cargados: {len(df_usuarios)}")
print(f"   ✅ Archivo existe: {os.path.exists('usuarios.csv')}")

# Test 2: Validar credenciales del admin
print("\n2. Validando credenciales del admin...")
valido, datos = auth_module.validar_credenciales('admin', 'admin123')
if valido:
    print(f"   ✅ Login exitoso")
    print(f"   - Usuario: {datos['usuario']}")
    print(f"   - Nombre: {datos['nombre_completo']}")
    print(f"   - Rol: {datos['rol']}")
else:
    print("   ❌ Login fallido")

# Test 3: Crear un usuario de prueba
print("\n3. Creando usuario de prueba...")
exito, mensaje = auth_module.crear_usuario(
    usuario='test_user',
    password='test123',
    nombre_completo='Usuario de Prueba',
    rol='usuario'
)
print(f"   {'✅' if exito else '❌'} {mensaje}")

# Test 4: Verificar que no se puede crear usuario duplicado
print("\n4. Intentando crear usuario duplicado...")
exito, mensaje = auth_module.crear_usuario(
    usuario='test_user',
    password='otra_pass',
    nombre_completo='Otro Usuario',
    rol='usuario'
)
print(f"   {'✅' if not exito else '❌'} {mensaje}")

# Test 5: Validar credenciales del nuevo usuario
print("\n5. Validando credenciales del nuevo usuario...")
valido, datos = auth_module.validar_credenciales('test_user', 'test123')
if valido:
    print(f"   ✅ Login exitoso")
    print(f"   - Usuario: {datos['usuario']}")
    print(f"   - Nombre: {datos['nombre_completo']}")
else:
    print("   ❌ Login fallido")

# Test 6: Desactivar usuario
print("\n6. Desactivando usuario de prueba...")
exito, mensaje = auth_module.desactivar_usuario('test_user')
print(f"   {'✅' if exito else '❌'} {mensaje}")

# Test 7: Intentar login con usuario desactivado
print("\n7. Intentando login con usuario desactivado...")
valido, datos = auth_module.validar_credenciales('test_user', 'test123')
print(f"   {'✅' if not valido else '❌'} Usuario desactivado no puede hacer login")

# Test 8: Activar usuario de nuevo
print("\n8. Reactivando usuario...")
exito, mensaje = auth_module.activar_usuario('test_user')
print(f"   {'✅' if exito else '❌'} {mensaje}")

# Test 9: Cambiar contraseña
print("\n9. Cambiando contraseña del usuario de prueba...")
exito, mensaje = auth_module.cambiar_password('test_user', 'test123', 'nueva_pass456')
print(f"   {'✅' if exito else '❌'} {mensaje}")

# Test 10: Validar con nueva contraseña
print("\n10. Validando con nueva contraseña...")
valido, datos = auth_module.validar_credenciales('test_user', 'nueva_pass456')
print(f"   {'✅' if valido else '❌'} Login con nueva contraseña")

print("\n" + "=" * 60)
print("PRUEBAS COMPLETADAS")
print("=" * 60)

# Mostrar resumen de usuarios
print("\n📋 RESUMEN DE USUARIOS:")
df_usuarios = auth_module.cargar_usuarios()
print(df_usuarios[['usuario', 'nombre_completo', 'rol', 'activo']].to_string(index=False))
