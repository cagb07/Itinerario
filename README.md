# 📝 Sistema de Control de Informes

Sistema completo de gestión y planificación de informes para centros educativos con **autenticación de usuarios** y **calendarios independientes**, desarrollado con Streamlit.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.51.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Características Principales

### 🔐 Sistema de Autenticación (NUEVO)
- **Login seguro** con usuario y contraseña
- **Contraseñas encriptadas** con SHA-256
- **Roles de usuario**: Admin y Usuario estándar
- **Gestión de usuarios**: Crear, activar/desactivar, cambiar contraseñas
- **Sesiones persistentes** durante toda la navegación
- **Usuario por defecto**: `admin` / `admin123`

### 📅 Calendarios Individuales por Usuario (NUEVO)
- **Calendarios privados**: Cada usuario tiene su propio calendario
- **Archivos independientes**: `calendario_usuario.csv` por cada usuario
- **No más conflictos**: Las agendas no se borran entre usuarios
- **Privacidad total**: Solo ves tu propio calendario

### 📊 Dashboard de Control
- Monitoreo en tiempo real del avance de informes
- Métricas de cobertura global
- Visualización del flujo de trabajo
- Gráficos de actividad reciente

### 📋 Kanban de Informes
- Tablero visual de seguimiento (Pendiente → En Proceso → Terminado)
- Búsqueda avanzada de centros educativos
- Gestión de prioridades
- Asignación de responsables

### 📅 Sistema de Calendario Mejorado
- **Vistas múltiples**: Diaria, Semanal
- **Búsqueda inteligente**: Por cualquier criterio (nombre, código, provincia, cantón)
- **Gestión completa de citas**: Crear, editar, eliminar, reprogramar
- **Estados de citas**: Pendiente, Confirmada, Completada, Cancelada
- **Generador automático**: Crea itinerarios optimizados
- **Validaciones inteligentes**: Evita conflictos y duplicados
- **Integración Kanban-Calendario**: Sincronización bidireccional
- **Bug de borrado SOLUCIONADO**: Ya no se pierden agendas al actualizar/eliminar

### 📂 Gestión de Base de Datos
- **Agregar centros**: Manual o importación masiva CSV
- **Editar/Eliminar**: Gestión completa de centros
- **Búsqueda avanzada**: Por cualquier campo
- **Exportación**: Descarga filtrada o completa
- **Validaciones**: Evita duplicados

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8 o superior
- pip

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/cagb07/Itinerario.git
cd Itinerario

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run app.py
```

La aplicación estará disponible en `http://localhost:8501`

### 🔐 Primer Login

Al iniciar por primera vez, usa las credenciales por defecto:
- **Usuario:** `admin`
- **Contraseña:** `admin123`

⚠️ **IMPORTANTE:** Cambia la contraseña del admin inmediatamente después del primer inicio.

## 📁 Estructura del Proyecto

```
Itinerario/
├── app.py                         # Aplicación principal
├── auth_module.py                 # Sistema de autenticación (NUEVO)
├── calendario_module.py           # Módulo de calendario (MEJORADO)
├── requirements.txt               # Dependencias de Python
├── .streamlit/
│   └── config.toml               # Configuración (tema oscuro)
├── .gitignore                    # Archivos ignorados por Git
├── LISTADO-CON-FASES.csv         # Base de datos de centros
├── seguimiento_informes.csv       # Datos del Kanban (compartido)
├── usuarios.csv                   # Base de datos de usuarios (NUEVO)
├── calendario_usuario.csv         # Calendarios por usuario (NUEVO)
├── test_auth.py                   # Tests de autenticación (NUEVO)
├── test_calendario.py             # Tests de calendario (NUEVO)
├── DEPLOY.md                      # Guía de despliegue
├── SISTEMA_AUTENTICACION.md       # Documentación técnica (NUEVO)
├── GUIA_USO.md                    # Guía rápida de usuario (NUEVO)
├── MEJORAS_CALENDARIO.md          # Documentación del calendario
├── GESTION_CENTROS.md             # Documentación de gestión
└── README.md                      # Este archivo
```

## 📚 Documentación

- **[GUIA_USO.md](GUIA_USO.md)** - Guía rápida para usuarios
- **[SISTEMA_AUTENTICACION.md](SISTEMA_AUTENTICACION.md)** - Documentación técnica completa del sistema de autenticación
- **[MEJORAS_CALENDARIO.md](MEJORAS_CALENDARIO.md)** - Detalles del sistema de calendario
- **[GESTION_CENTROS.md](GESTION_CENTROS.md)** - Gestión de base de datos
- **[DEPLOY.md](DEPLOY.md)** - Guía de despliegue en producción

## 🆕 Cambios Recientes (v2.0)

### ✅ Implementaciones Nuevas
- 🔐 **Sistema de autenticación completo** con usuarios y contraseñas
- 👥 **Gestión de usuarios** para administradores
- 📅 **Calendarios independientes** por usuario
- 🔒 **Contraseñas encriptadas** con SHA-256
- 💾 **Sesiones persistentes** con `st.session_state`

### 🐛 Bugs Corregidos
- ✅ **Bug de borrado de agendas**: Las citas ya no se pierden al actualizar o eliminar
- ✅ **Sobrescritura de calendarios**: Los usuarios ya no comparten el mismo archivo
- ✅ **Duplicación de registros**: La generación automática ya no duplica citas
- ✅ **Índices incorrectos**: Eliminación de citas ahora resetea índices correctamente

## 🎨 Capturas de Pantalla

### Pantalla de Login (NUEVO)
![Login](docs/login.png)

### Dashboard de Control
![Dashboard](docs/dashboard.png)

### Kanban de Informes
![Kanban](docs/kanban.png)

### Calendario - Vista Diaria
![Calendario](docs/calendario.png)

### Gestión de Centros
![Gestión](docs/gestion.png)

## 📖 Documentación

- **[DEPLOY.md](DEPLOY.md)** - Guía completa de despliegue
- **[MEJORAS_CALENDARIO.md](MEJORAS_CALENDARIO.md)** - Funcionalidades del calendario
- **[GESTION_CENTROS.md](GESTION_CENTROS.md)** - Gestión de base de datos

## 🔧 Configuración

### Tema Oscuro
El sistema usa tema oscuro por defecto. Configuración en `.streamlit/config.toml`:

```toml
[theme]
base="dark"
primaryColor="#3498db"
backgroundColor="#0e1117"
secondaryBackgroundColor="#262730"
textColor="#fafafa"
```

### Archivos de Datos
- `LISTADO-CON-FASES.csv` - Base de datos de centros educativos
- `seguimiento_informes.csv` - Estado de informes (Kanban)
- `calendario.csv` - Citas programadas

## 🚀 Despliegue

### Streamlit Cloud (Recomendado)
1. Sube el código a GitHub
2. Conecta con [Streamlit Cloud](https://share.streamlit.io)
3. Despliega con un clic

Ver [DEPLOY.md](DEPLOY.md) para más opciones (Heroku, Docker, servidor local).

## 💡 Uso

### 1. Agregar Centros Educativos
```
Base de Datos → Agregar Centros → Manual o CSV
```

### 2. Crear Informe en Kanban
```
Kanban de Informes → Iniciar Nuevo Informe → Seleccionar Centro
```

### 3. Agendar Cita
```
Calendario → Agendar Cita → Buscar Centro → Programar
```

### 4. Generar Itinerario Automático
```
Calendario → Generador Automático → Configurar → Generar
```

## 🔒 Seguridad

- Los archivos CSV con datos reales no se suben a Git (ver `.gitignore`)
- Opción de agregar autenticación (ver `DEPLOY.md`)
- Backup automático recomendado

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Changelog

### v2.0.0 (2025-11-24)
- ✨ Sistema de calendario completamente rediseñado
- ✨ Vistas múltiples (Diaria, Semanal)
- ✨ Búsqueda por cualquier criterio
- ✨ Gestión completa de citas (CRUD)
- ✨ Generador automático optimizado
- ✨ Integración Kanban-Calendario
- ✨ Exportación ICS
- ✨ Gestión de centros educativos (agregar, editar, eliminar)
- ✨ Importación masiva CSV
- 🎨 Tema oscuro permanente
- 🎨 Mejoras visuales en todas las secciones

### v1.0.0 (2025-11-21)
- 🎉 Versión inicial
- Dashboard de control
- Kanban de informes
- Calendario básico

## 🐛 Reportar Problemas

Si encuentras un bug o tienes una sugerencia:
1. Verifica que no exista un issue similar
2. Crea un nuevo issue con detalles
3. Incluye capturas de pantalla si es posible

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Jeremy Fernández**
- Sistema desarrollado para la gestión de informes de centros educativos

## 🙏 Agradecimientos

- [Streamlit](https://streamlit.io) - Framework de desarrollo
- [Pandas](https://pandas.pydata.org) - Manipulación de datos
- Comunidad de Streamlit por el soporte

## 📞 Soporte

Para soporte técnico:
- 📧 Email: soporte@ejemplo.com
- 💬 Discord: [Servidor de Soporte](#)
- 📖 Documentación: Ver archivos `.md` en el proyecto

---

**Desarrollado con ❤️ usando Streamlit**

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub
