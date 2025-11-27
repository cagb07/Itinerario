# 🔄 Guía de Migración de Datos Existentes

## 📋 Información General

Si ya tenías una versión anterior del sistema funcionando con datos, esta guía te ayudará a migrar sin perder información.

---

## ⚠️ Antes de Empezar

### Hacer Backup Completo

```bash
# Crear carpeta de backup con fecha
mkdir backup_$(date +%Y%m%d)

# Copiar todos los archivos importantes
cp calendario.csv backup_$(date +%Y%m%d)/
cp seguimiento_informes.csv backup_$(date +%Y%m%d)/
cp LISTADO-CON-FASES.csv backup_$(date +%Y%m%d)/
```

---

## 🔄 Migración del Calendario

### Escenario 1: Un Solo Usuario

Si solo tú usas el sistema:

1. **Identificar tu usuario**
   - Por defecto será: `admin`

2. **Renombrar el archivo de calendario antiguo**
   ```bash
   # Si tu usuario es 'admin'
   mv calendario.csv calendario_admin.csv
   ```

3. **Iniciar sesión**
   - Usuario: `admin`
   - Contraseña: `admin123`

4. **Verificar**
   - Ir a "Calendario"
   - Deberías ver todas tus citas antiguas

### Escenario 2: Múltiples Usuarios

Si varias personas usaban el sistema:

1. **Decidir cómo distribuir las citas**

   **Opción A: Todas las citas a un usuario principal**
   ```bash
   mv calendario.csv calendario_admin.csv
   ```

   **Opción B: Dividir por responsable**
   - Editar manualmente el archivo
   - Crear múltiples archivos `calendario_usuario.csv`

2. **Crear usuarios en el sistema**
   - Login como `admin`
   - Ir a "👥 Gestión de Usuarios"
   - Crear un usuario por cada persona

3. **Distribuir calendarios**
   ```bash
   # Ejemplo: Crear calendarios específicos
   cp calendario.csv calendario_jperez.csv
   cp calendario.csv calendario_mgarcia.csv
   
   # Luego editar cada archivo para dejar solo las citas relevantes
   ```

---

## 📊 Migración del Kanban

El Kanban NO necesita migración porque es compartido entre todos los usuarios.

El archivo `seguimiento_informes.csv` se mantiene igual.

---

## 📁 Migración de Base de Centros

La base de centros educativos tampoco necesita migración.

El archivo `LISTADO-CON-FASES.csv` se mantiene igual.

---

## 👥 Creación de Usuarios Iniciales

### Paso 1: Primer Login

```
Usuario: admin
Contraseña: admin123
```

### Paso 2: Cambiar Contraseña del Admin

1. Ir a "👥 Gestión de Usuarios" → "🔧 Gestionar"
2. Seleccionar `admin`
3. Expandir "🔑 Cambiar Contraseña"
4. Ingresar nueva contraseña segura
5. Guardar

### Paso 3: Crear Usuarios del Equipo

Para cada miembro del equipo:

1. Ir a "👥 Gestión de Usuarios" → "➕ Crear Usuario"
2. Completar:
   - **Usuario:** (ej: `jperez`)
   - **Nombre Completo:** (ej: `Juan Pérez`)
   - **Contraseña:** (ej: `temporal123`)
   - **Rol:** `usuario` (o `admin` si necesita permisos)
3. Crear usuario

### Paso 4: Notificar a los Usuarios

Enviar a cada usuario:
```
Hola [Nombre],

Ya puedes acceder al nuevo sistema de Control de Informes:

URL: http://tu-servidor:8501
Usuario: [usuario]
Contraseña temporal: [contraseña]

Por favor cambia tu contraseña al iniciar sesión por primera vez.

Ahora cada usuario tiene su propio calendario independiente.
```

---

## 🔍 Verificación Post-Migración

### Checklist de Verificación

- [ ] Archivo `usuarios.csv` creado
- [ ] Usuario `admin` existe y funciona
- [ ] Todos los usuarios del equipo creados
- [ ] Calendario antiguo respaldado
- [ ] Calendarios por usuario creados
- [ ] Cada usuario puede ver sus citas
- [ ] Kanban funciona correctamente
- [ ] Base de centros intacta
- [ ] No hay duplicados en calendarios

### Probar Funcionalidades

1. **Login/Logout**
   - Cada usuario puede entrar
   - Cerrar sesión funciona

2. **Calendarios Independientes**
   - Usuario A ve solo sus citas
   - Usuario B ve solo sus citas
   - No hay cruces de información

3. **Kanban Compartido**
   - Todos ven los mismos informes
   - Pueden actualizar estados

4. **Creación de Citas**
   - Crear citas nuevas funciona
   - Modificar citas funciona
   - Eliminar citas funciona (sin borrar otras)

---

## 🛠️ Solución de Problemas Comunes

### No veo mis citas antiguas

**Causa:** El archivo de calendario no tiene el nombre correcto.

**Solución:**
```bash
# Verificar qué archivos existen
ls calendario*.csv

# Renombrar al formato correcto
mv calendario.csv calendario_tuusuario.csv
```

### Veo citas de otras personas

**Causa:** Todos están usando el mismo archivo de calendario.

**Solución:**
1. Hacer backup del calendario actual
2. Dividir el archivo manualmente
3. Crear archivos separados para cada usuario

### No puedo crear usuarios

**Causa:** No tienes rol de admin.

**Solución:**
1. Cerrar sesión
2. Iniciar como `admin`
3. Crear los usuarios necesarios

### Error al guardar calendario

**Causa:** Permisos de archivo.

**Solución:**
```bash
# Dar permisos de escritura
chmod 666 calendario_*.csv
```

---

## 📦 Script de Migración Automatizada

Para facilitar la migración, aquí hay un script:

```bash
#!/bin/bash
# migrate.sh - Script de migración automática

echo "🔄 Iniciando migración..."

# 1. Crear backup
BACKUP_DIR="backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p $BACKUP_DIR
echo "📦 Creando backup en $BACKUP_DIR"

cp calendario.csv $BACKUP_DIR/ 2>/dev/null || echo "⚠️  calendario.csv no encontrado"
cp seguimiento_informes.csv $BACKUP_DIR/ 2>/dev/null
cp LISTADO-CON-FASES.csv $BACKUP_DIR/ 2>/dev/null

# 2. Renombrar calendario para admin
if [ -f calendario.csv ]; then
    echo "📅 Migrando calendario.csv → calendario_admin.csv"
    mv calendario.csv calendario_admin.csv
fi

# 3. Verificar archivos
echo ""
echo "✅ Migración completada"
echo ""
echo "📋 Archivos actuales:"
ls -lh calendario*.csv 2>/dev/null || echo "Sin calendarios"
ls -lh usuarios.csv 2>/dev/null || echo "Sin usuarios (se creará al iniciar)"

echo ""
echo "🚀 Siguiente paso:"
echo "   1. Ejecutar: streamlit run app.py"
echo "   2. Login con admin/admin123"
echo "   3. Cambiar contraseña del admin"
echo "   4. Crear usuarios del equipo"
```

**Usar el script:**
```bash
chmod +x migrate.sh
./migrate.sh
```

---

## 📊 Esquema de Datos Después de la Migración

### Antes (Sistema Antiguo)
```
calendario.csv                 ← Compartido por todos
seguimiento_informes.csv       ← Compartido
LISTADO-CON-FASES.csv         ← Compartido
```

### Después (Sistema Nuevo)
```
usuarios.csv                   ← NUEVO: Base de usuarios
calendario_admin.csv           ← NUEVO: Calendario de admin
calendario_jperez.csv          ← NUEVO: Calendario de jperez
calendario_mgarcia.csv         ← NUEVO: Calendario de mgarcia
seguimiento_informes.csv       ← Compartido (sin cambios)
LISTADO-CON-FASES.csv         ← Compartido (sin cambios)
```

---

## 🎯 Resumen de Pasos

1. ✅ **Hacer backup completo**
2. ✅ **Renombrar calendario.csv → calendario_admin.csv**
3. ✅ **Iniciar aplicación**
4. ✅ **Login como admin**
5. ✅ **Cambiar contraseña del admin**
6. ✅ **Crear usuarios del equipo**
7. ✅ **Distribuir calendarios (si aplica)**
8. ✅ **Verificar funcionamiento**
9. ✅ **Notificar a usuarios**

---

## 📞 Soporte

Si encuentras problemas durante la migración:

1. **Revisar logs de error** en la terminal donde corre Streamlit
2. **Verificar permisos** de archivos
3. **Confirmar backup** antes de cualquier cambio
4. **Consultar** `SISTEMA_AUTENTICACION.md` para detalles técnicos
5. **Revisar** `GUIA_USO.md` para uso del sistema

---

**¡Buena suerte con la migración!** 🚀

Si todo sale bien, tendrás un sistema mucho más robusto con:
- ✅ Autenticación segura
- ✅ Calendarios independientes
- ✅ Sin pérdida de datos
- ✅ Sin bugs de borrado
