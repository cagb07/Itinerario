# 📚 Gestión de Base de Datos de Centros Educativos

## 🎉 Nuevas Funcionalidades Implementadas

### 1. **📋 Gestión Completa de Centros Educativos**

#### **Ver y Buscar Centros**
- **Búsqueda avanzada**: Busca por nombre, código, provincia, cantón o cualquier campo
- **Filtros múltiples**: Provincia + Categoría combinados
- **Contador de resultados**: Muestra cuántos centros coinciden
- **Tabla interactiva**: Visualización completa con scroll

#### **Agregar Centros**

##### **📝 Método Manual (Individual)**
1. Ve a **Base de Datos** → **➕ Agregar Centros**
2. Selecciona **"📝 Manual (Individual)"**
3. Completa el formulario:
   - **Nombre del Centro** * (obligatorio)
   - **Provincia** * (obligatorio)
   - **Cantón**
   - **Código**
   - **Categoría** (1-5)
4. Haz clic en **"➕ Agregar Centro"**

**Validaciones:**
- ✅ No permite nombres duplicados
- ✅ Campos obligatorios marcados con *
- ✅ Provincias predefinidas (evita errores de escritura)

##### **📄 Método CSV (Masivo)**
1. Ve a **Base de Datos** → **➕ Agregar Centros**
2. Selecciona **"📄 Importar CSV (Masivo)"**
3. Prepara tu archivo CSV con las columnas:
   ```
   NOMBRE,PROVINCIA,CANTON,CODIGO,CATALOGO
   Escuela ABC,SAN JOSE,Central,001,1
   Liceo XYZ,ALAJUELA,San Carlos,002,2
   ```
4. Sube el archivo
5. Revisa la vista previa
6. Selecciona el modo:
   - **➕ Agregar a existentes**: Mantiene los centros actuales y agrega los nuevos
   - **🔄 Reemplazar todos**: Borra todo y carga solo los nuevos
7. Haz clic en **"📥 Importar Centros"**

**Características:**
- ✅ Detecta automáticamente codificación (UTF-8 o Latin-1)
- ✅ Normaliza nombres de columnas
- ✅ Elimina duplicados automáticamente
- ✅ Muestra vista previa antes de importar

#### **✏️ Editar Centros**
1. Ve a **Base de Datos** → **📋 Centros Educativos**
2. Usa los filtros para encontrar el centro
3. Selecciona el centro en **"Editar o Eliminar Centro"**
4. Expande **"📝 Ver/Editar Detalles"**
5. Modifica los campos necesarios
6. Haz clic en **"💾 Guardar Cambios"**

#### **🗑️ Eliminar Centros**
1. Sigue los pasos 1-4 de "Editar Centros"
2. Haz clic en **"🗑️ Eliminar Centro"**
3. El centro se eliminará permanentemente

**⚠️ Advertencia**: La eliminación es permanente. Descarga un backup antes si es necesario.

#### **⬇️ Exportar Datos**
- **Descargar Filtrados**: Exporta solo los centros que coinciden con los filtros actuales
- **Descargar Todos**: Exporta la base de datos completa
- Formato: CSV compatible con Excel

---

### 2. **🔍 Búsqueda Mejorada en Calendario**

#### **Búsqueda por Cualquier Criterio**
Al agendar una cita, ahora puedes buscar centros por:
- ✅ **Nombre** del centro
- ✅ **Código** del centro
- ✅ **Provincia**
- ✅ **Cantón**
- ✅ **Categoría**
- ✅ **Cualquier otro campo** en la base de datos

#### **Filtros Combinados**
- **🗺️ Provincia**: Filtra por provincia específica
- **🏷️ Categoría**: Filtra por categoría (1-5)
- **📍 Cantón**: Nuevo filtro por cantón
- **Búsqueda de texto**: Busca en todos los campos simultáneamente

#### **Contador Inteligente**
- Muestra cuántos centros coinciden con los filtros
- Indica el total de centros disponibles
- Se actualiza en tiempo real

**Ejemplo de uso:**
```
Búsqueda: "Juan"
Provincia: SAN JOSE
Categoría: 1

Resultado: 🔍 3 centros encontrados de 150 totales
```

---

## 📊 Estructura de la Base de Datos

### Campos Principales

| Campo | Tipo | Descripción | Obligatorio |
|-------|------|-------------|-------------|
| `NOMBRE` | Texto | Nombre completo del centro | ✅ Sí |
| `PROVINCIA` | Texto | Provincia (7 opciones) | ✅ Sí |
| `CANTON` | Texto | Cantón del centro | ❌ No |
| `CODIGO` | Texto | Código identificador | ❌ No |
| `CATALOGO` | Número | Categoría (1-5) | ❌ No |

### Provincias Válidas
1. SAN JOSE
2. ALAJUELA
3. CARTAGO
4. HEREDIA
5. GUANACASTE
6. PUNTARENAS
7. LIMON

---

## 🚀 Casos de Uso

### **Caso 1: Agregar un Centro Nuevo**
**Situación**: Necesitas agregar "Escuela Nueva Esperanza" en Heredia

**Pasos**:
1. Base de Datos → Agregar Centros
2. Manual (Individual)
3. Completa:
   - Nombre: Escuela Nueva Esperanza
   - Provincia: HEREDIA
   - Cantón: San Rafael
   - Código: 301
   - Categoría: 2
4. Agregar Centro

---

### **Caso 2: Importar 50 Centros desde Excel**
**Situación**: Tienes un Excel con 50 centros nuevos

**Pasos**:
1. Guarda el Excel como CSV
2. Asegúrate de que tenga las columnas: NOMBRE, PROVINCIA, CANTON, CODIGO, CATALOGO
3. Base de Datos → Agregar Centros
4. Importar CSV (Masivo)
5. Sube el archivo
6. Selecciona "Agregar a existentes"
7. Importar Centros

---

### **Caso 3: Buscar Centro por Código al Agendar**
**Situación**: Quieres agendar una cita para el centro con código "205"

**Pasos**:
1. Calendario → Agendar Cita
2. En "Buscar por cualquier criterio" escribe: **205**
3. El sistema buscará en todos los campos
4. Selecciona el centro encontrado
5. Completa la cita

---

### **Caso 4: Actualizar Información de un Centro**
**Situación**: El cantón de "Escuela ABC" cambió de "Central" a "Goicoechea"

**Pasos**:
1. Base de Datos → Centros Educativos
2. Busca "Escuela ABC"
3. Selecciona en "Editar o Eliminar Centro"
4. Expande "Ver/Editar Detalles"
5. Cambia Cantón a "Goicoechea"
6. Guardar Cambios

---

## 🔧 Mantenimiento de la Base de Datos

### **Backup Regular**
1. Ve a **Base de Datos** → **Centros Educativos**
2. Haz clic en **"⬇️ Descargar Todos (CSV)"**
3. Guarda el archivo con fecha: `centros_backup_2025-11-24.csv`

### **Limpieza de Duplicados**
1. Exporta la base de datos completa
2. Abre en Excel
3. Elimina duplicados manualmente
4. Importa con modo **"🔄 Reemplazar todos"**

### **Actualización Masiva**
1. Exporta la base de datos
2. Edita en Excel
3. Guarda como CSV
4. Importa con **"🔄 Reemplazar todos"**

---

## ⚠️ Consideraciones Importantes

### **Formato del CSV**
- **Codificación**: UTF-8 o Latin-1
- **Separador**: Coma (,)
- **Primera fila**: Encabezados (NOMBRE, PROVINCIA, etc.)
- **Sin comillas** en los valores (a menos que contengan comas)

### **Nombres de Columnas**
El sistema normaliza automáticamente:
- Convierte a mayúsculas
- Elimina espacios extra
- Acepta variaciones (ej: "Nombre Centro" → "NOMBRE")

### **Duplicados**
- Al importar con "Agregar a existentes", se eliminan duplicados por NOMBRE
- Se mantiene el primer registro encontrado

### **Validaciones**
- El nombre del centro es obligatorio
- No se permiten nombres duplicados
- La provincia debe ser una de las 7 válidas (en modo manual)

---

## 📝 Plantilla CSV

Copia este contenido en un archivo `.csv`:

```csv
NOMBRE,PROVINCIA,CANTON,CODIGO,CATALOGO
Escuela Ejemplo 1,SAN JOSE,Central,001,1
Liceo Ejemplo 2,ALAJUELA,San Carlos,002,2
Colegio Ejemplo 3,CARTAGO,La Unión,003,1
```

---

## 🐛 Solución de Problemas

### **Error al importar CSV**
- **Problema**: "Error al leer el archivo"
- **Solución**: Verifica que el archivo sea CSV válido y tenga las columnas correctas

### **No se ven los centros nuevos**
- **Problema**: Agregaste centros pero no aparecen
- **Solución**: Haz clic en **"🔄 Recargar Datos"**

### **Búsqueda no encuentra el centro**
- **Problema**: Sabes que existe pero no aparece
- **Solución**: 
  1. Limpia todos los filtros
  2. Busca solo por una palabra clave
  3. Verifica que el centro exista en la base de datos

### **Centro duplicado**
- **Problema**: Agregaste un centro que ya existía
- **Solución**: Elimina el duplicado desde "Editar o Eliminar Centro"

---

## 💡 Tips y Mejores Prácticas

1. **Haz backups regulares** antes de importaciones masivas
2. **Usa códigos únicos** para cada centro
3. **Mantén consistencia** en nombres de provincias y cantones
4. **Revisa la vista previa** antes de importar CSV
5. **Usa filtros combinados** para búsquedas más precisas
6. **Documenta cambios importantes** en un archivo externo

---

**Desarrollado con ❤️ para facilitar la gestión de centros educativos**
