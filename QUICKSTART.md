# 🚀 Guía Rápida de Despliegue

## ✅ Archivos Listos para Despliegue

### 📦 Archivos Principales
- ✅ `app.py` - Aplicación principal
- ✅ `calendario_module.py` - Módulo de calendario
- ✅ `requirements.txt` - Dependencias de Python
- ✅ `.streamlit/config.toml` - Configuración de tema oscuro
- ✅ `.gitignore` - Archivos ignorados por Git

### 📚 Documentación
- ✅ `README.md` - Documentación principal del proyecto
- ✅ `DEPLOY.md` - Guía completa de despliegue
- ✅ `MEJORAS_CALENDARIO.md` - Funcionalidades del calendario
- ✅ `GESTION_CENTROS.md` - Gestión de base de datos

### 🛠️ Scripts Útiles
- ✅ `start_app.bat` - Inicia la aplicación en Windows
- ✅ `backup.bat` - Crea backup de datos

### 📊 Datos
- ✅ `ejemplo_centros.csv` - Archivo de ejemplo para importar

---

## 🎯 Opciones de Despliegue

### 1️⃣ Streamlit Cloud (Más Fácil) ⭐ RECOMENDADO

**Tiempo:** ~10 minutos

```bash
# 1. Crear repositorio en GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU_USUARIO/control-informes.git
git push -u origin main

# 2. Ir a https://share.streamlit.io
# 3. Conectar con GitHub
# 4. Seleccionar repositorio y app.py
# 5. ¡Deploy!
```

**URL final:** `https://TU_USUARIO-control-informes-app-XXXXX.streamlit.app`

---

### 2️⃣ Servidor Local/Intranet (Más Control)

**Tiempo:** ~5 minutos

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Iniciar aplicación
streamlit run app.py

# O usar el script:
start_app.bat
```

**URL local:** `http://localhost:8501`
**URL red:** `http://TU_IP:8501`

---

### 3️⃣ Docker (Más Portable)

**Tiempo:** ~15 minutos

```bash
# 1. Construir imagen
docker build -t control-informes .

# 2. Ejecutar contenedor
docker run -p 8501:8501 control-informes
```

**URL:** `http://localhost:8501`

---

## 📋 Checklist Pre-Despliegue

### Antes de Desplegar
- [ ] Verificar que `requirements.txt` existe
- [ ] Probar localmente con `streamlit run app.py`
- [ ] Revisar que `.gitignore` está configurado
- [ ] Crear backup de datos con `backup.bat`
- [ ] Leer `DEPLOY.md` para tu opción elegida

### Después de Desplegar
- [ ] Verificar que la app carga correctamente
- [ ] Probar cada sección (Dashboard, Kanban, Calendario, Base de Datos)
- [ ] Importar datos iniciales si es necesario
- [ ] Configurar backup automático
- [ ] Documentar URL de acceso
- [ ] Capacitar usuarios

---

## 🔧 Comandos Útiles

### Desarrollo Local
```bash
# Iniciar app
streamlit run app.py

# Iniciar en puerto específico
streamlit run app.py --server.port 8502

# Limpiar caché
# Dentro de la app: Ctrl+C → Reiniciar
```

### Mantenimiento
```bash
# Crear backup
backup.bat

# Actualizar dependencias
pip install --upgrade streamlit pandas

# Ver logs (en la terminal donde corre la app)
```

### Git
```bash
# Subir cambios
git add .
git commit -m "Descripción del cambio"
git push origin main

# Ver estado
git status

# Ver historial
git log --oneline
```

---

## 🆘 Solución Rápida de Problemas

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### "Address already in use"
```bash
streamlit run app.py --server.port 8502
```

### "Cannot connect to app"
1. Verifica firewall
2. Usa `--server.address 0.0.0.0`
3. Verifica IP correcta

### App muy lenta
1. Limpia caché: `st.cache_data.clear()`
2. Reduce tamaño de CSV
3. Reinicia la app

---

## 📞 Recursos

- **Documentación Completa:** Ver `DEPLOY.md`
- **Streamlit Docs:** https://docs.streamlit.io
- **Soporte:** https://discuss.streamlit.io

---

## 🎉 ¡Listo para Desplegar!

**Opción Recomendada para Empezar:**
1. Prueba local con `start_app.bat`
2. Si funciona bien, despliega en Streamlit Cloud

**Tiempo Total Estimado:** 15-30 minutos

---

**¿Necesitas ayuda?** Consulta `DEPLOY.md` para guías detalladas de cada opción.
