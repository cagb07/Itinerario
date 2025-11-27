"""
Módulo de Autenticación para Control de Informes
Maneja login, logout y gestión de usuarios
"""

import streamlit as st
import pandas as pd
import hashlib
import os
from datetime import datetime

# Archivo de usuarios
ARCHIVO_USUARIOS = "usuarios.csv"

def hash_password(password):
    """Genera un hash SHA-256 de la contraseña"""
    return hashlib.sha256(password.encode()).hexdigest()

def cargar_usuarios():
    """Carga la base de datos de usuarios"""
    if os.path.exists(ARCHIVO_USUARIOS):
        return pd.read_csv(ARCHIVO_USUARIOS)
    else:
        # Crear archivo inicial con usuario admin por defecto
        df_inicial = pd.DataFrame([{
            'usuario': 'admin',
            'password_hash': hash_password('admin123'),
            'nombre_completo': 'Administrador',
            'rol': 'admin',
            'activo': True,
            'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }])
        df_inicial.to_csv(ARCHIVO_USUARIOS, index=False)
        return df_inicial

def guardar_usuarios(df_usuarios):
    """Guarda la base de datos de usuarios"""
    df_usuarios.to_csv(ARCHIVO_USUARIOS, index=False)

def validar_credenciales(usuario, password):
    """Valida las credenciales del usuario"""
    df_usuarios = cargar_usuarios()
    password_hash = hash_password(password)
    
    usuario_encontrado = df_usuarios[
        (df_usuarios['usuario'] == usuario) & 
        (df_usuarios['password_hash'] == password_hash) &
        (df_usuarios['activo'] == True)
    ]
    
    if not usuario_encontrado.empty:
        return True, usuario_encontrado.iloc[0].to_dict()
    return False, None

def crear_usuario(usuario, password, nombre_completo, rol='usuario'):
    """Crea un nuevo usuario en el sistema"""
    df_usuarios = cargar_usuarios()
    
    # Verificar si el usuario ya existe
    if usuario in df_usuarios['usuario'].values:
        return False, "El usuario ya existe"
    
    # Crear nuevo registro
    nuevo_usuario = {
        'usuario': usuario,
        'password_hash': hash_password(password),
        'nombre_completo': nombre_completo,
        'rol': rol,
        'activo': True,
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    df_usuarios = pd.concat([df_usuarios, pd.DataFrame([nuevo_usuario])], ignore_index=True)
    guardar_usuarios(df_usuarios)
    return True, "Usuario creado exitosamente"

def cambiar_password(usuario, password_actual, password_nueva):
    """Cambia la contraseña de un usuario"""
    df_usuarios = cargar_usuarios()
    
    # Validar contraseña actual
    valido, _ = validar_credenciales(usuario, password_actual)
    if not valido:
        return False, "Contraseña actual incorrecta"
    
    # Actualizar contraseña
    df_usuarios.loc[df_usuarios['usuario'] == usuario, 'password_hash'] = hash_password(password_nueva)
    guardar_usuarios(df_usuarios)
    return True, "Contraseña actualizada exitosamente"

def desactivar_usuario(usuario):
    """Desactiva un usuario (no lo elimina)"""
    df_usuarios = cargar_usuarios()
    df_usuarios.loc[df_usuarios['usuario'] == usuario, 'activo'] = False
    guardar_usuarios(df_usuarios)
    return True, "Usuario desactivado"

def activar_usuario(usuario):
    """Activa un usuario previamente desactivado"""
    df_usuarios = cargar_usuarios()
    df_usuarios.loc[df_usuarios['usuario'] == usuario, 'activo'] = True
    guardar_usuarios(df_usuarios)
    return True, "Usuario activado"

def inicializar_sesion():
    """Inicializa las variables de sesión necesarias"""
    if 'autenticado' not in st.session_state:
        st.session_state.autenticado = False
    if 'usuario' not in st.session_state:
        st.session_state.usuario = None
    if 'datos_usuario' not in st.session_state:
        st.session_state.datos_usuario = None

def logout():
    """Cierra la sesión del usuario"""
    st.session_state.autenticado = False
    st.session_state.usuario = None
    st.session_state.datos_usuario = None

def render_login():
    """Renderiza la pantalla de login"""
    st.markdown("""
        <style>
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 40px;
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("# 🔐 Control de Informes")
        st.markdown("### Iniciar Sesión")
        st.divider()
        
        with st.form("login_form"):
            usuario = st.text_input("👤 Usuario", placeholder="Ingrese su usuario")
            password = st.text_input("🔑 Contraseña", type="password", placeholder="Ingrese su contraseña")
            
            submit = st.form_submit_button("🚀 Ingresar", use_container_width=True, type="primary")
            
            if submit:
                if not usuario or not password:
                    st.error("❌ Por favor complete todos los campos")
                else:
                    valido, datos = validar_credenciales(usuario, password)
                    if valido:
                        st.session_state.autenticado = True
                        st.session_state.usuario = usuario
                        st.session_state.datos_usuario = datos
                        st.success(f"✅ Bienvenido {datos['nombre_completo']}!")
                        st.rerun()
                    else:
                        st.error("❌ Usuario o contraseña incorrectos")
        
        st.divider()
       
def render_gestion_usuarios():
    """Renderiza la interfaz de gestión de usuarios (solo para admin)"""
    if st.session_state.datos_usuario.get('rol') != 'admin':
        st.error("⛔ No tienes permisos para acceder a esta sección")
        return
    
    st.title("👥 Gestión de Usuarios")
    
    df_usuarios = cargar_usuarios()
    
    tab1, tab2, tab3 = st.tabs(["📋 Lista de Usuarios", "➕ Crear Usuario", "🔧 Gestionar"])
    
    # Tab 1: Lista de usuarios
    with tab1:
        st.subheader("Usuarios Registrados")
        
        # Ocultar el hash de la contraseña
        df_display = df_usuarios[['usuario', 'nombre_completo', 'rol', 'activo', 'fecha_creacion']].copy()
        st.dataframe(df_display, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Usuarios", len(df_usuarios))
        col2.metric("Activos", len(df_usuarios[df_usuarios['activo'] == True]))
        col3.metric("Inactivos", len(df_usuarios[df_usuarios['activo'] == False]))
    
    # Tab 2: Crear usuario
    with tab2:
        st.subheader("Crear Nuevo Usuario")
        
        with st.form("form_crear_usuario"):
            col1, col2 = st.columns(2)
            
            with col1:
                nuevo_usuario = st.text_input("Usuario *", placeholder="ejemplo: jperez")
                nuevo_nombre = st.text_input("Nombre Completo *", placeholder="Juan Pérez")
            
            with col2:
                nuevo_password = st.text_input("Contraseña *", type="password", placeholder="Mínimo 6 caracteres")
                nuevo_rol = st.selectbox("Rol *", ["usuario", "admin"])
            
            if st.form_submit_button("➕ Crear Usuario", type="primary"):
                if not nuevo_usuario or not nuevo_password or not nuevo_nombre:
                    st.error("❌ Complete todos los campos obligatorios")
                elif len(nuevo_password) < 6:
                    st.error("❌ La contraseña debe tener al menos 6 caracteres")
                else:
                    exito, mensaje = crear_usuario(nuevo_usuario, nuevo_password, nuevo_nombre, nuevo_rol)
                    if exito:
                        st.success(f"✅ {mensaje}")
                        st.rerun()
                    else:
                        st.error(f"❌ {mensaje}")
    
    # Tab 3: Gestionar usuarios
    with tab3:
        st.subheader("Gestionar Usuarios Existentes")
        
        usuarios_list = df_usuarios['usuario'].tolist()
        usuario_seleccionado = st.selectbox("Seleccionar Usuario", usuarios_list)
        
        if usuario_seleccionado:
            datos_usuario = df_usuarios[df_usuarios['usuario'] == usuario_seleccionado].iloc[0]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"""
                **Usuario:** {datos_usuario['usuario']}  
                **Nombre:** {datos_usuario['nombre_completo']}  
                **Rol:** {datos_usuario['rol']}  
                **Estado:** {'✅ Activo' if datos_usuario['activo'] else '❌ Inactivo'}  
                **Creado:** {datos_usuario['fecha_creacion']}
                """)
            
            with col2:
                st.markdown("### Acciones")
                
                if datos_usuario['activo']:
                    if st.button(f"🚫 Desactivar usuario '{usuario_seleccionado}'", use_container_width=True):
                        if usuario_seleccionado == 'admin':
                            st.error("❌ No se puede desactivar el usuario admin")
                        else:
                            desactivar_usuario(usuario_seleccionado)
                            st.success(f"Usuario '{usuario_seleccionado}' desactivado")
                            st.rerun()
                else:
                    if st.button(f"✅ Activar usuario '{usuario_seleccionado}'", use_container_width=True):
                        activar_usuario(usuario_seleccionado)
                        st.success(f"Usuario '{usuario_seleccionado}' activado")
                        st.rerun()
                
                st.divider()
                
                with st.expander("🔑 Cambiar Contraseña"):
                    with st.form(f"form_cambiar_pass_{usuario_seleccionado}"):
                        nueva_pass = st.text_input("Nueva Contraseña", type="password")
                        confirmar_pass = st.text_input("Confirmar Contraseña", type="password")
                        
                        if st.form_submit_button("💾 Actualizar Contraseña"):
                            if nueva_pass != confirmar_pass:
                                st.error("❌ Las contraseñas no coinciden")
                            elif len(nueva_pass) < 6:
                                st.error("❌ La contraseña debe tener al menos 6 caracteres")
                            else:
                                df_usuarios.loc[df_usuarios['usuario'] == usuario_seleccionado, 'password_hash'] = hash_password(nueva_pass)
                                guardar_usuarios(df_usuarios)
                                st.success("✅ Contraseña actualizada")
                                st.rerun()
