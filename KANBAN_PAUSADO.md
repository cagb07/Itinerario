# ⏸️ Estado "Pausado" en el Kanban

## 🎉 Nueva Funcionalidad Implementada

Se ha agregado una **cuarta columna "Pausado"** al tablero Kanban para gestionar mejor los informes que necesitan ser detenidos temporalmente.

---

## 📊 Flujo de Estados Actualizado

### **Antes (3 estados):**
```
Pendiente → En Proceso → Terminado
```

### **Ahora (4 estados):**
```
Pendiente → En Proceso ⇄ Pausado
                ↓
           Terminado
```

---

## 🎯 Estados Disponibles

| Estado | Icono | Color | Descripción |
|--------|-------|-------|-------------|
| **Pendiente** | 🔴 | Rojo | Informe creado, esperando inicio |
| **En Proceso** | 🟡 | Amarillo | Trabajo activo en el informe |
| **Pausado** | ⏸️ | Gris | Temporalmente detenido |
| **Terminado** | 🟢 | Verde | Informe completado |

---

## 🚀 Cómo Usar el Estado Pausado

### **Pausar un Informe en Proceso**

1. Localiza la tarjeta en **"🟡 En Proceso"**
2. Haz clic en **"⏸️ Pausar"**
3. La tarjeta se moverá a **"⏸️ Pausado"**

**Cuándo pausar:**
- Esperando información del centro
- Falta de recursos temporalmente
- Prioridad cambiada a otros informes
- Problemas técnicos o logísticos
- Espera de aprobaciones

---

### **Reanudar un Informe Pausado**

Desde la columna **"⏸️ Pausado"** tienes dos opciones:

#### **Opción 1: Reanudar (volver a En Proceso)**
1. Haz clic en **"▶️ Reanudar"**
2. La tarjeta vuelve a **"🟡 En Proceso"**
3. Continúa el trabajo normalmente

#### **Opción 2: Volver a Pendiente**
1. Haz clic en **"⬅️ Pendiente"**
2. La tarjeta vuelve a **"🔴 Pendiente"**
3. Útil si necesitas reiniciar el proceso

---

## 💡 Casos de Uso

### **Caso 1: Esperando Documentación**

**Situación:** Iniciaste un informe pero el centro no ha enviado documentos necesarios

**Pasos:**
1. Mueve a **"⏸️ Pausado"**
2. Agrega observación:
   ```
   PAUSADO: 24/11/2025
   MOTIVO: Esperando documentación administrativa
   PENDIENTE: 
   - Certificados de matrícula
   - Informes de evaluación
   SEGUIMIENTO: Contactar al centro el 01/12/2025
   ```
3. Cuando llegue la documentación, haz clic en **"▶️ Reanudar"**

---

### **Caso 2: Cambio de Prioridades**

**Situación:** Surge un informe urgente y necesitas pausar el actual

**Pasos:**
1. Mueve el informe actual a **"⏸️ Pausado"**
2. Agrega observación:
   ```
   PAUSADO: 24/11/2025
   MOTIVO: Prioridad cambiada a Informe Urgente XYZ
   AVANCE: 60% completado
   RETOMAR: Después del 30/11/2025
   ```
3. Trabaja en el informe urgente
4. Cuando termines, **"▶️ Reanudar"** el pausado

---

### **Caso 3: Problemas Técnicos**

**Situación:** El sistema de información del centro está caído

**Pasos:**
1. Mueve a **"⏸️ Pausado"**
2. Agrega observación:
   ```
   PAUSADO: 24/11/2025
   MOTIVO: Sistema de información del centro fuera de servicio
   CONTACTO: Técnico reportó que estará disponible el 26/11/2025
   ACCIÓN: Esperar resolución técnica
   ```
3. Cuando se resuelva, **"▶️ Reanudar"**

---

### **Caso 4: Espera de Aprobación**

**Situación:** Necesitas aprobación de un supervisor antes de continuar

**Pasos:**
1. Mueve a **"⏸️ Pausado"**
2. Agrega observación:
   ```
   PAUSADO: 24/11/2025
   MOTIVO: Esperando aprobación de supervisor
   ENVIADO: Borrador enviado a María González
   ESPERADO: Respuesta en 2-3 días hábiles
   ```
3. Al recibir aprobación, **"▶️ Reanudar"**

---

## 📊 Dashboard Actualizado

El **Dashboard de Control** ahora muestra 5 métricas:

```
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│ 📋          │ ⚡          │ ⏸️          │ ✅          │ 📊          │
│ Pendientes  │ En Proceso  │ Pausados    │ Terminados  │ Total       │
│     5       │      3      │      2      │     10      │     20      │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

---

## 🎨 Visualización en el Kanban

### **Diseño de 4 Columnas**

```
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ 🔴 Pendiente │ 🟡 En Proceso│ ⏸️ Pausado   │ 🟢 Terminado │
├──────────────┼──────────────┼──────────────┼──────────────┤
│              │              │              │              │
│ [Tarjeta 1]  │ [Tarjeta 3]  │ [Tarjeta 5]  │ [Tarjeta 7]  │
│ [➡️ Iniciar] │ [⏸️ Pausar]  │ [⬅️ Pend.]  │ [↩️ Reabrir] │
│              │ [✅ Terminar]│ [▶️ Reanudar]│              │
│              │              │              │              │
│ [Tarjeta 2]  │ [Tarjeta 4]  │ [Tarjeta 6]  │ [Tarjeta 8]  │
│              │              │              │              │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

---

## 🔄 Transiciones de Estado

### **Desde Pendiente:**
- ➡️ **Iniciar** → En Proceso

### **Desde En Proceso:**
- ⏸️ **Pausar** → Pausado
- ✅ **Terminar** → Terminado

### **Desde Pausado:**
- ⬅️ **Pendiente** → Pendiente
- ▶️ **Reanudar** → En Proceso

### **Desde Terminado:**
- ↩️ **Reabrir** → En Proceso

---

## 📝 Mejores Prácticas

### **Cuándo Pausar:**
✅ Esperando información externa
✅ Falta de recursos temporales
✅ Cambio de prioridades
✅ Problemas técnicos
✅ Espera de aprobaciones
✅ Vacaciones o ausencias

### **Cuándo NO Pausar:**
❌ Solo porque no quieres trabajar en ello (usa Pendiente)
❌ Si el informe está terminado (usa Terminado)
❌ Si nunca se va a reanudar (elimínalo)

### **Documentar Siempre:**
Cuando pauses un informe, **agrega observaciones** explicando:
1. **Motivo** del pauso
2. **Qué se necesita** para reanudar
3. **Fecha estimada** de reanudación
4. **Avance actual** (opcional)

---

## 📊 Reportes y Estadísticas

### **Métricas Útiles:**
- **Tasa de pausa**: Pausados / Total
- **Tiempo promedio pausado**: Días en estado pausado
- **Motivos más comunes**: Análisis de observaciones

### **Alertas Sugeridas:**
- ⚠️ Informes pausados por más de 7 días
- ⚠️ Más de 3 informes pausados simultáneamente
- ⚠️ Informes pausados sin observaciones

---

## 🔧 Integración con Otras Secciones

### **Dashboard:**
- Muestra contador de pausados
- Incluye en gráficos de estado

### **Calendario:**
- Los informes pausados no afectan las citas
- Puedes tener cita agendada con informe pausado

### **Base de Datos:**
- El estado "Pausado" se guarda en `seguimiento_informes.csv`
- Se puede filtrar y exportar

---

## 💾 Estructura de Datos

El archivo `seguimiento_informes.csv` ahora incluye el estado "Pausado":

```csv
ID,Centro,Estado,Fecha_Inicio,Fecha_Fin,Responsable,Prioridad,Observaciones
1,Escuela ABC,En Proceso,2025-11-20,,Jeremy,Alta,""
2,Liceo XYZ,Pausado,2025-11-22,,Ana,Media,"Esperando documentación..."
3,Colegio 123,Terminado,2025-11-15,2025-11-24,Carlos,Baja,""
```

---

## 🎯 Ventajas del Estado Pausado

### **Organización:**
✅ Separa informes activos de detenidos
✅ Mejor visibilidad del trabajo real
✅ Facilita priorización

### **Seguimiento:**
✅ Identifica bloqueos rápidamente
✅ Documenta razones de retrasos
✅ Mejora planificación

### **Comunicación:**
✅ Equipo sabe qué está detenido
✅ Transparencia en el proceso
✅ Facilita coordinación

---

## 🆘 Preguntas Frecuentes

### **¿Cuál es la diferencia entre Pausado y Pendiente?**
- **Pendiente**: Nunca se ha iniciado
- **Pausado**: Ya se inició pero se detuvo temporalmente

### **¿Puedo pausar un informe terminado?**
No. Los informes terminados solo pueden reabrirse a "En Proceso".

### **¿Se pierde información al pausar?**
No. Todas las observaciones y datos se mantienen.

### **¿Cuánto tiempo puede estar pausado un informe?**
No hay límite, pero se recomienda revisar pausados semanalmente.

### **¿Puedo mover directamente de Pausado a Terminado?**
No. Debes reanudar primero (En Proceso) y luego terminar.

---

## 📈 Ejemplo de Flujo Completo

```
1. CREAR INFORME
   Estado: Pendiente
   Observación: "Informe para Escuela ABC"

2. INICIAR TRABAJO
   Estado: En Proceso
   Observación: "Iniciada revisión de instalaciones"

3. PAUSAR (Esperando info)
   Estado: Pausado
   Observación: "Pausado - Esperando certificados del centro"

4. REANUDAR (Info recibida)
   Estado: En Proceso
   Observación: "Reanudado - Certificados recibidos"

5. TERMINAR
   Estado: Terminado
   Observación: "Informe completado y enviado"
```

---

## 🎉 ¡Kanban Completo con 4 Estados!

Ahora tienes un sistema Kanban profesional con:
- ✅ 4 estados (Pendiente, En Proceso, Pausado, Terminado)
- ✅ Transiciones claras entre estados
- ✅ Dashboard actualizado con métricas
- ✅ Mejor gestión de bloqueos y pausas
- ✅ Documentación de motivos de pausa

---

**Desarrollado para optimizar la gestión de informes educativos** 📚
