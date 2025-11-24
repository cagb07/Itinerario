import streamlit as st
import pandas as pd
import datetime
import os
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Control de Informes",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS OPTIMIZADOS PARA TEMA OSCURO ---
st.markdown("""
    <style>
    /* Métricas mejoradas */
    [data-testid="stMetricLabel"] {
        color: #9ca3af !important;
        font-weight: 600;
        font-size: 0.95rem;
    }
    [data-testid="stMetricValue"] {
        color: #3b82f6 !important;
        font-weight: 700;
    }
    
    /* Tarjetas Kanban optimizadas para oscuro */
    .kanban-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border: 1px solid #475569;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .kanban-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    }
    .kanban-header {
        font-weight: 700;
        font-size: 1.1em;
        margin-bottom: 8px;
        color: #f1f5f9;
    }
    .kanban-meta {
        font-size: 0.85em;
        color: #94a3b8;
        line-height: 1.6;
    }
    
    /* Botones mejorados */
    .stButton button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
    
    /* Expanders con mejor contraste */
    .streamlit-expanderHeader {
        background-color: #1e293b;
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Inputs mejorados */
    .stTextInput input, .stSelectbox select, .stDateInput input {
        background-color: #1e293b !important;
        border: 1px solid #475569 !important;
        border-radius: 8px !important;
        color: #f1f5f9 !important;
    }
    
    /* Tabs con mejor diseño */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 12px 24px;
        font-weight: 600;
    }
    
    /* Dataframes mejorados */
    .dataframe {
        border-radius: 8px;
        overflow: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONSTANTES ---
ARCHIVO_DATOS = "LISTADO-CON-FASES.csv"
ARCHIVO_SEGUIMIENTO = "seguimiento_informes.csv"
ARCHIVO_CALENDARIO = "calendario.csv"

# --- FUNCIONES ---

@st.cache_data
def cargar_datos_maestros():
    """Carga el listado maestro de centros."""
    if not os.path.exists(ARCHIVO_DATOS):
        return pd.DataFrame()
    try:
        df = pd.read_csv(ARCHIVO_DATOS, header=1, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(ARCHIVO_DATOS, header=1, encoding='latin-1')
        except:
            return pd.DataFrame()
            
    # Normalizar columnas
    df.columns = [str(c).strip().upper() for c in df.columns]
    
    # Mapeo de columnas clave
    mapa = {}
    for col in df.columns:
        if "NOMBRE" in col: mapa[col] = "NOMBRE"
        elif "PROVINCIA" in col: mapa[col] = "PROVINCIA"
        elif "CODIGO" in col: mapa[col] = "CODIGO"
        elif "CATALOGO" in col: mapa[col] = "CATALOGO"
        elif "CANTON" in col: mapa[col] = "CANTON"
    
    df.rename(columns=mapa, inplace=True)
    return df

def cargar_seguimiento():
    """Carga el estado de los informes (Kanban)."""
    if os.path.exists(ARCHIVO_SEGUIMIENTO):
        return pd.read_csv(ARCHIVO_SEGUIMIENTO)
    return pd.DataFrame(columns=["ID", "Centro", "Estado", "Fecha_Inicio", "Fecha_Fin", "Responsable", "Prioridad"])

def guardar_seguimiento(df):
    df.to_csv(ARCHIVO_SEGUIMIENTO, index=False)

# --- CARGA DE DATOS ---
df_centros = cargar_datos_maestros()
df_seguimiento = cargar_seguimiento()

# --- INTERFAZ ---

with st.sidebar:
    st.title("📝 Control Informes")
    menu = st.radio("Menú", ["Dashboard de Control", "Kanban de Informes", "Calendario", "Base de Datos"], index=0)
    st.divider()
    st.info(f"📅 Hoy: {datetime.date.today().strftime('%d/%m/%Y')}")

if df_centros.empty:
    st.error("⚠️ No se encuentra el archivo maestro de centros (LISTADO-CON-FASES.csv).")
else:
    
    # --- DASHBOARD: CONTROL DE AVANCE ---
    if menu == "Dashboard de Control":
        st.title("📊 Control de Realización de Informes")
        st.markdown("Monitoreo del avance en la generación de informes por centro educativo.")
        
        # --- SECCIÓN 1: COBERTURA GLOBAL (Datos Maestros vs Realizados) ---
        st.subheader("🌍 Cobertura Global")
        
        # Lógica de métricas globales
        total_centros = len(df_centros)
        
        # Contamos como "Atendidos" los que están TERMINADOS en el seguimiento
        if not df_seguimiento.empty:
            terminados_global = df_seguimiento[df_seguimiento['Estado'] == 'Terminado']
            centros_atendidos = terminados_global['Centro'].nunique()
        else:
            centros_atendidos = 0
            
        centros_pendientes = total_centros - centros_atendidos
        cobertura = centros_atendidos / total_centros if total_centros > 0 else 0

        # Tarjetas Globales
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Centros", total_centros, help="Total de centros en la base de datos maestra")
        m2.metric("Centros Atendidos", centros_atendidos, delta_color="normal", help="Centros con informe TERMINADO")
        m3.metric("Centros Pendientes", centros_pendientes, delta_color="inverse", help="Centros sin informe terminado")
        m4.metric("Cobertura", f"{cobertura:.1%}", help="% del total de centros cubiertos")
        
        st.progress(cobertura)
        
        st.divider()

        # --- SECCIÓN 2: ESTADO DEL FLUJO DE TRABAJO (Kanban) ---
        st.subheader("🚀 Flujo de Trabajo Actual")
        
        # Métricas del Kanban
        total_seguimiento = len(df_seguimiento)
        en_proceso = len(df_seguimiento[df_seguimiento['Estado'] == 'En Proceso'])
        pendientes_kanban = len(df_seguimiento[df_seguimiento['Estado'] == 'Pendiente'])
        terminados_kanban = len(df_seguimiento[df_seguimiento['Estado'] == 'Terminado'])
        
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("En Cola (Pendientes)", pendientes_kanban, help="Informes creados pero no iniciados")
        k2.metric("⚡ En Proceso", en_proceso, delta_color="off", help="Informes que se están trabajando actualmente")
        k3.metric("✅ Terminados", terminados_kanban, help="Total histórico de terminados")
        k4.metric("Total Gestionados", total_seguimiento, help="Suma de todos los estados")
        
        st.divider()
        
        # Gráficos
        c1, c2 = st.columns([2, 1])
        
        with c1:
            st.subheader("📈 Actividad Reciente")
            if not df_seguimiento.empty:
                # Convertir fechas
                df_view = df_seguimiento.copy()
                df_view['Fecha_Inicio'] = pd.to_datetime(df_view['Fecha_Inicio'])
                
                # Agrupar por fecha de inicio
                por_fecha = df_view['Fecha_Inicio'].dt.date.value_counts().sort_index()
                st.line_chart(por_fecha)
            else:
                st.info("No hay actividad registrada aún.")
                
        with c2:
            st.subheader("📊 Estado Actual")
            if not df_seguimiento.empty:
                st.bar_chart(df_seguimiento['Estado'].value_counts())
            else:
                st.caption("Sin datos.")

    # --- KANBAN DE INFORMES ---
    elif menu == "Kanban de Informes":
        st.title("📋 Tablero Kanban de Seguimiento")
        st.markdown("Visualiza y gestiona el estado de los informes en tiempo real.")
        
        # Botón para iniciar nuevo informe (Agregar al Kanban)
        with st.expander("➕ Iniciar Nuevo Informe (Agregar al Tablero)", expanded=False):
            # Campo de búsqueda fuera del formulario
            lista_centros = sorted(df_centros['NOMBRE'].unique().tolist()) if 'NOMBRE' in df_centros.columns else []
            busqueda = st.text_input("🔍 Buscar Centro Educativo", placeholder="Escribe para filtrar...", key="buscar_centro")
            
            # Filtrar centros según la búsqueda
            if busqueda:
                centros_filtrados = [c for c in lista_centros if busqueda.upper() in c.upper()]
            else:
                centros_filtrados = lista_centros
            
            st.caption(f"Mostrando {len(centros_filtrados)} de {len(lista_centros)} centros")
            
            with st.form("form_nuevo_seguimiento"):
                centro_kanban = st.selectbox("Seleccionar Centro", centros_filtrados if centros_filtrados else ["No hay coincidencias"])
                resp_kanban = st.text_input("Responsable", value="Jeremy Fernández")
                prio_kanban = st.select_slider("Prioridad", ["Baja", "Media", "Alta"], value="Media")
                
                if st.form_submit_button("🚀 Iniciar Informe"):
                    if centro_kanban == "No hay coincidencias":
                        st.error("Por favor selecciona un centro válido")
                    else:
                        nuevo_id = len(df_seguimiento) + 1
                        nuevo_item = {
                            "ID": nuevo_id,
                            "Centro": centro_kanban,
                            "Estado": "Pendiente",
                            "Fecha_Inicio": datetime.date.today(),
                            "Fecha_Fin": None,
                            "Responsable": resp_kanban,
                            "Prioridad": prio_kanban
                        }
                        df_seguimiento = pd.concat([df_seguimiento, pd.DataFrame([nuevo_item])], ignore_index=True)
                        guardar_seguimiento(df_seguimiento)
                        st.success(f"Informe para {centro_kanban} agregado al tablero.")
                        st.rerun()

        # Columnas del Kanban
        col_pend, col_proc, col_fin = st.columns(3)
        
        # Estilos de cabecera
        col_pend.markdown("<h3 style='text-align: center; color: #dc3545;'>🔴 Pendiente</h3>", unsafe_allow_html=True)
        col_proc.markdown("<h3 style='text-align: center; color: #ffc107;'>🟡 En Proceso</h3>", unsafe_allow_html=True)
        col_fin.markdown("<h3 style='text-align: center; color: #28a745;'>🟢 Terminado</h3>", unsafe_allow_html=True)
        
        # Filtrar datos
        df_pend = df_seguimiento[df_seguimiento['Estado'] == 'Pendiente']
        df_proc = df_seguimiento[df_seguimiento['Estado'] == 'En Proceso']
        df_fin = df_seguimiento[df_seguimiento['Estado'] == 'Terminado']
        
        # Función para renderizar tarjeta
        def render_card(row, col_obj, current_status):
            with col_obj:
                with st.container():
                    st.markdown(f"""
                    <div class="kanban-card" style="border-left-color: {'#dc3545' if current_status=='Pendiente' else '#ffc107' if current_status=='En Proceso' else '#28a745'};">
                        <div class="kanban-header">{row['Centro']}</div>
                        <div class="kanban-meta">👤 {row['Responsable']} | 📅 Inicio: {row['Fecha_Inicio']}</div>
                        <div class="kanban-meta">⚡ Prioridad: {row['Prioridad']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Controles de movimiento
                    c1, c2 = st.columns(2)
                    if current_status == 'Pendiente':
                        if c2.button("➡️ Iniciar", key=f"start_{row['ID']}"):
                            df_seguimiento.loc[df_seguimiento['ID'] == row['ID'], 'Estado'] = 'En Proceso'
                            guardar_seguimiento(df_seguimiento)
                            st.rerun()
                    elif current_status == 'En Proceso':
                        if c1.button("⬅️ Pausar", key=f"pause_{row['ID']}"):
                            df_seguimiento.loc[df_seguimiento['ID'] == row['ID'], 'Estado'] = 'Pendiente'
                            guardar_seguimiento(df_seguimiento)
                            st.rerun()
                        if c2.button("✅ Terminar", key=f"finish_{row['ID']}"):
                            df_seguimiento.loc[df_seguimiento['ID'] == row['ID'], 'Estado'] = 'Terminado'
                            df_seguimiento.loc[df_seguimiento['ID'] == row['ID'], 'Fecha_Fin'] = datetime.date.today()
                            guardar_seguimiento(df_seguimiento)
                            st.rerun()
                    elif current_status == 'Terminado':
                        if c1.button("↩️ Reabrir", key=f"reopen_{row['ID']}"):
                            df_seguimiento.loc[df_seguimiento['ID'] == row['ID'], 'Estado'] = 'En Proceso'
                            guardar_seguimiento(df_seguimiento)
                            st.rerun()

        # Renderizar columnas
        for _, row in df_pend.iterrows():
            render_card(row, col_pend, 'Pendiente')
            
        for _, row in df_proc.iterrows():
            render_card(row, col_proc, 'En Proceso')
            
        for _, row in df_fin.iterrows():
            render_card(row, col_fin, 'Terminado')

    # --- CALENDARIO: PLANIFICACIÓN DE INFORMES (MÓDULO MEJORADO) ---
    elif menu == "Calendario":
        from calendario_module import render_calendario
        render_calendario(df_centros, df_seguimiento, ARCHIVO_CALENDARIO)

    # --- BASE DE DATOS ---
    elif menu == "Base de Datos":
        st.title("📂 Gestión de Base de Datos")
        
        tab1, tab2, tab3 = st.tabs(["📋 Centros Educativos", "📊 Seguimiento (Kanban)", "➕ Agregar Centros"])
        
        # ========== TAB 1: CENTROS EDUCATIVOS ==========
        with tab1:
            st.subheader("Listado de Centros Educativos")
            
            if df_centros.empty:
                st.warning("⚠️ No hay centros educativos en la base de datos")
            else:
                # Búsqueda y filtros
                col_search1, col_search2, col_search3 = st.columns([2, 1, 1])
                
                with col_search1:
                    busqueda_bd = st.text_input("🔍 Buscar centro", placeholder="Nombre, código, provincia, cantón...", key="buscar_bd")
                
                with col_search2:
                    if 'PROVINCIA' in df_centros.columns:
                        provincias_bd = ["Todas"] + sorted(df_centros['PROVINCIA'].dropna().unique().tolist())
                        filtro_prov_bd = st.selectbox("Provincia", provincias_bd, key="prov_bd")
                    else:
                        filtro_prov_bd = "Todas"
                
                with col_search3:
                    if 'CATALOGO' in df_centros.columns:
                        cats_bd = ["Todas"] + sorted(df_centros['CATALOGO'].dropna().astype(str).unique().tolist())
                        filtro_cat_bd = st.selectbox("Categoría", cats_bd, key="cat_bd")
                    else:
                        filtro_cat_bd = "Todas"
                
                # Aplicar filtros
                df_filtrado_bd = df_centros.copy()
                
                if busqueda_bd:
                    mask = df_filtrado_bd.apply(lambda row: busqueda_bd.upper() in str(row).upper(), axis=1)
                    df_filtrado_bd = df_filtrado_bd[mask]
                
                if filtro_prov_bd != "Todas":
                    df_filtrado_bd = df_filtrado_bd[df_filtrado_bd['PROVINCIA'] == filtro_prov_bd]
                
                if filtro_cat_bd != "Todas" and 'CATALOGO' in df_centros.columns:
                    df_filtrado_bd = df_filtrado_bd[df_filtrado_bd['CATALOGO'].astype(str) == filtro_cat_bd]
                
                st.caption(f"📊 Mostrando {len(df_filtrado_bd)} de {len(df_centros)} centros")
                
                # Mostrar tabla
                st.dataframe(df_filtrado_bd, use_container_width=True, height=400)
                
                # Botones de acción
                col_btn1, col_btn2, col_btn3 = st.columns(3)
                
                with col_btn1:
                    csv_centros = df_filtrado_bd.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "⬇️ Descargar Filtrados (CSV)",
                        csv_centros,
                        f"centros_filtrados_{datetime.date.today()}.csv",
                        "text/csv",
                        use_container_width=True
                    )
                
                with col_btn2:
                    csv_todos = df_centros.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "⬇️ Descargar Todos (CSV)",
                        csv_todos,
                        f"centros_completo_{datetime.date.today()}.csv",
                        "text/csv",
                        use_container_width=True
                    )
                
                with col_btn3:
                    if st.button("🔄 Recargar Datos", use_container_width=True):
                        st.cache_data.clear()
                        st.rerun()
                
                # Editar/Eliminar centros
                st.divider()
                st.subheader("✏️ Editar o Eliminar Centro")
                
                if not df_filtrado_bd.empty:
                    centro_editar = st.selectbox(
                        "Seleccionar centro para editar/eliminar",
                        df_filtrado_bd['NOMBRE'].tolist() if 'NOMBRE' in df_filtrado_bd.columns else [],
                        key="centro_editar"
                    )
                    
                    if centro_editar:
                        centro_data = df_centros[df_centros['NOMBRE'] == centro_editar].iloc[0]
                        
                        with st.expander("📝 Ver/Editar Detalles", expanded=False):
                            with st.form("form_editar_centro"):
                                col_e1, col_e2 = st.columns(2)
                                
                                with col_e1:
                                    nombre_edit = st.text_input("Nombre", value=centro_data.get('NOMBRE', ''))
                                    provincia_edit = st.text_input("Provincia", value=centro_data.get('PROVINCIA', ''))
                                    canton_edit = st.text_input("Cantón", value=centro_data.get('CANTON', ''))
                                
                                with col_e2:
                                    codigo_edit = st.text_input("Código", value=centro_data.get('CODIGO', ''))
                                    catalogo_edit = st.text_input("Categoría", value=centro_data.get('CATALOGO', ''))
                                
                                col_btn_e1, col_btn_e2 = st.columns(2)
                                
                                with col_btn_e1:
                                    if st.form_submit_button("💾 Guardar Cambios", type="primary", use_container_width=True):
                                        # Actualizar datos
                                        idx = df_centros[df_centros['NOMBRE'] == centro_editar].index[0]
                                        df_centros.loc[idx, 'NOMBRE'] = nombre_edit
                                        df_centros.loc[idx, 'PROVINCIA'] = provincia_edit
                                        df_centros.loc[idx, 'CANTON'] = canton_edit
                                        df_centros.loc[idx, 'CODIGO'] = codigo_edit
                                        df_centros.loc[idx, 'CATALOGO'] = catalogo_edit
                                        
                                        # Guardar
                                        df_centros.to_csv(ARCHIVO_DATOS, index=False)
                                        st.success("✅ Centro actualizado")
                                        st.cache_data.clear()
                                        time.sleep(1)
                                        st.rerun()
                                
                                with col_btn_e2:
                                    if st.form_submit_button("🗑️ Eliminar Centro", use_container_width=True):
                                        # Eliminar
                                        df_centros_new = df_centros[df_centros['NOMBRE'] != centro_editar]
                                        df_centros_new.to_csv(ARCHIVO_DATOS, index=False)
                                        st.success("🗑️ Centro eliminado")
                                        st.cache_data.clear()
                                        time.sleep(1)
                                        st.rerun()
        
        # ========== TAB 2: SEGUIMIENTO KANBAN ==========
        with tab2:
            st.subheader("Historial de Seguimiento")
            
            if not df_seguimiento.empty:
                st.dataframe(df_seguimiento, use_container_width=True, height=400)
                csv = df_seguimiento.to_csv(index=False).encode('utf-8')
                st.download_button("⬇️ Descargar Seguimiento", csv, "seguimiento_informes.csv", "text/csv")
            else:
                st.info("📭 No hay datos de seguimiento.")
        
        # ========== TAB 3: AGREGAR CENTROS ==========
        with tab3:
            st.subheader("➕ Agregar Nuevos Centros Educativos")
            
            metodo = st.radio("Método de ingreso", ["📝 Manual (Individual)", "📄 Importar CSV (Masivo)"], horizontal=True)
            
            if metodo == "📝 Manual (Individual)":
                st.markdown("### Agregar Centro Manualmente")
                
                with st.form("form_agregar_centro"):
                    col_a1, col_a2 = st.columns(2)
                    
                    with col_a1:
                        nombre_nuevo = st.text_input("Nombre del Centro *", placeholder="Ej: Escuela Juan Mora Fernández")
                        provincia_nuevo = st.selectbox("Provincia *", [
                            "SAN JOSE", "ALAJUELA", "CARTAGO", "HEREDIA", "GUANACASTE", 
                            "PUNTARENAS", "LIMON"
                        ])
                        canton_nuevo = st.text_input("Cantón", placeholder="Ej: Central")
                    
                    with col_a2:
                        codigo_nuevo = st.text_input("Código", placeholder="Ej: 001")
                        catalogo_nuevo = st.selectbox("Categoría", ["1", "2", "3", "4", "5"])
                    
                    st.caption("* Campos obligatorios")
                    
                    if st.form_submit_button("➕ Agregar Centro", type="primary", use_container_width=True):
                        if not nombre_nuevo:
                            st.error("❌ El nombre del centro es obligatorio")
                        else:
                            # Verificar duplicados
                            if not df_centros.empty and nombre_nuevo in df_centros['NOMBRE'].values:
                                st.error("❌ Ya existe un centro con ese nombre")
                            else:
                                # Crear nuevo centro
                                nuevo_centro = {
                                    'NOMBRE': nombre_nuevo,
                                    'PROVINCIA': provincia_nuevo,
                                    'CANTON': canton_nuevo,
                                    'CODIGO': codigo_nuevo,
                                    'CATALOGO': catalogo_nuevo
                                }
                                
                                # Agregar al DataFrame
                                if df_centros.empty:
                                    df_centros_new = pd.DataFrame([nuevo_centro])
                                else:
                                    df_centros_new = pd.concat([df_centros, pd.DataFrame([nuevo_centro])], ignore_index=True)
                                
                                # Guardar
                                df_centros_new.to_csv(ARCHIVO_DATOS, index=False)
                                st.success(f"✅ Centro '{nombre_nuevo}' agregado exitosamente")
                                st.cache_data.clear()
                                time.sleep(1.5)
                                st.rerun()
            
            else:  # Importar CSV
                st.markdown("### Importar Centros desde CSV")
                
                st.info("""
                📋 **Formato del CSV:**
                - El archivo debe tener las columnas: `NOMBRE`, `PROVINCIA`, `CANTON`, `CODIGO`, `CATALOGO`
                - La primera fila debe contener los encabezados
                - Codificación: UTF-8 o Latin-1
                """)
                
                archivo_csv = st.file_uploader("Seleccionar archivo CSV", type=['csv'], key="upload_csv")
                
                if archivo_csv is not None:
                    try:
                        # Intentar leer el CSV
                        df_importar = pd.read_csv(archivo_csv, encoding='utf-8')
                    except:
                        try:
                            df_importar = pd.read_csv(archivo_csv, encoding='latin-1')
                        except Exception as e:
                            st.error(f"❌ Error al leer el archivo: {e}")
                            df_importar = None
                    
                    if df_importar is not None:
                        # Normalizar columnas
                        df_importar.columns = [str(c).strip().upper() for c in df_importar.columns]
                        
                        st.success(f"✅ Archivo leído: {len(df_importar)} centros encontrados")
                        
                        # Vista previa
                        st.markdown("**Vista Previa:**")
                        st.dataframe(df_importar.head(10), use_container_width=True)
                        
                        col_imp1, col_imp2 = st.columns(2)
                        
                        with col_imp1:
                            modo_importacion = st.radio(
                                "Modo de importación",
                                ["➕ Agregar a existentes", "🔄 Reemplazar todos"],
                                help="Agregar: mantiene los centros actuales. Reemplazar: borra todo y carga solo los nuevos."
                            )
                        
                        with col_imp2:
                            if st.button("📥 Importar Centros", type="primary", use_container_width=True):
                                if modo_importacion == "➕ Agregar a existentes":
                                    if df_centros.empty:
                                        df_final = df_importar
                                    else:
                                        df_final = pd.concat([df_centros, df_importar], ignore_index=True)
                                    
                                    # Eliminar duplicados por nombre
                                    df_final = df_final.drop_duplicates(subset=['NOMBRE'], keep='first')
                                else:
                                    df_final = df_importar
                                
                                # Guardar
                                df_final.to_csv(ARCHIVO_DATOS, index=False)
                                st.success(f"✅ {len(df_importar)} centros importados. Total en BD: {len(df_final)}")
                                st.cache_data.clear()
                                time.sleep(2)
                                st.rerun()

