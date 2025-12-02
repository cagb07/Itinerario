# 🧪 Plan de Pruebas Completo - Sistema de Control de Informes

## 📋 Información General

**Fecha de Pruebas:** 2025-12-02  
**Versión:** 2.0.0  
**Tester:** Automatizado + Manual  
**Objetivo:** Verificar funcionalidad completa del sistema

---

## ✅ Checklist de Pruebas

### **1. VERIFICACIÓN DE ARCHIVOS** ✅

- [x] `app.py` existe y tiene contenido
- [x] `calendario_module.py` existe
- [x] `requirements.txt` tiene dependencias correctas
- [x] `.streamlit/config.toml` configurado
- [x] `LISTADO-CON-FASES.csv` existe (85,561 bytes)
- [x] `seguimiento_informes.csv` existe con datos (12 registros)
- [x] `calendario.csv` existe con datos (12 citas)
- [x] Scripts de inicio creados (INICIAR.bat, INICIO_RAPIDO.bat, DETENER.bat)
- [x] Documentación completa (8 archivos .md)

**Resultado:** ✅ PASS - Todos los archivos presentes

---

### **2. PRUEBAS DE INICIO DE APLICACIÓN**

#### **Test 2.1: Inicio con INICIAR.bat**
```
Pasos:
1. Ejecutar INICIAR.bat
2. Verificar que muestra verificaciones
3. Verificar que abre navegador
4. Verificar que carga en http://localhost:8501

Resultado Esperado:
- Verificaciones completas
- Navegador abre automáticamente
- App carga sin errores

Estado: ⏳ PENDIENTE (Requiere ejecución manual)
```

#### **Test 2.2: Inicio con INICIO_RAPIDO.bat**
```
Pasos:
1. Ejecutar INICIO_RAPIDO.bat
2. Verificar inicio rápido
3. Abrir manualmente http://localhost:8501

Resultado Esperado:
- Inicio inmediato
- App funcional

Estado: ⏳ PENDIENTE (Requiere ejecución manual)
```

---

### **3. PRUEBAS DE DASHBOARD**

#### **Test 3.1: Visualización de Métricas Globales**
```
Pasos:
1. Ir a "Dashboard de Control"
2. Verificar Sección 1: Cobertura Global
   - Total Centros
   - Visitados
   - Pendientes
   - % Cobertura

Datos Esperados (según archivos):
- Total Centros: ~150 (de LISTADO-CON-FASES.csv)
- Visitados: 3 (Terminados en seguimiento)
- Pendientes: Resto

Estado: ⏳ PENDIENTE
```

#### **Test 3.2: Visualización de Flujo de Trabajo**
```
Pasos:
1. Verificar Sección 2: Flujo de Trabajo Actual
2. Verificar métricas:
   - 📋 Pendientes: 7
   - ⚡ En Proceso: 1
   - ⏸️ Pausados: 1
   - ✅ Terminados: 3
   - 📊 Total: 12

Datos Esperados (según seguimiento_informes.csv):
- Pendientes: 7 (IDs 7-12)
- En Proceso: 1 (ID 6)
- Pausados: 1 (ID 4 - EL SUR)
- Terminados: 3 (IDs 1,2,3,5)

Estado: ⏳ PENDIENTE
```

#### **Test 3.3: Gráficos**
```
Pasos:
1. Verificar gráfico "Actividad Reciente"
2. Verificar gráfico "Estado Actual"

Resultado Esperado:
- Gráficos se renderizan
- Datos coinciden con CSV

Estado: ⏳ PENDIENTE
```

---

### **4. PRUEBAS DE KANBAN**

#### **Test 4.1: Visualización de Tablero**
```
Pasos:
1. Ir a "Kanban de Informes"
2. Tab "📊 Tablero Kanban"
3. Verificar 4 columnas:
   - 🔴 Pendiente (7 tarjetas)
   - 🟡 En Proceso (1 tarjeta)
   - ⏸️ Pausado (1 tarjeta)
   - 🟢 Terminado (3 tarjetas)

Datos Esperados:
- Pendiente: 7 centros
- En Proceso: J.N. DANTE ALIGHIERI
- Pausado: EL SUR (con observación)
- Terminado: MAURO FERNÁNDEZ, LA GUARIA, BAJO BURGOS, LA JOYA

Estado: ⏳ PENDIENTE
```

#### **Test 4.2: Crear Nuevo Informe**
```
Pasos:
1. Expandir "➕ Iniciar Nuevo Informe"
2. Buscar centro: "TEST"
3. Seleccionar centro de prueba
4. Responsable: "Tester"
5. Prioridad: Alta
6. Observaciones: "Informe de prueba"
7. Clic en "🚀 Iniciar Informe"

Resultado Esperado:
- Informe creado
- Aparece en columna Pendiente
- Datos guardados en CSV

Estado: ⏳ PENDIENTE
```

#### **Test 4.3: Mover Estados**
```
Pasos:
1. Seleccionar informe en Pendiente
2. Clic "➡️ Iniciar"
3. Verificar que se mueve a "En Proceso"
4. Clic "⏸️ Pausar"
5. Verificar que se mueve a "Pausado"
6. Clic "▶️ Reanudar"
7. Verificar que vuelve a "En Proceso"
8. Clic "✅ Terminar"
9. Verificar que se mueve a "Terminado"

Resultado Esperado:
- Transiciones funcionan
- Datos se guardan en cada paso
- Fechas se actualizan

Estado: ⏳ PENDIENTE
```

#### **Test 4.4: Editar Informe**
```
Pasos:
1. Seleccionar cualquier informe
2. Expandir "📝 Ver Detalles y Editar"
3. Verificar información del centro
4. Cambiar responsable
5. Cambiar prioridad
6. Agregar/editar observaciones
7. Clic "💾 Guardar Cambios"

Resultado Esperado:
- Cambios se guardan
- Mensaje de confirmación
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 4.5: Eliminar Informe**
```
Pasos:
1. Crear informe de prueba
2. Expandir "📝 Ver Detalles y Editar"
3. Clic "🗑️ Eliminar Informe"

Resultado Esperado:
- Informe eliminado
- Desaparece del tablero
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 4.6: Observaciones**
```
Pasos:
1. Verificar informe ID 4 (EL SUR)
2. Expandir detalles
3. Verificar observación: "se envia correo ya que en meraki tiene problemas de equipo fantasma"
4. Agregar nueva observación
5. Guardar

Resultado Esperado:
- Observación existente visible
- Nueva observación se agrega
- Formato preservado

Estado: ⏳ PENDIENTE
```

---

### **5. PRUEBAS DE REPORTES**

#### **Test 5.1: Filtros**
```
Pasos:
1. Tab "📈 Reportes de Estado"
2. Filtrar por Estado: Solo "Pausado"
3. Verificar que muestra 1 registro (EL SUR)
4. Filtrar por Prioridad: Solo "Alta"
5. Filtrar por fechas: 24/11/2025 - 25/11/2025

Resultado Esperado:
- Filtros funcionan
- Métricas se actualizan
- Resultados correctos

Estado: ⏳ PENDIENTE
```

#### **Test 5.2: Vista Tabla Completa**
```
Pasos:
1. Seleccionar "📋 Tabla Completa"
2. Verificar columnas
3. Verificar datos

Resultado Esperado:
- Tabla muestra todos los campos
- Observaciones truncadas a 50 caracteres
- Scroll funciona

Estado: ⏳ PENDIENTE
```

#### **Test 5.3: Vista Detalle con Observaciones**
```
Pasos:
1. Seleccionar "📝 Detalle con Observaciones"
2. Expandir varios informes
3. Verificar observaciones completas

Resultado Esperado:
- Observaciones completas visibles
- Información del centro mostrada
- Expanders funcionan

Estado: ⏳ PENDIENTE
```

#### **Test 5.4: Vista Resumen por Estado**
```
Pasos:
1. Seleccionar "📊 Resumen por Estado"
2. Verificar agrupación por estado
3. Verificar indicadores (✅ Con obs. / ⚠️ Sin obs.)

Resultado Esperado:
- Agrupación correcta
- Indicadores precisos
- Preview de observaciones

Estado: ⏳ PENDIENTE
```

#### **Test 5.5: Exportar CSV Completo**
```
Pasos:
1. Clic "⬇️ Descargar CSV Completo"
2. Verificar descarga
3. Abrir archivo en Excel
4. Verificar contenido

Resultado Esperado:
- Archivo descarga
- Formato correcto
- Datos completos

Estado: ⏳ PENDIENTE
```

#### **Test 5.6: Exportar Solo Con Observaciones**
```
Pasos:
1. Clic "⬇️ Solo Con Observaciones"
2. Verificar descarga
3. Verificar que solo incluye informes con observaciones

Resultado Esperado:
- Solo informes con observaciones
- IDs 4 y 5 presentes

Estado: ⏳ PENDIENTE
```

#### **Test 5.7: Exportar Resumen Ejecutivo**
```
Pasos:
1. Clic "⬇️ Resumen Ejecutivo"
2. Verificar descarga
3. Abrir en Excel

Resultado Esperado:
- Resumen por estado
- Columnas: Estado, Cantidad, Con_Observaciones, Prioridad_Alta

Estado: ⏳ PENDIENTE
```

---

### **6. PRUEBAS DE CALENDARIO**

#### **Test 6.1: Vista Diaria**
```
Pasos:
1. Ir a "Calendario"
2. Tab "📅 Ver Agenda"
3. Seleccionar fecha: 24/11/2025
4. Verificar citas del día

Datos Esperados:
- 5 citas el 24/11/2025
- Horas: 8, 9, 10, 11, 13

Estado: ⏳ PENDIENTE
```

#### **Test 6.2: Vista Semanal**
```
Pasos:
1. Seleccionar vista "Semanal"
2. Verificar semana actual
3. Verificar distribución de citas

Resultado Esperado:
- Citas agrupadas por día
- Colores por prioridad
- Información completa

Estado: ⏳ PENDIENTE
```

#### **Test 6.3: Agendar Cita**
```
Pasos:
1. Tab "➕ Agendar Cita"
2. Buscar centro: "DANTE"
3. Verificar filtros (Provincia, Categoría, Cantón)
4. Seleccionar centro
5. Fecha: Mañana
6. Hora: 10:00
7. Prioridad: Alta
8. Nota: "Cita de prueba"
9. Guardar

Resultado Esperado:
- Cita creada
- Aparece en vista diaria
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 6.4: Búsqueda Avanzada**
```
Pasos:
1. En "Agendar Cita"
2. Buscar por código
3. Buscar por provincia
4. Buscar por cantón
5. Buscar por categoría

Resultado Esperado:
- Búsqueda funciona en todos los campos
- Contador actualizado
- Resultados correctos

Estado: ⏳ PENDIENTE
```

#### **Test 6.5: Editar Cita**
```
Pasos:
1. Seleccionar cita existente
2. Editar detalles
3. Guardar cambios

Resultado Esperado:
- Cambios guardados
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 6.6: Eliminar Cita**
```
Pasos:
1. Seleccionar cita
2. Eliminar
3. Confirmar

Resultado Esperado:
- Cita eliminada
- Desaparece de vista
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 6.7: Generador Automático**
```
Pasos:
1. Tab "🤖 Generador Automático"
2. Configurar parámetros
3. Generar agenda

Resultado Esperado:
- Citas generadas automáticamente
- Sin conflictos de horario
- Distribución óptima

Estado: ⏳ PENDIENTE
```

---

### **7. PRUEBAS DE BASE DE DATOS**

#### **Test 7.1: Ver Centros Educativos**
```
Pasos:
1. Ir a "Base de Datos"
2. Tab "📋 Centros Educativos"
3. Verificar tabla de centros

Resultado Esperado:
- Lista completa de centros
- Búsqueda funciona
- Filtros funcionan

Estado: ⏳ PENDIENTE
```

#### **Test 7.2: Agregar Centro Manual**
```
Pasos:
1. Tab "➕ Agregar Centros"
2. "📝 Manual (Individual)"
3. Nombre: "Centro de Prueba"
4. Provincia: SAN JOSE
5. Cantón: Escazú
6. Código: 999
7. Categoría: 1
8. Guardar

Resultado Esperado:
- Centro agregado
- Aparece en lista
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 7.3: Importar CSV**
```
Pasos:
1. "📄 Importar CSV (Masivo)"
2. Subir ejemplo_centros.csv
3. Revisar vista previa
4. Modo: "Agregar a existentes"
5. Importar

Resultado Esperado:
- 14 centros importados
- Sin duplicados
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 7.4: Editar Centro**
```
Pasos:
1. Buscar centro
2. Seleccionar en "Editar o Eliminar"
3. Expandir "Ver/Editar Detalles"
4. Modificar datos
5. Guardar

Resultado Esperado:
- Cambios guardados
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 7.5: Eliminar Centro**
```
Pasos:
1. Seleccionar centro de prueba
2. Eliminar

Resultado Esperado:
- Centro eliminado
- CSV actualizado

Estado: ⏳ PENDIENTE
```

#### **Test 7.6: Exportar Centros**
```
Pasos:
1. Aplicar filtros
2. Descargar filtrados
3. Descargar todos

Resultado Esperado:
- Archivos descargados
- Datos correctos

Estado: ⏳ PENDIENTE
```

---

### **8. PRUEBAS DE PERSISTENCIA DE DATOS**

#### **Test 8.1: Guardado Automático** ⭐ CRÍTICO
```
Pasos:
1. Crear nuevo informe en Kanban
2. Agregar observaciones
3. Verificar sidebar: "✅ Datos verificados hace Xs"
4. Cerrar navegador (NO la terminal)
5. Reabrir http://localhost:8501
6. Verificar que el informe existe

Resultado Esperado:
- Datos persisten
- Observaciones intactas
- Sin pérdida de información

Estado: ⏳ PENDIENTE - CRÍTICO
```

#### **Test 8.2: Suspensión de PC** ⭐ CRÍTICO
```
Pasos:
1. Crear informe con observaciones
2. Verificar guardado
3. Suspender PC (Sleep)
4. Esperar 5 minutos
5. Reactivar PC
6. Verificar que la app sigue corriendo
7. Verificar que los datos existen

Resultado Esperado:
- App se reactiva
- Datos intactos
- Sin pérdida de información

Estado: ⏳ PENDIENTE - CRÍTICO
```

#### **Test 8.3: Backup y Restauración**
```
Pasos:
1. Ejecutar backup.bat
2. Verificar carpeta backups/
3. Modificar datos
4. Restaurar backup
5. Verificar datos restaurados

Resultado Esperado:
- Backup creado
- Restauración exitosa
- Datos coinciden

Estado: ⏳ PENDIENTE
```

#### **Test 8.4: Verificación de Integridad**
```
Pasos:
1. Eliminar columna 'Observaciones' del CSV
2. Reiniciar app
3. Verificar que se agrega automáticamente

Resultado Esperado:
- Columna agregada automáticamente
- Mensaje de advertencia
- CSV corregido

Estado: ⏳ PENDIENTE
```

---

### **9. PRUEBAS DE RENDIMIENTO**

#### **Test 9.1: Carga con Muchos Datos**
```
Pasos:
1. Importar 100+ centros
2. Crear 50+ informes
3. Agendar 100+ citas
4. Verificar rendimiento

Resultado Esperado:
- App responde en < 3 segundos
- Sin errores de memoria
- Navegación fluida

Estado: ⏳ PENDIENTE
```

#### **Test 9.2: Exportaciones Grandes**
```
Pasos:
1. Exportar CSV con 100+ registros
2. Verificar tiempo de descarga

Resultado Esperado:
- Descarga en < 5 segundos
- Archivo completo

Estado: ⏳ PENDIENTE
```

---

### **10. PRUEBAS DE INTERFAZ**

#### **Test 10.1: Tema Oscuro**
```
Pasos:
1. Verificar que toda la app usa tema oscuro
2. Verificar contraste de colores
3. Verificar legibilidad

Resultado Esperado:
- Tema oscuro consistente
- Colores apropiados
- Texto legible

Estado: ⏳ PENDIENTE
```

#### **Test 10.2: Responsive**
```
Pasos:
1. Redimensionar ventana
2. Verificar que elementos se ajustan

Resultado Esperado:
- Layout se adapta
- Sin elementos cortados

Estado: ⏳ PENDIENTE
```

#### **Test 10.3: Iconos y Emojis**
```
Pasos:
1. Verificar que todos los iconos se muestran
2. Verificar emojis en headers

Resultado Esperado:
- Todos los iconos visibles
- Emojis renderizados

Estado: ⏳ PENDIENTE
```

---

### **11. PRUEBAS DE ERRORES**

#### **Test 11.1: Archivo CSV Corrupto**
```
Pasos:
1. Corromper seguimiento_informes.csv
2. Reiniciar app
3. Verificar manejo de error

Resultado Esperado:
- Backup creado
- Error manejado
- App funcional

Estado: ⏳ PENDIENTE
```

#### **Test 11.2: Archivo Faltante**
```
Pasos:
1. Eliminar calendario.csv
2. Reiniciar app
3. Verificar que se crea nuevo

Resultado Esperado:
- Archivo creado automáticamente
- App funcional

Estado: ⏳ PENDIENTE
```

#### **Test 11.3: Datos Duplicados**
```
Pasos:
1. Crear IDs duplicados en CSV
2. Reiniciar app
3. Verificar corrección automática

Resultado Esperado:
- IDs corregidos
- Mensaje de advertencia
- CSV actualizado

Estado: ⏳ PENDIENTE
```

---

## 📊 Resumen de Pruebas

### **Por Categoría:**

| Categoría | Total Tests | Completados | Pendientes | Críticos |
|-----------|-------------|-------------|------------|----------|
| Archivos | 9 | 9 ✅ | 0 | 0 |
| Inicio | 2 | 0 | 2 ⏳ | 0 |
| Dashboard | 3 | 0 | 3 ⏳ | 0 |
| Kanban | 6 | 0 | 6 ⏳ | 0 |
| Reportes | 7 | 0 | 7 ⏳ | 0 |
| Calendario | 7 | 0 | 7 ⏳ | 0 |
| Base de Datos | 6 | 0 | 6 ⏳ | 0 |
| Persistencia | 4 | 0 | 4 ⏳ | 2 ⭐ |
| Rendimiento | 2 | 0 | 2 ⏳ | 0 |
| Interfaz | 3 | 0 | 3 ⏳ | 0 |
| Errores | 3 | 0 | 3 ⏳ | 0 |
| **TOTAL** | **52** | **9** | **43** | **2** |

---

## 🎯 Prioridad de Pruebas

### **Alta Prioridad (Ejecutar Primero):**
1. ⭐ Test 8.1: Guardado Automático
2. ⭐ Test 8.2: Suspensión de PC
3. Test 4.3: Mover Estados
4. Test 4.4: Editar Informe
5. Test 5.1: Filtros de Reportes

### **Media Prioridad:**
6. Test 6.3: Agendar Cita
7. Test 7.2: Agregar Centro Manual
8. Test 4.2: Crear Nuevo Informe
9. Test 5.5: Exportar CSV

### **Baja Prioridad:**
10. Tests de Interfaz
11. Tests de Rendimiento
12. Tests de Errores

---

## 📝 Instrucciones de Ejecución

### **Preparación:**
```bash
1. Ejecutar backup.bat (crear backup antes de pruebas)
2. Ejecutar INICIAR.bat
3. Abrir este documento
4. Ir marcando tests completados
```

### **Durante las Pruebas:**
```
1. Ejecutar cada test en orden
2. Marcar resultado (✅ PASS / ❌ FAIL)
3. Anotar observaciones
4. Capturar pantallas si hay errores
```

### **Después de las Pruebas:**
```
1. Compilar resultados
2. Reportar bugs encontrados
3. Crear issues para mejoras
4. Actualizar documentación
```

---

## 🐛 Registro de Bugs

| ID | Test | Descripción | Severidad | Estado |
|----|------|-------------|-----------|--------|
| - | - | - | - | - |

---

## ✅ Criterios de Aceptación

Para considerar el sistema APROBADO:

- [ ] 100% de tests críticos PASS
- [ ] 90%+ de tests alta prioridad PASS
- [ ] 80%+ de tests media prioridad PASS
- [ ] Sin bugs de severidad crítica
- [ ] Datos persisten correctamente
- [ ] Todas las exportaciones funcionan
- [ ] Interfaz responsive

---

**Documento creado:** 2025-12-02  
**Última actualización:** 2025-12-02  
**Próxima revisión:** Después de ejecutar pruebas manuales
