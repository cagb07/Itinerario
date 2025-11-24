# 🚀 Guía de Despliegue - Sistema de Control de Informes

## 📋 Tabla de Contenidos
1. [Requisitos Previos](#requisitos-previos)
2. [Opción 1: Streamlit Cloud (Recomendado)](#opción-1-streamlit-cloud-recomendado)
3. [Opción 2: Servidor Local/Intranet](#opción-2-servidor-localintranet)
4. [Opción 3: Heroku](#opción-3-heroku)
5. [Opción 4: Docker](#opción-4-docker)
6. [Configuración de Archivos](#configuración-de-archivos)
7. [Solución de Problemas](#solución-de-problemas)

---

## 📦 Requisitos Previos

### Software Necesario
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, pero recomendado)

### Archivos del Proyecto
```
Itinerario/
├── app.py                          # Aplicación principal
├── calendario_module.py            # Módulo de calendario
├── requirements.txt                # Dependencias
├── .streamlit/
│   └── config.toml                # Configuración de Streamlit
├── LISTADO-CON-FASES.csv          # Base de datos de centros
├── seguimiento_informes.csv        # Datos de Kanban
├── calendario.csv                  # Datos de calendario
├── MEJORAS_CALENDARIO.md          # Documentación
├── GESTION_CENTROS.md             # Documentación
└── ejemplo_centros.csv            # Archivo de ejemplo
```

---

## 🌐 Opción 1: Streamlit Cloud (Recomendado)

**✅ Ventajas:**
- Gratis para proyectos públicos
- Despliegue automático desde GitHub
- HTTPS incluido
- Fácil de actualizar
- No requiere servidor propio

**📝 Pasos:**

### 1. Preparar el Repositorio

#### a) Crear archivo `requirements.txt`
```bash
streamlit==1.28.0
pandas==2.1.0
```

#### b) Crear `.gitignore`
```
*.pyc
__pycache__/
.DS_Store
*.csv
!ejemplo_centros.csv
.streamlit/secrets.toml
```

**Nota:** Los archivos CSV con datos reales no se suben por seguridad.

### 2. Subir a GitHub

```bash
# Inicializar repositorio
git init

# Agregar archivos
git add app.py calendario_module.py requirements.txt .streamlit/config.toml
git add MEJORAS_CALENDARIO.md GESTION_CENTROS.md ejemplo_centros.csv

# Commit
git commit -m "Initial commit - Sistema de Control de Informes"

# Crear repositorio en GitHub (desde la web)
# Luego conectar:
git remote add origin https://github.com/TU_USUARIO/control-informes.git
git branch -M main
git push -u origin main
```

### 3. Desplegar en Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Inicia sesión con GitHub
3. Haz clic en **"New app"**
4. Selecciona:
   - **Repository**: `TU_USUARIO/control-informes`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Haz clic en **"Deploy"**

### 4. Configurar Datos Iniciales

Como los CSV no se suben a GitHub, tienes dos opciones:

**Opción A: Usar la interfaz de la app**
1. Accede a la app desplegada
2. Ve a **Base de Datos** → **Agregar Centros**
3. Importa el CSV manualmente

**Opción B: Usar Streamlit Secrets**
1. En Streamlit Cloud, ve a **Settings** → **Secrets**
2. Agrega los datos iniciales (no recomendado para muchos datos)

### 5. URL de Acceso

Tu app estará disponible en:
```
https://TU_USUARIO-control-informes-app-XXXXX.streamlit.app
```

---

## 🖥️ Opción 2: Servidor Local/Intranet

**✅ Ventajas:**
- Control total
- Datos permanecen en tu red
- Sin límites de uso
- Ideal para uso interno

**📝 Pasos:**

### 1. Instalar Dependencias

```bash
# Navegar a la carpeta del proyecto
cd C:\Users\icacgranad\Desktop\Itinerario

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar para Red Local

Edita `.streamlit/config.toml`:

```toml
[theme]
base="dark"
primaryColor="#3498db"
backgroundColor="#0e1117"
secondaryBackgroundColor="#262730"
textColor="#fafafa"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[browser]
serverAddress = "0.0.0.0"
serverPort = 8501
```

### 3. Ejecutar la Aplicación

```bash
# Opción 1: Ejecución simple
streamlit run app.py

# Opción 2: Especificar puerto
streamlit run app.py --server.port 8501

# Opción 3: Acceso desde red local
streamlit run app.py --server.address 0.0.0.0
```

### 4. Acceder desde Otros Equipos

**Desde la misma red:**
```
http://IP_DEL_SERVIDOR:8501
```

**Ejemplo:**
```
http://192.168.1.100:8501
```

**Para encontrar tu IP:**
```bash
# Windows
ipconfig

# Busca "Dirección IPv4"
```

### 5. Mantener la App Ejecutándose

**Windows - Usar `nssm` (Non-Sucking Service Manager):**

```bash
# Descargar nssm desde: https://nssm.cc/download

# Instalar como servicio
nssm install ControlInformes "C:\Python\python.exe" "-m streamlit run C:\Users\icacgranad\Desktop\Itinerario\app.py"

# Iniciar servicio
nssm start ControlInformes
```

**Alternativa - Usar Task Scheduler:**
1. Abre **Programador de tareas**
2. Crear tarea básica
3. Trigger: Al iniciar el sistema
4. Acción: Ejecutar script
5. Script: `start_app.bat`

Crea `start_app.bat`:
```batch
@echo off
cd C:\Users\icacgranad\Desktop\Itinerario
python -m streamlit run app.py
```

---

## ☁️ Opción 3: Heroku

**✅ Ventajas:**
- Gratis (con limitaciones)
- Fácil de configurar
- HTTPS incluido

**📝 Pasos:**

### 1. Crear Archivos Necesarios

#### `Procfile`
```
web: sh setup.sh && streamlit run app.py
```

#### `setup.sh`
```bash
mkdir -p ~/.streamlit/

echo "\
[theme]\n\
base='dark'\n\
primaryColor='#3498db'\n\
backgroundColor='#0e1117'\n\
secondaryBackgroundColor='#262730'\n\
textColor='#fafafa'\n\
\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

#### `runtime.txt`
```
python-3.11.5
```

### 2. Desplegar

```bash
# Instalar Heroku CLI
# Descargar desde: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Crear app
heroku create control-informes-app

# Desplegar
git push heroku main

# Abrir app
heroku open
```

---

## 🐳 Opción 4: Docker

**✅ Ventajas:**
- Portabilidad total
- Fácil de replicar
- Aislamiento de dependencias

**📝 Pasos:**

### 1. Crear `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copiar archivos
COPY requirements.txt .
COPY app.py .
COPY calendario_module.py .
COPY .streamlit .streamlit

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 8501

# Comando de inicio
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

### 2. Crear `docker-compose.yml`

```yaml
version: '3.8'

services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
    restart: unless-stopped
```

### 3. Construir y Ejecutar

```bash
# Construir imagen
docker build -t control-informes .

# Ejecutar contenedor
docker run -p 8501:8501 control-informes

# O usar docker-compose
docker-compose up -d
```

---

## 📁 Configuración de Archivos

### `requirements.txt`

```txt
streamlit==1.28.0
pandas==2.1.0
```

### `.streamlit/config.toml`

```toml
[theme]
base="dark"
primaryColor="#3498db"
backgroundColor="#0e1117"
secondaryBackgroundColor="#262730"
textColor="#fafafa"

[server]
headless = true
port = 8501
enableCORS = false
maxUploadSize = 200

[browser]
gatherUsageStats = false
```

---

## 🔒 Seguridad y Mejores Prácticas

### 1. Proteger Datos Sensibles

**No subir a GitHub:**
- `LISTADO-CON-FASES.csv` (datos reales)
- `seguimiento_informes.csv`
- `calendario.csv`

**Usar `.gitignore`:**
```
*.csv
!ejemplo_centros.csv
.streamlit/secrets.toml
```

### 2. Autenticación (Opcional)

Para agregar login, crea `.streamlit/secrets.toml`:

```toml
[passwords]
admin = "tu_password_seguro"
usuario1 = "password1"
```

Agrega al inicio de `app.py`:

```python
import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["passwords"]["admin"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        return True

if not check_password():
    st.stop()
```

### 3. Backup Automático

Crea un script `backup.py`:

```python
import shutil
import datetime
import os

def backup_data():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"backups/backup_{timestamp}"
    os.makedirs(backup_dir, exist_ok=True)
    
    files = ["LISTADO-CON-FASES.csv", "seguimiento_informes.csv", "calendario.csv"]
    for file in files:
        if os.path.exists(file):
            shutil.copy(file, f"{backup_dir}/{file}")
    
    print(f"Backup creado en: {backup_dir}")

if __name__ == "__main__":
    backup_data()
```

Ejecuta diariamente con Task Scheduler o cron.

---

## 🔧 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'streamlit'"

**Solución:**
```bash
pip install streamlit pandas
```

### Error: "Address already in use"

**Solución:**
```bash
# Cambiar puerto
streamlit run app.py --server.port 8502
```

### Error: "Cannot connect to app"

**Solución:**
1. Verifica que el firewall permita el puerto 8501
2. Usa `0.0.0.0` como server address
3. Verifica la IP correcta del servidor

### App muy lenta

**Solución:**
1. Limpia el caché: `st.cache_data.clear()`
2. Reduce el tamaño de los CSV
3. Aumenta recursos del servidor

### Datos no persisten

**Solución:**
1. Verifica permisos de escritura en la carpeta
2. En Streamlit Cloud, usa Streamlit Secrets o base de datos externa
3. Considera usar SQLite en lugar de CSV

---

## 📊 Monitoreo y Mantenimiento

### Logs

**Ver logs en tiempo real:**
```bash
# Streamlit Cloud
# Ve a la app → Settings → Logs

# Servidor local
# Los logs aparecen en la terminal
```

### Actualizar la App

**Streamlit Cloud:**
```bash
git add .
git commit -m "Actualización"
git push origin main
# Se actualiza automáticamente
```

**Servidor local:**
```bash
# Detener la app (Ctrl+C)
# Actualizar archivos
# Reiniciar
streamlit run app.py
```

---

## 📞 Soporte

### Recursos Útiles
- [Documentación Streamlit](https://docs.streamlit.io)
- [Streamlit Community](https://discuss.streamlit.io)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

### Contacto
Para soporte técnico de esta aplicación, contacta al desarrollador.

---

## ✅ Checklist de Despliegue

- [ ] Crear `requirements.txt`
- [ ] Configurar `.streamlit/config.toml`
- [ ] Crear `.gitignore`
- [ ] Probar localmente
- [ ] Crear repositorio GitHub (si aplica)
- [ ] Configurar backup de datos
- [ ] Desplegar en plataforma elegida
- [ ] Probar acceso desde otros dispositivos
- [ ] Configurar autenticación (opcional)
- [ ] Documentar URL de acceso
- [ ] Capacitar usuarios

---

**¡Listo para desplegar! 🚀**
