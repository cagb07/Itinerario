# 🚀 Guía Rápida de Uso - Sistema de Control de Informes

## 📝 Inicio Rápido

### 1️⃣ Iniciar la Aplicación
```bash
streamlit run app.py
```

### 2️⃣ Primer Login
**Credenciales por defecto:**
- **Usuario:** `admin`
- **Contraseña:** `admin123`

⚠️ **Importante:** Cambia la contraseña del admin después del primer inicio.

---

## 👥 Gestión de Usuarios

### Crear un Nuevo Usuario (Solo Admin)

1. **Navegar al menú** → `👥 Gestión de Usuarios`
2. **Ir a la pestaña** → `➕ Crear Usuario`
3. **Completar el formulario:**
   - Usuario (único, ej: `jperez`)
   - Nombre Completo (ej: `Juan Pérez`)
   - Contraseña (mínimo 6 caracteres)
   - Rol: `usuario` o `admin`
4. **Hacer clic** en `➕ Crear Usuario`

### Cambiar Contraseña de un Usuario

1. **Ir a** → `👥 Gestión de Usuarios` → `🔧 Gestionar`
2. **Seleccionar usuario** del dropdown
3. **Expandir** "🔑 Cambiar Contraseña"
4. **Ingresar nueva contraseña** (dos veces)
5. **Hacer clic** en `💾 Actualizar Contraseña`

### Desactivar/Activar Usuario

1. **Ir a** → `👥 Gestión de Usuarios` → `🔧 Gestionar`
2. **Seleccionar usuario**
3. **Hacer clic** en:
   - `🚫 Desactivar usuario` (si está activo)
   - `✅ Activar usuario` (si está inactivo)

---

## 📅 Usar el Calendario

### Ver Agenda

1. **Navegar a** → `Calendario`
2. **Seleccionar vista:**
   - `📅 Diaria` - Ver citas de un día específico
   - `📆 Semanal` - Ver toda la semana
3. **Cada usuario ve solo su propio calendario**

### Agendar una Cita

1. **Ir a** → `Calendario` → `➕ Agendar Cita`
2. **Completar formulario:**
   - Fecha de la cita
   - Hora (8:00 - 16:00, excepto 12:00-13:00)
   - Seleccionar centro educativo
   - Prioridad (Alta, Media, Baja)
   - Nota opcional
3. **Hacer clic** en `📅 Crear Cita`

### Gestionar Citas Existentes

1. **Ir a** → `Calendario` → `⚙️ Gestionar Citas`
2. **Expandir la cita** que deseas modificar
3. **Opciones disponibles:**
   - Cambiar estado (Pendiente, Confirmada, Completada, Cancelada)
   - Eliminar cita

### Generador Automático de Citas

1. **Ir a** → `Calendario` → `🤖 Generador Automático`
2. **Configurar parámetros:**
   - Fecha de inicio
   - Días a planificar
   - Máximo de citas por día
   - Categorías de centros
3. **Hacer clic** en `🚀 Generar`
4. El sistema creará citas automáticamente:
   - Solo en días laborables (lunes a viernes)
   - Sin sobrecargar días
   - Excluyendo centros ya agendados

---

## 📊 Dashboard y Kanban

### Ver Estadísticas Globales

1. **Navegar a** → `Dashboard de Control`
2. **Métricas disponibles:**
   - Total de centros en base de datos
   - Centros con informes completados
   - Centros pendientes
   - Porcentaje de cobertura

### Gestionar Flujo de Trabajo (Kanban)

1. **Ir a** → `Kanban de Informes`
2. **Estados disponibles:**
   - ⚪ Pendiente
   - 🟡 Pausado
   - 🔵 En Proceso
   - 🟢 Terminado
3. **Arrastrar tarjetas** entre columnas para cambiar estado
4. **Agregar notas/observaciones** a cada informe

### Iniciar Nuevo Informe

1. **En Kanban** → Expandir `➕ Iniciar Nuevo Informe`
2. **Buscar centro educativo** (filtro por nombre)
3. **Completar información:**
   - Fecha de inicio
   - Responsable
   - Prioridad
   - Observaciones
4. **Hacer clic** en `➕ Agregar al Kanban`

---

## 🗄️ Base de Datos

### Ver Centros Educativos

1. **Navegar a** → `Base de Datos` → `📋 Centros Educativos`
2. **Funciones disponibles:**
   - Ver listado completo
   - Filtrar por provincia
   - Buscar por nombre
   - Ver estadísticas por categoría

### Agregar Nuevos Centros

**Método Manual:**
1. **Ir a** → `Base de Datos` → `➕ Agregar Centros`
2. **Seleccionar** → `📝 Manual (Individual)`
3. **Completar formulario** y hacer clic en `➕ Agregar Centro`

**Método por Importación:**
1. **Ir a** → `Base de Datos` → `➕ Agregar Centros`
2. **Seleccionar** → `📁 Importar CSV`
3. **Subir archivo CSV** con la estructura correcta
4. **Elegir modo:**
   - `➕ Agregar a existentes` - No borra datos actuales
   - `🔄 Reemplazar todos` - Limpia y carga nuevos
5. **Hacer clic** en `📥 Importar Centros`

---

## 🔒 Seguridad y Privacidad

### ✅ Características de Seguridad

- ✔️ Contraseñas encriptadas (SHA-256)
- ✔️ Sesiones seguras
- ✔️ Calendarios privados por usuario
- ✔️ Control de acceso basado en roles

### 🚪 Cerrar Sesión

**Siempre cierra sesión al terminar:**
1. En el **sidebar** (barra lateral izquierda)
2. **Hacer clic** en `🚪 Cerrar Sesión`

---

## 💡 Consejos y Mejores Prácticas

### Para Usuarios Normales

✅ **Revisa tu calendario diariamente** para confirmar citas  
✅ **Actualiza el estado de las citas** después de cada visita  
✅ **Usa el generador automático** para planificar semanas completas  
✅ **Agrega notas** en las citas para recordar detalles importantes  

### Para Administradores

✅ **Crea usuarios con contraseñas seguras** (combinar letras y números)  
✅ **Revisa el dashboard regularmente** para monitorear progreso  
✅ **Haz backup semanal** de los archivos CSV  
✅ **Desactiva usuarios** que ya no necesiten acceso (no los elimines)  
✅ **Mantén actualizada la base de centros educativos**  

### Backup Recomendado

Archivos importantes a respaldar:
- `usuarios.csv` - Base de datos de usuarios
- `calendario_*.csv` - Todos los calendarios
- `seguimiento_informes.csv` - Estado de informes (Kanban)
- `LISTADO-CON-FASES.csv` - Base de datos de centros

---

## ❓ Preguntas Frecuentes

### ¿Puedo ver el calendario de otro usuario?
**No.** Cada usuario solo ve su propio calendario para mantener privacidad.

### ¿Qué pasa si olvido mi contraseña?
**Contacta a un administrador** para que resetee tu contraseña.

### ¿Puedo agendar dos citas a la misma hora?
**No.** El sistema previene conflictos de horario automáticamente.

### ¿Los datos del Kanban son compartidos?
**Sí.** El Kanban es compartido entre todos los usuarios para coordinar el trabajo.

### ¿Puedo exportar mi calendario?
**Actualmente no hay función de exportación**, pero puedes acceder directamente al archivo `calendario_tuusuario.csv` para crear tus propios reportes.

### ¿Se pueden recuperar citas eliminadas?
**No.** La eliminación es permanente. Confirma siempre antes de eliminar.

---

## 🆘 Soporte y Ayuda

Si encuentras problemas:

1. **Verifica que estás usando las credenciales correctas**
2. **Cierra y vuelve a iniciar sesión**
3. **Revisa el archivo** `SISTEMA_AUTENTICACION.md` para información técnica detallada
4. **Contacta al administrador del sistema** si el problema persiste

---

## 📌 Atajos de Teclado Útiles

- `Ctrl + R` - Recargar la página (útil si algo no responde)
- `F11` - Pantalla completa
- `Ctrl + -` / `Ctrl + +` - Zoom out/in

---

**Última actualización:** 27 de Noviembre, 2025  
**Versión del sistema:** 2.0 con autenticación integrada
