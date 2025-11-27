# 🔐 Sistema de Autenticación y Calendarios por Usuario

## Resumen de Cambios

Se ha implementado un **sistema completo de autenticación de usuarios** y se ha corregido el problema de **borrado de agendas**. Ahora cada usuario tiene su propio calendario independiente.

---

## ✅ Problemas Resueltos

### 1. **Bug de Borrado de Agendas** 
**Problema identificado:** En `calendario_module.py`, las líneas 372, 379, 469-471 estaban sobrescribiendo el archivo completo del calendario en lugar de actualizarlo correctamente.

**Solución implementada:**
- Se creó la función `guardar_calendario(df_calendario, archivo_calendario)` que reemplaza correctamente el archivo
- Se modificó el proceso de eliminación para resetear correctamente el índice con `.reset_index(drop=True)`
- Se corrigió la generación automática para usar `pd.concat()` en lugar de modo append de CSV que duplicaba registros

### 2. **Calendarios Compartidos**
**Problema:** Todos los usuarios compartían el mismo archivo `calendario.csv`, causando confusión y pérdida de datos.

**Solución implementada:**
- Cada usuario ahora tiene su propio archivo: `calendario_usuario.csv` 
- La función `obtener_archivo_calendario_usuario(usuario)` genera el nombre del archivo específico
- Los calendarios son completamente independientes entre usuarios

---

## 🆕 Funcionalidades Nuevas

### Sistema de Autenticación

#### **Características:**
- ✅ Login con usuario y contraseña
- ✅ Contraseñas hasheadas con SHA-256 (seguras)
- ✅ Sesión persistente durante toda la navegación
- ✅ Roles de usuario: `admin` y `usuario`
- ✅ Usuario por defecto: `admin` / `admin123`

#### **Gestión de Usuarios (Solo Admin):**
- ➕ Crear nuevos usuarios
- 👁️ Ver lista completa de usuarios
- 🚫 Activar/Desactivar usuarios
- 🔑 Cambiar contraseñas
- 📊 Estadísticas de usuarios activos/inactivos

---

## 📁 Archivos Modificados

### 1. **auth_module.py** (NUEVO)
Módulo completo de autenticación que incluye:
- `cargar_usuarios()` - Carga la base de datos de usuarios
- `validar_credenciales()` - Valida login
- `crear_usuario()` - Crea nuevos usuarios
- `cambiar_password()` - Actualiza contraseñas
- `render_login()` - Interfaz de login
- `render_gestion_usuarios()` - Panel de administración

### 2. **calendario_module.py** (MODIFICADO)
Cambios realizados:
- ✅ Función `obtener_archivo_calendario_usuario(usuario)` - Genera nombre de archivo por usuario
- ✅ Función `guardar_calendario(df, archivo)` - Guarda correctamente el calendario completo
- ✅ Parámetro `usuario` en `render_calendario()` - Muestra el usuario en el título
- ✅ Corrección del bug de eliminación de citas
- ✅ Corrección de generación automática sin sobrescribir

### 3. **app.py** (MODIFICADO)
Integraciones realizadas:
- ✅ Import de `auth_module` y `calendario_module`
- ✅ Inicialización de sesión con `auth_module.inicializar_sesion()`
- ✅ Verificación de autenticación antes de mostrar la app
- ✅ Obtención del archivo de calendario específico del usuario
- ✅ Información del usuario en el sidebar
- ✅ Botón de cerrar sesión
- ✅ Menú "Gestión de Usuarios" para administradores

### 4. **usuarios.csv** (NUEVO - Auto-generado)
Base de datos de usuarios con estructura:
```csv
usuario,password_hash,nombre_completo,rol,activo,fecha_creacion
admin,<hash>,Administrador,admin,True,2025-11-27 ...
```

### 5. **calendario_usuario.csv** (NUEVO - Por usuario)
Cada usuario tiene su propio archivo de calendario, por ejemplo:
- `calendario_admin.csv`
- `calendario_jperez.csv`
- `calendario_mgarcia.csv`

---

## 🚀 Cómo Usar el Sistema

### Primer Inicio
1. Ejecutar la aplicación: `streamlit run app.py`
2. Ingresar con las credenciales por defecto:
   - **Usuario:** `admin`
   - **Contraseña:** `admin123`
3. Cambiar la contraseña del admin (recomendado)

### Crear Usuarios
1. Iniciar sesión como `admin`
2. Ir a "👥 Gestión de Usuarios" en el menú
3. En la pestaña "➕ Crear Usuario":
   - Ingresar nombre de usuario (único)
   - Ingresar nombre completo
   - Crear contraseña (mínimo 6 caracteres)
   - Seleccionar rol (`usuario` o `admin`)
4. Hacer clic en "➕ Crear Usuario"

### Trabajar con el Calendario
1. Cada usuario ve solo su propio calendario
2. Las citas creadas son privadas para cada usuario
3. Los administradores NO ven los calendarios de otros usuarios (privacidad)

### Gestionar Usuarios Existentes
1. Ir a "👥 Gestión de Usuarios" → pestaña "🔧 Gestionar"
2. Seleccionar el usuario a gestionar
3. Opciones disponibles:
   - Activar/Desactivar usuario
   - Cambiar contraseña (sin necesidad de saber la actual)

---

## 🔒 Seguridad

### Contraseñas
- ✅ Las contraseñas se hashean con SHA-256
- ✅ NUNCA se almacenan en texto plano
- ✅ No es posible recuperar la contraseña original
- ⚠️ Los administradores pueden resetear contraseñas de otros usuarios

### Sesiones
- ✅ La sesión se mantiene durante toda la navegación
- ✅ Cerrar sesión limpia todos los datos de `session_state`
- ✅ No hay acceso sin autenticación

### Privacidad de Datos
- ✅ Cada usuario solo ve su calendario
- ✅ Los archivos están separados físicamente
- ✅ No hay acceso cruzado entre usuarios

---

## 📊 Estructura de Datos

### Session State
```python
st.session_state.autenticado      # bool: True si el usuario está logueado
st.session_state.usuario           # str: Nombre de usuario actual
st.session_state.datos_usuario     # dict: Información completa del usuario
```

### Datos de Usuario
```python
{
    'usuario': 'jperez',
    'nombre_completo': 'Juan Pérez',
    'rol': 'usuario',
    'activo': True,
    'fecha_creacion': '2025-11-27 10:30:00'
}
```

---

## 🔄 Flujo de la Aplicación

```
1. Usuario accede a la app
   ↓
2. Se inicializa session_state
   ↓
3. ¿Está autenticado?
   NO → Mostrar pantalla de login → Validar credenciales
   ↓
4. SÍ → Obtener archivo de calendario del usuario
   ↓
5. Mostrar interfaz principal con:
   - Información del usuario en sidebar
   - Menú según permisos (admin ve más opciones)
   - Calendario específico del usuario
   ↓
6. Usuario trabaja con sus datos
   ↓
7. Cerrar sesión → Limpiar session_state → Volver a login
```

---

## ⚠️ Consideraciones Importantes

### Backup
- Hacer backup regular de `usuarios.csv`
- Hacer backup de todos los archivos `calendario_*.csv`

### Eliminación de Usuarios
- Actualmente se desactivan, NO se eliminan
- Para eliminar físicamente, editar manualmente `usuarios.csv` (no recomendado)
- Los calendarios de usuarios desactivados NO se eliminan automáticamente

### Migración de Datos Antiguos
Si ya tenías un `calendario.csv` con datos:
1. Hacer backup del archivo
2. Renombrarlo según el usuario: `calendario_admin.csv`
3. O importar manualmente las citas al calendario del usuario correspondiente

---

## 🛠️ Troubleshooting

### "No se encuentra usuarios.csv"
**Solución:** El archivo se crea automáticamente en el primer inicio. Si falta, se genera con el usuario `admin` por defecto.

### "Olvide mi contraseña de admin"
**Solución:** 
1. Cerrar la app
2. Eliminar `usuarios.csv`
3. Reiniciar la app (se creará de nuevo con `admin/admin123`)

### "No veo mis citas antiguas"
**Solución:** Verificar que el archivo `calendario_tuusuario.csv` exista. Si tenías un `calendario.csv` antiguo, renómbralo según tu usuario.

### "Error al guardar calendario"
**Solución:** Verificar permisos de escritura en el directorio de la aplicación.

---

## 📝 Tareas Futuras (Opcionales)

- [ ] Agregar recuperación de contraseña por email
- [ ] Implementar logs de auditoría de acciones
- [ ] Agregar opción de exportar/importar calendarios
- [ ] Permitir que admins vean calendarios de otros usuarios (con permiso)
- [ ] Agregar foto de perfil para usuarios
- [ ] Implementar permisos más granulares

---

## 👨‍💻 Créditos

Sistema desarrollado para resolver:
1. Bug de borrado de agendas en operaciones de actualización/eliminación
2. Necesidad de calendarios independientes por usuario
3. Sistema de autenticación y gestión de usuarios

**Fecha de implementación:** 27 de Noviembre, 2025
