import streamlit as st
import pandas as pd
import datetime
import os
import time

def render_calendario(df_centros, df_seguimiento, ARCHIVO_CALENDARIO):
    """Módulo completo del sistema de calendario mejorado"""
    
    def cargar_calendario():
        if os.path.exists(ARCHIVO_CALENDARIO):
            return pd.read_csv(ARCHIVO_CALENDARIO)
        return pd.DataFrame()
    
    def guardar_registro(ruta, datos):
        df_new = pd.DataFrame([datos])
        if not os.path.exists(ruta):
            df_new.to_csv(ruta, index=False)
        else:
            df_new.to_csv(ruta, mode='a', header=False, index=False)
    
    st.title("📅 Sistema de Planificación de Informes")
    
    # Cargar calendario
    df_cal = cargar_calendario()
    if not df_cal.empty:
        df_cal['Fecha'] = pd.to_datetime(df_cal['Fecha']).dt.date
        df_cal['ID_Cita'] = df_cal.index if 'ID_Cita' not in df_cal.columns else df_cal['ID_Cita']
    
    # --- ESTADÍSTICAS GENERALES ---
    st.subheader("📊 Resumen de Agenda")
    col_stat1, col_stat2, col_stat3, col_stat4, col_stat5 = st.columns(5)
    
    total_citas = len(df_cal)
    citas_pendientes = len(df_cal[df_cal['Estado'] == 'Pendiente']) if not df_cal.empty else 0
    citas_confirmadas = len(df_cal[df_cal['Estado'] == 'Confirmada']) if not df_cal.empty else 0
    citas_completadas = len(df_cal[df_cal['Estado'] == 'Completada']) if not df_cal.empty else 0
    citas_hoy = len(df_cal[df_cal['Fecha'] == datetime.date.today()]) if not df_cal.empty else 0
    
    col_stat1.metric("Total Citas", total_citas)
    col_stat2.metric("⏳ Pendientes", citas_pendientes)
    col_stat3.metric("✅ Confirmadas", citas_confirmadas)
    col_stat4.metric("🎯 Completadas", citas_completadas)
    col_stat5.metric("📅 Hoy", citas_hoy, delta_color="off")
    
    st.divider()
    
    # --- TABS PRINCIPALES ---
    tab_ver, tab_agendar, tab_gestionar, tab_auto = st.tabs([
        "👀 Ver Agenda", 
        "➕ Agendar Cita", 
        "⚙️ Gestionar Citas",
        "🤖 Generador Automático"
    ])
    
    # ========== PESTAÑA 1: VER AGENDA ==========
    with tab_ver:
        st.subheader("Visualización de Agenda")
        
        # Selector de vista
        vista_tipo = st.radio("Tipo de Vista", ["📅 Diaria", "📆 Semanal"], horizontal=True)
        
        # --- VISTA DIARIA ---
        if vista_tipo == "📅 Diaria":
            fecha_ver = st.date_input("Seleccionar Fecha", datetime.date.today(), key="fecha_diaria")
            
            st.markdown(f"### Itinerario del {fecha_ver.strftime('%d/%m/%Y')}")
            
            agenda_dia = {h: None for h in range(8, 17)}
            
            if not df_cal.empty:
                citas_dia = df_cal[df_cal['Fecha'] == fecha_ver]
                for _, row in citas_dia.iterrows():
                    h = int(row['Hora'])
                    if h in agenda_dia:
                        agenda_dia[h] = row
            
            for h in range(8, 17):
                hora_fmt = f"{h:02d}:00"
                if h == 12:
                    st.info(f"🍽️ **{hora_fmt} - 13:00** | ALMUERZO")
                    continue
                
                cita = agenda_dia[h]
                if cita is not None:
                    color_map = {"Alta": "#ef4444", "Media": "#f59e0b", "Baja": "#3b82f6"}
                    estado_map = {"Pendiente": "⏳", "Confirmada": "✅", "Completada": "🎯", "Cancelada": "❌"}
                    color = color_map.get(cita['Prioridad'], "#3b82f6")
                    icono_estado = estado_map.get(cita['Estado'], "📝")
                    
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
                                padding: 16px; border-radius: 12px; 
                                border-left: 5px solid {color}; margin-bottom: 12px;
                                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <strong style="font-size: 1.1em; color: #60a5fa;">📝 {hora_fmt}</strong> - 
                                <span style="font-size: 1.2em; font-weight: bold; color: #f1f5f9;">{cita['Centro']}</span>
                            </div>
                            <span style="font-size: 1.3em;">{icono_estado}</span>
                        </div>
                        <div style="margin-top: 8px; color: #94a3b8; font-size: 0.9em;">
                            📍 {cita['Provincia']} | 🏷️ {cita['Categoria']} | ⚡ {cita['Prioridad']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="padding: 12px; border-bottom: 1px solid #374151; color: #6b7280;">
                        ⏰ {hora_fmt} - <em>Disponible</em>
                    </div>
                    """, unsafe_allow_html=True)
        
        # --- VISTA SEMANAL ---
        else:
            fecha_ref = st.date_input("Semana de referencia", datetime.date.today(), key="fecha_semanal")
            inicio_semana = fecha_ref - datetime.timedelta(days=fecha_ref.weekday())
            dias_semana = [inicio_semana + datetime.timedelta(days=i) for i in range(5)]
            
            st.markdown(f"### Semana del {dias_semana[0].strftime('%d/%m')} al {dias_semana[4].strftime('%d/%m/%Y')}")
            
            cols_semana = st.columns(5)
            
            for idx, dia in enumerate(dias_semana):
                with cols_semana[idx]:
                    dia_nombre = ["Lun", "Mar", "Mié", "Jue", "Vie"][idx]
                    st.markdown(f"**{dia_nombre}** {dia.strftime('%d/%m')}")
                    
                    if not df_cal.empty:
                        citas_dia = df_cal[df_cal['Fecha'] == dia]
                        if not citas_dia.empty:
                            for _, cita in citas_dia.iterrows():
                                hora_fmt = f"{int(cita['Hora']):02d}:00"
                                color_map = {"Alta": "#ef4444", "Media": "#f59e0b", "Baja": "#3b82f6"}
                                color = color_map.get(cita['Prioridad'], "#3b82f6")
                                
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, {color}15 0%, {color}25 100%); 
                                            border-left: 3px solid {color};
                                            color: #f1f5f9; padding: 10px; 
                                            border-radius: 8px; margin-bottom: 6px; font-size: 0.85em;">
                                    <strong style="color: {color};">{hora_fmt}</strong><br>
                                    <span style="color: #e2e8f0;">{cita['Centro'][:25]}...</span>
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.caption("Sin citas")
                    else:
                        st.caption("Sin citas")
    
    # ========== PESTAÑA 2: AGENDAR CITA ==========
    with tab_agendar:
        st.subheader("➕ Programar Nueva Cita")
        
        st.markdown("### 🔍 Búsqueda Avanzada de Centros")
        
        # Búsqueda principal
        busqueda_centro = st.text_input(
            "Buscar por cualquier criterio", 
            placeholder="Nombre, código, provincia, cantón, categoría...", 
            key="buscar_agendar",
            help="Busca en todos los campos del centro educativo"
        )
        
        # Filtros adicionales
        col_f1, col_f2, col_f3 = st.columns(3)
        
        with col_f1:
            provincias = ["Todas"] + sorted(df_centros['PROVINCIA'].dropna().unique().tolist()) if 'PROVINCIA' in df_centros.columns else ["Todas"]
            filtro_prov = st.selectbox("🗺️ Provincia", provincias, key="filtro_prov_agendar")
        
        with col_f2:
            if 'CATALOGO' in df_centros.columns:
                categorias = ["Todas"] + sorted(df_centros['CATALOGO'].dropna().astype(str).unique().tolist())
                filtro_cat = st.selectbox("🏷️ Categoría", categorias, key="filtro_cat_agendar")
            else:
                filtro_cat = "Todas"
        
        with col_f3:
            if 'CANTON' in df_centros.columns:
                cantones = ["Todos"] + sorted(df_centros['CANTON'].dropna().unique().tolist())
                filtro_canton = st.selectbox("📍 Cantón", cantones, key="filtro_canton_agendar")
            else:
                filtro_canton = "Todos"
        
        # Aplicar filtros
        df_filtrado = df_centros.copy()
        
        # Filtro de provincia
        if filtro_prov != "Todas":
            df_filtrado = df_filtrado[df_filtrado['PROVINCIA'] == filtro_prov]
        
        # Filtro de categoría
        if filtro_cat != "Todas" and 'CATALOGO' in df_centros.columns:
            df_filtrado = df_filtrado[df_filtrado['CATALOGO'].astype(str) == filtro_cat]
        
        # Filtro de cantón
        if filtro_canton != "Todos" and 'CANTON' in df_centros.columns:
            df_filtrado = df_filtrado[df_filtrado['CANTON'] == filtro_canton]
        
        # Búsqueda de texto en todos los campos
        if busqueda_centro:
            busqueda_upper = busqueda_centro.upper()
            mask = df_filtrado.apply(
                lambda row: any(busqueda_upper in str(val).upper() for val in row.values if pd.notna(val)),
                axis=1
            )
            df_filtrado = df_filtrado[mask]
        
        lista_centros_final = sorted(df_filtrado['NOMBRE'].unique().tolist()) if 'NOMBRE' in df_filtrado.columns else []
        
        # Mostrar contador con más información
        if busqueda_centro or filtro_prov != "Todas" or filtro_cat != "Todas" or filtro_canton != "Todos":
            st.info(f"🔍 **{len(lista_centros_final)}** centros encontrados de {len(df_centros)} totales")
        else:
            st.caption(f"📋 {len(lista_centros_final)} centros disponibles")
        
        st.divider()
        
        with st.form("form_agendar"):
            col_a1, col_a2 = st.columns(2)
            
            with col_a1:
                centro_sel = st.selectbox("Centro", lista_centros_final if lista_centros_final else ["No hay coincidencias"])
                fecha_visita = st.date_input("Fecha", min_value=datetime.date.today())
            
            with col_a2:
                horas_validas = [8, 9, 10, 11, 13, 14, 15]
                hora_str = [f"{h}:00" for h in horas_validas]
                hora_elegida_str = st.selectbox("Hora", hora_str)
                hora_int = horas_validas[hora_str.index(hora_elegida_str)]
                
                prioridad = st.select_slider("Prioridad", ["Baja", "Media", "Alta"], value="Media")
            
            nota = st.text_area("Notas", placeholder="Objetivos de la visita...")
            crear_kanban = st.checkbox("✅ Crear en Kanban", value=True)
            
            if st.form_submit_button("📅 Agendar", type="primary", use_container_width=True):
                errores = []
                
                if centro_sel == "No hay coincidencias":
                    errores.append("Selecciona un centro válido")
                if fecha_visita.weekday() >= 5:
                    errores.append("No se permiten fines de semana")
                if not df_cal.empty:
                    if not df_cal[(df_cal['Fecha'] == fecha_visita) & (df_cal['Hora'] == hora_int)].empty:
                        errores.append("Horario ocupado")
                
                if errores:
                    for e in errores:
                        st.error(f"❌ {e}")
                else:
                    centro_data = df_centros[df_centros['NOMBRE'] == centro_sel].iloc[0]
                    nueva_cita = {
                        "ID_Cita": len(df_cal) + 1 if not df_cal.empty else 1,
                        "Fecha": fecha_visita,
                        "Hora": hora_int,
                        "Centro": centro_sel,
                        "Provincia": centro_data.get('PROVINCIA', 'N/A'),
                        "Canton": centro_data.get('CANTON', 'N/A'),
                        "Categoria": centro_data.get('CATALOGO', 'N/A'),
                        "Prioridad": prioridad,
                        "Nota": nota,
                        "Estado": "Pendiente",
                        "Fecha_Creacion": datetime.date.today()
                    }
                    
                    guardar_registro(ARCHIVO_CALENDARIO, nueva_cita)
                    
                    if crear_kanban:
                        from app import guardar_seguimiento
                        nuevo_kanban = {
                            "ID": len(df_seguimiento) + 1,
                            "Centro": centro_sel,
                            "Estado": "Pendiente",
                            "Fecha_Inicio": fecha_visita,
                            "Fecha_Fin": None,
                            "Responsable": "Sistema",
                            "Prioridad": prioridad
                        }
                        df_seguimiento_new = pd.concat([df_seguimiento, pd.DataFrame([nuevo_kanban])], ignore_index=True)
                        guardar_seguimiento(df_seguimiento_new)
                    
                    st.success(f"✅ Cita agendada: {centro_sel}")
                    time.sleep(1)
                    st.rerun()
    
    # ========== PESTAÑA 3: GESTIONAR CITAS ==========
    with tab_gestionar:
        st.subheader("⚙️ Administración de Citas")
        
        if df_cal.empty:
            st.info("📭 No hay citas programadas")
        else:
            for idx, cita in df_cal.iterrows():
                with st.expander(f"📅 {cita['Fecha']} {int(cita['Hora']):02d}:00 - {cita['Centro'][:40]}"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.write(f"**Provincia:** {cita['Provincia']}")
                        st.write(f"**Estado:** {cita['Estado']}")
                        st.write(f"**Prioridad:** {cita['Prioridad']}")
                    
                    with col2:
                        nuevo_estado = st.selectbox("Estado", ["Pendiente", "Confirmada", "Completada", "Cancelada"],
                                                    index=["Pendiente", "Confirmada", "Completada", "Cancelada"].index(cita['Estado']),
                                                    key=f"est_{idx}")
                        
                        if st.button("💾 Guardar", key=f"save_{idx}"):
                            df_cal.loc[idx, 'Estado'] = nuevo_estado
                            df_cal.to_csv(ARCHIVO_CALENDARIO, index=False)
                            st.success("✅ Actualizado")
                            time.sleep(0.5)
                            st.rerun()
                        
                        if st.button("🗑️ Eliminar", key=f"del_{idx}"):
                            df_cal = df_cal.drop(idx)
                            df_cal.to_csv(ARCHIVO_CALENDARIO, index=False)
                            st.success("🗑️ Eliminada")
                            time.sleep(0.5)
                            st.rerun()
    
    # ========== PESTAÑA 4: GENERADOR AUTOMÁTICO ==========
    with tab_auto:
        st.subheader("🤖 Generador Inteligente")
        
        with st.form("form_auto"):
            col1, col2 = st.columns(2)
            
            with col1:
                fecha_inicio = st.date_input("Fecha Inicio", datetime.date.today() + datetime.timedelta(days=1))
                max_citas_dia = st.slider("Citas/día", 1, 7, 5)
            
            with col2:
                dias_generar = st.number_input("Días a planificar", 1, 30, 10)
                categorias = st.multiselect("Categorías", ["1", "2", "3"], default=["1", "2"])
            
            if st.form_submit_button("🚀 Generar", type="primary"):
                with st.spinner("Generando..."):
                    df_cand = df_centros.copy()
                    
                    if 'CATALOGO' in df_cand.columns and categorias:
                        df_cand = df_cand[df_cand['CATALOGO'].astype(str).isin(categorias)]
                    
                    centros_ocupados = set()
                    if not df_seguimiento.empty:
                        centros_ocupados.update(df_seguimiento[df_seguimiento['Estado'] == 'Terminado']['Centro'].unique())
                    if not df_cal.empty:
                        centros_ocupados.update(df_cal['Centro'].unique())
                    
                    df_cand = df_cand[~df_cand['NOMBRE'].isin(centros_ocupados)]
                    
                    if df_cand.empty:
                        st.warning("No hay centros disponibles")
                    else:
                        nuevas = []
                        fecha_cursor = fecha_inicio
                        horas = [8, 9, 10, 11, 13, 14, 15]
                        slot_idx = 0
                        dias_count = 0
                        citas_dia = 0
                        
                        for _, centro in df_cand.iterrows():
                            if dias_count >= dias_generar:
                                break
                            
                            while fecha_cursor.weekday() >= 5:
                                fecha_cursor += datetime.timedelta(days=1)
                            
                            if citas_dia >= max_citas_dia:
                                fecha_cursor += datetime.timedelta(days=1)
                                while fecha_cursor.weekday() >= 5:
                                    fecha_cursor += datetime.timedelta(days=1)
                                citas_dia = 0
                                slot_idx = 0
                                dias_count += 1
                            
                            if dias_count >= dias_generar:
                                break
                            
                            nuevas.append({
                                "ID_Cita": len(df_cal) + len(nuevas) + 1,
                                "Fecha": fecha_cursor,
                                "Hora": horas[slot_idx],
                                "Centro": centro['NOMBRE'],
                                "Provincia": centro.get('PROVINCIA', 'N/A'),
                                "Canton": centro.get('CANTON', 'N/A'),
                                "Categoria": centro.get('CATALOGO', 'N/A'),
                                "Prioridad": "Alta",
                                "Nota": "Auto-generado",
                                "Estado": "Pendiente",
                                "Fecha_Creacion": datetime.date.today()
                            })
                            
                            citas_dia += 1
                            slot_idx = (slot_idx + 1) % len(horas)
                        
                        if nuevas:
                            df_nuevas = pd.DataFrame(nuevas)
                            if not os.path.exists(ARCHIVO_CALENDARIO):
                                df_nuevas.to_csv(ARCHIVO_CALENDARIO, index=False)
                            else:
                                df_nuevas.to_csv(ARCHIVO_CALENDARIO, mode='a', header=False, index=False)
                            
                            st.success(f"✅ {len(nuevas)} citas generadas")
                            st.dataframe(df_nuevas[['Fecha', 'Hora', 'Centro', 'Provincia']].head(10))
                            time.sleep(1)
                            st.rerun()
