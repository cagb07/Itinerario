# 📅 Sistema de Calendario Mejorado - Control de Informes

## 🎉 Mejoras Implementadas

### ✨ Nuevas Funcionalidades

#### 1. **📊 Dashboard de Estadísticas**
- **Métricas en tiempo real**: Total de citas, pendientes, confirmadas, completadas y citas del día
- **Visualización instantánea** del estado de la agenda

#### 2. **👀 Vistas Múltiples de Agenda**

##### Vista Diaria
- Itinerario completo del día seleccionado (8am - 4pm)
- Indicadores visuales por prioridad (colores)
- Estados de citas con iconos (⏳ Pendiente, ✅ Confirmada, 🎯 Completada, ❌ Cancelada)
- Visualización de notas y detalles de cada cita

##### Vista Semanal
- Visualización de 5 días laborables (Lunes a Viernes)
- Resumen compacto de citas por día
- Códigos de color por prioridad

#### 3. **🔍 Búsqueda Avanzada al Agendar**
- **Búsqueda de texto libre**: Filtra por nombre, código o cantón
- **Filtros combinados**: Provincia + Categoría + Búsqueda
- **Contador de resultados**: Muestra cuántos centros coinciden con los filtros

#### 4. **⚙️ Gestión Completa de Citas (CRUD)**
- **Editar estado**: Cambiar entre Pendiente, Confirmada, Completada, Cancelada
- **Eliminar citas**: Remover citas programadas
- **Reprogramar** (en calendario_module.py): Cambiar fecha y hora
- **Filtros de gestión**: Ver citas por estado y rango de fechas

#### 5. **🛡️ Validaciones Inteligentes**
- ❌ **No permite fines de semana**
- ❌ **No permite fechas pasadas**
- ❌ **Detecta horarios ocupados**
- ⚠️ **Advierte si el centro ya tiene informe terminado**
- ⚠️ **Límite diario**: Máximo 7 citas por día (configurable en generador automático)

#### 6. **✅ Integración Kanban-Calendario**
- **Opción al agendar**: Crear entrada en Kanban automáticamente
- **Sincronización**: Al completar una cita, se actualiza el Kanban
- **Evita duplicados**: No agenda centros que ya están en el Kanban como "Terminado"

#### 7. **🤖 Generador Automático Optimizado**

##### Parámetros Configurables:
- **Fecha de inicio** personalizada
- **Máximo de citas por día** (1-7)
- **Días a planificar** (1-30)
- **Categorías a incluir** (selección múltiple)

##### Optimizaciones:
- **Agrupación geográfica**: Agrupa centros de la misma provincia/cantón
- **Exclusión inteligente**: No agenda centros con informe terminado o ya agendados
- **Distribución equilibrada**: Respeta el límite de citas por día
- **Salto de fines de semana** automático

##### Resultados:
- **Vista previa** de las primeras 10 citas generadas
- **Resumen**: Total de citas, días cubiertos, provincias
- **Descarga CSV** del itinerario generado

#### 8. **📈 Estadísticas y Análisis** (en calendario_module.py)
- Gráficos de citas por estado
- Distribución por provincia
- Citas por prioridad
- Análisis por día de la semana
- Carga semanal

#### 9. **📤 Exportación de Datos**
- **CSV completo**: Descarga toda la agenda
- **Formato ICS** (iCalendar): Compatible con Google Calendar, Outlook, Apple Calendar
- **Itinerarios generados**: Descarga automática de agendas creadas

#### 10. **🎨 Mejoras de UX**
- **Diseño moderno** con tarjetas y colores
- **Iconos intuitivos** para cada estado
- **Tooltips informativos**
- **Feedback visual** en todas las acciones
- **Mensajes de confirmación** claros

---

## 📁 Estructura de Archivos

```
Itinerario/
├── app.py                    # Aplicación principal (Dashboard, Kanban, Base de Datos)
├── calendario_module.py      # Módulo del sistema de calendario mejorado
├── LISTADO-CON-FASES.csv    # Base de datos de centros educativos
├── seguimiento_informes.csv  # Datos del Kanban
└── calendario.csv            # Datos de citas programadas
```

---

## 🚀 Cómo Usar el Nuevo Sistema

### Agendar una Cita Manual

1. Ve a **Calendario** > **➕ Agendar Cita**
2. Usa la búsqueda y filtros para encontrar el centro
3. Selecciona fecha, hora y prioridad
4. Agrega notas si es necesario
5. Marca "Crear en Kanban" si quieres seguimiento
6. Haz clic en **📅 Agendar**

### Generar Agenda Automática

1. Ve a **Calendario** > **🤖 Generador Automático**
2. Configura:
   - Fecha de inicio
   - Máximo de citas por día
   - Días a planificar
   - Categorías a incluir
3. Haz clic en **🚀 Generar**
4. Revisa la vista previa
5. Descarga el CSV si lo necesitas

### Gestionar Citas Existentes

1. Ve a **Calendario** > **⚙️ Gestionar Citas**
2. Filtra por estado y fechas
3. Expande la cita que quieres modificar
4. Cambia el estado o elimínala

### Ver la Agenda

1. Ve a **Calendario** > **👀 Ver Agenda**
2. Selecciona **Vista Diaria** o **Vista Semanal**
3. Navega por las fechas

---

## 🔧 Campos de la Base de Datos de Calendario

| Campo | Descripción |
|-------|-------------|
| `ID_Cita` | Identificador único de la cita |
| `Fecha` | Fecha de la visita |
| `Hora` | Hora de inicio (8-16, excepto 12) |
| `Centro` | Nombre del centro educativo |
| `Provincia` | Provincia del centro |
| `Canton` | Cantón del centro |
| `Categoria` | Categoría del catálogo |
| `Prioridad` | Baja, Media o Alta |
| `Nota` | Observaciones de la visita |
| `Estado` | Pendiente, Confirmada, Completada o Cancelada |
| `Fecha_Creacion` | Fecha en que se agendó |

---

## 📊 Estados de Citas

| Estado | Icono | Descripción |
|--------|-------|-------------|
| **Pendiente** | ⏳ | Cita programada, no confirmada |
| **Confirmada** | ✅ | Cita confirmada con el centro |
| **Completada** | 🎯 | Visita realizada |
| **Cancelada** | ❌ | Cita cancelada |

---

## 🎨 Códigos de Color por Prioridad

- 🔴 **Alta**: Rojo (#e74c3c)
- 🟡 **Media**: Amarillo/Naranja (#f39c12)
- 🔵 **Baja**: Azul (#3498db)

---

## 💡 Consejos de Uso

1. **Usa el generador automático** para planificar semanas completas rápidamente
2. **Marca las citas como confirmadas** una vez que contactes al centro
3. **Actualiza a "Completada"** después de cada visita para sincronizar con el Kanban
4. **Exporta a ICS** para tener las citas en tu calendario personal
5. **Revisa las estadísticas** regularmente para optimizar tu agenda

---

## 🐛 Solución de Problemas

### La cita no se guarda
- Verifica que no sea fin de semana
- Asegúrate de que el horario no esté ocupado
- Revisa que hayas seleccionado un centro válido

### No aparecen centros en la búsqueda
- Verifica que el archivo `LISTADO-CON-FASES.csv` exista
- Prueba con filtros menos restrictivos
- Limpia el campo de búsqueda

### El generador automático no crea citas
- Asegúrate de que haya centros disponibles (sin informe terminado)
- Verifica que las categorías seleccionadas existan en la base de datos
- Aumenta el número de días a planificar

---

## 📝 Notas Técnicas

- **Módulo separado**: El calendario está en `calendario_module.py` para mejor organización
- **Persistencia**: Todos los datos se guardan en CSV automáticamente
- **Caché**: Los datos maestros usan `@st.cache_data` para mejor rendimiento
- **Validaciones**: Todas las entradas se validan antes de guardar

---

## 🎯 Próximas Mejoras Sugeridas

- [ ] Notificaciones por email de citas próximas
- [ ] Drag & drop para reprogramar citas
- [ ] Vista mensual tipo calendario
- [ ] Optimización de rutas con Google Maps API
- [ ] Exportación a PDF del itinerario semanal
- [ ] Recordatorios automáticos

---

**Desarrollado con ❤️ usando Streamlit**
