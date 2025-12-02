# 🔧 Solución: Pérdida de Datos al Suspender la Aplicación

## ❌ Problema Identificado

**Síntoma:** Al poner la computadora en suspensión o al dejar la aplicación inactiva, se pierden todos los datos recopilados de los informes del Kanban.

### **Causa Raíz:**

1. **Guardado Simple**: La función `guardar_seguimiento()` original era muy básica y no verificaba que los datos se guardaran correctamente
2. **Sin Verificación**: No había confirmación de que el archivo CSV se escribió correctamente
3. **Sin Backup**: No se creaban copias de seguridad antes de sobrescribir
4. **Sin Manejo de Errores**: Cualquier error durante el guardado pasaba desapercibido
5. **Falta de Columnas**: La columna 'Observaciones' podía no existir, causando errores

---

## ✅ Solución Implementada

### **1. Función de Guardado Robusta**

Se mejoró `guardar_seguimiento()` con:

```python
✅ Verificación de columnas requeridas
✅ Backup automático antes de guardar
✅ Encoding UTF-8 explícito
✅ Verificación post-guardado
✅ Restauración automática si falla
✅ Manejo completo de errores
✅ Mensajes claros al usuario
```

### **2. Sistema de Verificación de Integridad**

Al iniciar la app:

```python
✅ Verifica que todas las columnas existen
✅ Agrega columnas faltantes automáticamente
✅ Guarda inmediatamente si detecta problemas
✅ Muestra tiempo desde última verificación
```

### **3. Indicador de Estado**

En el sidebar:
```
✅ Datos verificados hace 5s
```

---

## 🛡️ Protecciones Implementadas

### **Backup Automático**

Cada vez que guardas datos:
1. Se crea `seguimiento_informes.csv.backup`
2. Se guarda el archivo nuevo
3. Se verifica que se guardó correctamente
4. Si todo está bien, se elimina el backup
5. Si algo falla, se restaura el backup

### **Verificación Post-Guardado**

```python
1. Guardar archivo
2. Leer archivo guardado
3. Comparar número de registros
4. Si coincide → ✅ Éxito
5. Si no coincide → ❌ Restaurar backup
```

### **Manejo de Errores**

```python
try:
    guardar_datos()
    verificar_guardado()
except Error:
    restaurar_backup()
    notificar_usuario()
```

---

## 📊 Flujo de Guardado Mejorado

### **Antes (Vulnerable):**
```
Usuario hace cambio
    ↓
df.to_csv()
    ↓
¿Se guardó? 🤷 (No se verifica)
    ↓
Posible pérdida de datos ❌
```

### **Ahora (Robusto):**
```
Usuario hace cambio
    ↓
Crear backup del archivo actual
    ↓
Verificar columnas requeridas
    ↓
Guardar con encoding UTF-8
    ↓
Leer archivo guardado
    ↓
¿Coincide con datos originales?
    ├─ Sí → Eliminar backup ✅
    └─ No → Restaurar backup ⚠️
```

---

## 🔍 Verificaciones Automáticas

### **Al Iniciar la App:**

1. **Carga de Datos**
   ```python
   df_seguimiento = cargar_seguimiento()
   ```

2. **Verificación de Integridad**
   ```python
   - ¿Existen todas las columnas?
   - ¿Hay IDs duplicados?
   - ¿El formato es correcto?
   ```

3. **Corrección Automática**
   ```python
   - Agregar columnas faltantes
   - Corregir IDs duplicados
   - Guardar cambios inmediatamente
   ```

4. **Confirmación Visual**
   ```
   ✅ Datos verificados hace 0s
   ```

---

## 💾 Archivos de Respaldo

### **Ubicación:**
```
Itinerario/
├── seguimiento_informes.csv          # Archivo principal
├── seguimiento_informes.csv.backup   # Backup temporal
└── backups/                           # Backups manuales
    ├── backup_20251202_102500/
    │   └── seguimiento_informes.csv
    └── ...
```

### **Tipos de Backup:**

1. **Backup Temporal** (`.backup`)
   - Se crea antes de cada guardado
   - Se elimina si el guardado es exitoso
   - Se usa para restaurar si falla

2. **Backup Manual** (`backups/`)
   - Ejecuta `backup.bat`
   - Crea carpeta con timestamp
   - Mantiene últimos 10 backups

---

## 🚨 Qué Hacer Si Pierdes Datos

### **Opción 1: Restaurar Backup Temporal**

Si acabas de perder datos:

```bash
1. Ve a la carpeta del proyecto
2. Busca: seguimiento_informes.csv.backup
3. Renombra a: seguimiento_informes.csv
4. Reinicia la app
```

### **Opción 2: Restaurar Backup Manual**

Si hiciste backup antes:

```bash
1. Ve a: backups/
2. Busca la carpeta más reciente
3. Copia: seguimiento_informes.csv
4. Pega en la carpeta principal
5. Reinicia la app
```

### **Opción 3: Recuperar de Versiones Anteriores (Windows)**

```bash
1. Click derecho en seguimiento_informes.csv
2. Propiedades → Versiones anteriores
3. Selecciona una versión
4. Restaurar
```

---

## 📝 Mejores Prácticas

### **Para Prevenir Pérdida de Datos:**

1. **Backup Regular**
   ```bash
   # Ejecuta esto semanalmente
   backup.bat
   ```

2. **Verificar Guardado**
   ```
   Después de cambios importantes:
   1. Mira el sidebar
   2. Debe decir: ✅ Datos verificados hace Xs
   3. Si no aparece, reporta el problema
   ```

3. **No Cerrar Bruscamente**
   ```
   ❌ No: Cerrar ventana directamente
   ❌ No: Apagar PC sin cerrar app
   ✅ Sí: Ctrl+C en terminal
   ✅ Sí: Usar DETENER.bat
   ```

4. **Monitorear Errores**
   ```
   Si ves mensajes como:
   ❌ Error al guardar seguimiento
   ⚠️ Se restauró el backup anterior
   
   → Reporta inmediatamente
   ```

---

## 🔧 Configuración Adicional

### **Habilitar Auto-Guardado Frecuente**

Edita `app.py`, busca la sección de Kanban y agrega después de cada cambio:

```python
# Después de cualquier modificación a df_seguimiento
guardar_seguimiento(df_seguimiento)
st.session_state.ultima_verificacion = datetime.datetime.now()
```

### **Aumentar Frecuencia de Backups**

Programa `backup.bat` para ejecutarse automáticamente:

```
1. Abre "Programador de tareas"
2. Crear tarea básica
3. Trigger: Diario a las 6 PM
4. Acción: Ejecutar backup.bat
```

---

## 📊 Monitoreo de Salud

### **Indicadores en Sidebar:**

```
✅ Datos verificados hace 5s    → Todo bien
⚠️ Última verificación: 5m      → Revisar
❌ Error en verificación         → Problema crítico
```

### **Archivos a Monitorear:**

```bash
# Debe existir y tener contenido
seguimiento_informes.csv

# Debe tener registros
wc -l seguimiento_informes.csv
# Debe ser > 1 (header + datos)

# Verificar última modificación
ls -l seguimiento_informes.csv
```

---

## 🆘 Solución de Problemas

### **Problema: "Error al guardar seguimiento"**

**Causas posibles:**
- Archivo bloqueado por otro programa
- Permisos insuficientes
- Disco lleno
- Ruta incorrecta

**Solución:**
```bash
1. Cierra Excel u otros programas que puedan tener el archivo abierto
2. Verifica permisos de la carpeta
3. Verifica espacio en disco
4. Reinicia la app
```

### **Problema: "El archivo guardado no coincide"**

**Causa:** Corrupción durante escritura

**Solución:**
```bash
1. La app restaurará el backup automáticamente
2. Intenta el cambio nuevamente
3. Si persiste, ejecuta backup.bat
4. Reporta el problema
```

### **Problema: Datos desaparecen al reabrir**

**Causa:** Archivo no se está guardando

**Solución:**
```bash
1. Verifica que seguimiento_informes.csv existe
2. Abre el archivo y verifica contenido
3. Si está vacío, restaura backup
4. Verifica permisos de escritura
```

---

## ✅ Checklist de Verificación

Después de cada sesión de trabajo:

- [ ] Sidebar muestra "✅ Datos verificados"
- [ ] Archivo `seguimiento_informes.csv` existe
- [ ] Archivo tiene más de 1 línea (header + datos)
- [ ] Última modificación es reciente
- [ ] No hay mensajes de error en la app
- [ ] Backup manual creado (si hiciste cambios importantes)

---

## 📈 Mejoras Futuras Sugeridas

1. **Auto-guardado cada N segundos**
2. **Sincronización con nube (Google Drive/OneDrive)**
3. **Historial de cambios (Git-like)**
4. **Notificaciones de guardado exitoso**
5. **Base de datos SQLite en lugar de CSV**

---

## 🎉 Resumen

### **Antes:**
```
❌ Guardado simple sin verificación
❌ Sin backups automáticos
❌ Sin manejo de errores
❌ Pérdida de datos frecuente
```

### **Ahora:**
```
✅ Guardado robusto con verificación
✅ Backups automáticos
✅ Manejo completo de errores
✅ Restauración automática
✅ Indicadores visuales
✅ Protección contra pérdida de datos
```

---

**¡Tus datos ahora están protegidos!** 🛡️

Si experimentas algún problema, consulta este documento o ejecuta `backup.bat` regularmente.
