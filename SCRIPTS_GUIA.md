# 🚀 Scripts de Inicio - Guía de Uso

## 📁 Scripts Disponibles

### 1. **INICIAR.bat** ⭐ RECOMENDADO

Script completo con todas las verificaciones y configuración automática.

**Características:**
- ✅ Verifica instalación de Python
- ✅ Verifica directorio correcto
- ✅ Instala dependencias automáticamente
- ✅ Verifica archivos de datos
- ✅ Abre navegador automáticamente
- ✅ Mensajes coloridos y claros
- ✅ Manejo de errores

**Cuándo usar:**
- Primera vez que ejecutas la aplicación
- Después de actualizar el código
- Si tienes problemas al iniciar
- Si no estás seguro de las dependencias

**Cómo usar:**
```
1. Doble clic en INICIAR.bat
2. Espera a que termine las verificaciones
3. El navegador se abrirá automáticamente
4. ¡Listo!
```

---

### 2. **INICIO_RAPIDO.bat** ⚡

Script minimalista para inicio rápido sin verificaciones.

**Características:**
- ⚡ Inicio instantáneo
- 🎯 Sin verificaciones
- 📝 3 líneas de código
- 🚀 Para usuarios avanzados

**Cuándo usar:**
- Ya verificaste que todo funciona
- Quieres inicio rápido
- Eres usuario avanzado
- Desarrollo/testing frecuente

**Cómo usar:**
```
1. Doble clic en INICIO_RAPIDO.bat
2. ¡Listo!
```

---

### 3. **DETENER.bat** 🛑

Script para detener la aplicación de forma segura.

**Características:**
- 🔍 Busca procesos de Streamlit
- ⚠️ Pide confirmación
- 🛑 Detiene todos los procesos
- ✅ Confirmación de cierre

**Cuándo usar:**
- Quieres cerrar la aplicación
- Tienes múltiples instancias corriendo
- La ventana de terminal se cerró pero la app sigue corriendo

**Cómo usar:**
```
1. Doble clic en DETENER.bat
2. Confirma con 'S'
3. ¡Listo!
```

---

### 4. **backup.bat** 💾

Script para crear copias de seguridad de los datos.

**Características:**
- 📦 Crea backup con timestamp
- 🗂️ Guarda en carpeta backups/
- 🧹 Limpia backups antiguos (mantiene últimos 10)
- ✅ Copia todos los CSV

**Cuándo usar:**
- Antes de importar datos masivos
- Antes de actualizar la aplicación
- Regularmente (semanal/mensual)
- Antes de hacer cambios importantes

**Cómo usar:**
```
1. Doble clic en backup.bat
2. Espera confirmación
3. ¡Listo!
```

---

## 🎯 Flujo de Trabajo Recomendado

### **Primera Vez:**
```
1. INICIAR.bat (verifica todo)
2. Usar la aplicación
3. DETENER.bat (cuando termines)
```

### **Uso Diario:**
```
1. INICIO_RAPIDO.bat
2. Usar la aplicación
3. Ctrl+C en la terminal (o DETENER.bat)
```

### **Antes de Cambios Importantes:**
```
1. backup.bat
2. INICIAR.bat
3. Hacer cambios
4. DETENER.bat
```

---

## 🔧 Solución de Problemas

### **Error: "Python no está instalado"**

**Solución:**
1. Descarga Python desde: https://www.python.org/downloads/
2. Durante instalación, marca "Add Python to PATH"
3. Reinicia la computadora
4. Ejecuta INICIAR.bat nuevamente

---

### **Error: "No se encuentra app.py"**

**Solución:**
1. Verifica que estás en la carpeta correcta
2. La carpeta debe contener:
   - app.py
   - calendario_module.py
   - requirements.txt
   - INICIAR.bat
3. Si falta app.py, descarga el proyecto completo

---

### **Error: "No se pudieron instalar las dependencias"**

**Solución:**
```bash
# Opción 1: Manual
pip install streamlit pandas

# Opción 2: Desde requirements.txt
pip install -r requirements.txt

# Opción 3: Actualizar pip
python -m pip install --upgrade pip
pip install streamlit pandas
```

---

### **La aplicación no se abre en el navegador**

**Solución:**
1. Abre manualmente: http://localhost:8501
2. Si no funciona, verifica el puerto:
   - Mira la terminal, puede estar en otro puerto (8502, 8503, etc.)
3. Prueba: http://localhost:8502

---

### **Múltiples instancias corriendo**

**Solución:**
1. Ejecuta DETENER.bat
2. Confirma con 'S'
3. Espera a que termine
4. Ejecuta INICIAR.bat nuevamente

---

### **Error: "Address already in use"**

**Solución:**
```bash
# Opción 1: Detener instancias anteriores
DETENER.bat

# Opción 2: Usar otro puerto
python -m streamlit run app.py --server.port 8502
```

---

## 📝 Personalización de Scripts

### **Cambiar Puerto por Defecto**

Edita `INICIAR.bat` o `INICIO_RAPIDO.bat`:

```batch
REM Cambiar esta línea:
python -m streamlit run app.py

REM Por esta:
python -m streamlit run app.py --server.port 8502
```

---

### **No Abrir Navegador Automáticamente**

Edita `INICIAR.bat`, comenta esta línea:

```batch
REM start http://localhost:8501
```

---

### **Cambiar Color de la Terminal**

Edita `INICIAR.bat`:

```batch
REM Colores disponibles:
color 0A  REM Verde (actual)
color 0B  REM Cyan
color 0E  REM Amarillo
color 0C  REM Rojo
```

---

## 🎨 Códigos de Color

| Código | Color | Uso |
|--------|-------|-----|
| `0A` | Verde | Éxito, normal |
| `0C` | Rojo | Errores |
| `0E` | Amarillo | Advertencias |
| `0B` | Cyan | Información |

---

## 📊 Comparación de Scripts

| Característica | INICIAR.bat | INICIO_RAPIDO.bat | DETENER.bat | backup.bat |
|----------------|-------------|-------------------|-------------|------------|
| Verifica Python | ✅ | ❌ | ❌ | ❌ |
| Instala dependencias | ✅ | ❌ | ❌ | ❌ |
| Abre navegador | ✅ | ❌ | ❌ | ❌ |
| Velocidad | Media | Rápida | Rápida | Media |
| Recomendado para | Principiantes | Avanzados | Todos | Todos |

---

## 💡 Tips y Trucos

### **Tip 1: Acceso Rápido**
Crea un acceso directo de `INICIO_RAPIDO.bat` en el escritorio para inicio con un clic.

### **Tip 2: Tarea Programada**
Programa `backup.bat` para ejecutarse automáticamente cada semana:
1. Abre "Programador de tareas"
2. Crear tarea básica
3. Trigger: Semanal
4. Acción: Ejecutar `backup.bat`

### **Tip 3: Alias de Comandos**
Crea un archivo `alias.bat` con:
```batch
@echo off
doskey iniciar=cd /d "C:\Users\icacgranad\Desktop\Itinerario" ^& INICIAR.bat
doskey detener=cd /d "C:\Users\icacgranad\Desktop\Itinerario" ^& DETENER.bat
```

### **Tip 4: Logs**
Para guardar logs de ejecución, modifica `INICIAR.bat`:
```batch
python -m streamlit run app.py > logs\app_%date%.log 2>&1
```

---

## 🆘 Soporte

Si tienes problemas:

1. **Revisa esta guía** primero
2. **Verifica los logs** en la terminal
3. **Ejecuta INICIAR.bat** (muestra más información)
4. **Consulta DEPLOY.md** para más opciones

---

## ✅ Checklist de Verificación

Antes de reportar un problema, verifica:

- [ ] Python está instalado (`python --version`)
- [ ] Estás en la carpeta correcta (existe `app.py`)
- [ ] Las dependencias están instaladas (`pip show streamlit`)
- [ ] No hay otras instancias corriendo (ejecuta `DETENER.bat`)
- [ ] El puerto 8501 está libre
- [ ] Tienes permisos de administrador (si es necesario)

---

## 📚 Archivos Relacionados

- **DEPLOY.md** - Guía completa de despliegue
- **QUICKSTART.md** - Inicio rápido general
- **README.md** - Documentación principal
- **requirements.txt** - Lista de dependencias

---

**¡Disfruta usando el Sistema de Control de Informes!** 🎉
