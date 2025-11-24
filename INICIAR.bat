@echo off
REM ========================================
REM   SISTEMA DE CONTROL DE INFORMES
REM   Script de Inicio Automático
REM ========================================

color 0A
title Sistema de Control de Informes

echo.
echo ========================================
echo   SISTEMA DE CONTROL DE INFORMES
echo   Iniciando aplicacion...
echo ========================================
echo.

REM Verificar que Python esta instalado
echo [1/5] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo.
    echo [ERROR] Python no esta instalado o no esta en el PATH
    echo.
    echo Por favor instala Python 3.8 o superior desde:
    echo https://www.python.org/downloads/
    echo.
    echo Asegurate de marcar "Add Python to PATH" durante la instalacion
    echo.
    pause
    exit /b 1
)
python --version
echo [OK] Python encontrado
echo.

REM Verificar que estamos en el directorio correcto
echo [2/5] Verificando directorio...
if not exist "app.py" (
    color 0C
    echo.
    echo [ERROR] No se encuentra app.py
    echo Asegurate de ejecutar este script desde la carpeta del proyecto
    echo.
    pause
    exit /b 1
)
echo [OK] Directorio correcto
echo.

REM Verificar/Instalar dependencias
echo [3/5] Verificando dependencias...
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo [INSTALANDO] Streamlit no encontrado, instalando...
    pip install streamlit pandas
    if errorlevel 1 (
        color 0C
        echo.
        echo [ERROR] No se pudieron instalar las dependencias
        echo Intenta manualmente: pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
) else (
    echo [OK] Dependencias instaladas
)
echo.

REM Verificar archivos de datos
echo [4/5] Verificando archivos de datos...
if not exist "LISTADO-CON-FASES.csv" (
    echo [ADVERTENCIA] LISTADO-CON-FASES.csv no encontrado
    echo La aplicacion iniciara con base de datos vacia
    echo Podras importar centros desde la interfaz
)
if not exist "seguimiento_informes.csv" (
    echo [INFO] seguimiento_informes.csv se creara automaticamente
)
if not exist "calendario.csv" (
    echo [INFO] calendario.csv se creara automaticamente
)
echo [OK] Verificacion completada
echo.

REM Limpiar pantalla anterior de Streamlit si existe
taskkill /F /IM streamlit.exe >nul 2>&1

REM Iniciar aplicacion
echo [5/5] Iniciando aplicacion...
echo.
echo ========================================
echo   APLICACION INICIADA
echo ========================================
echo.
echo   URL Local:    http://localhost:8501
echo   URL Red:      http://%COMPUTERNAME%:8501
echo.
echo   Presiona Ctrl+C para detener
echo ========================================
echo.

REM Esperar 2 segundos y abrir navegador
timeout /t 2 /nobreak >nul
start http://localhost:8501

REM Iniciar Streamlit
python -m streamlit run app.py

REM Si Streamlit se cierra, mostrar mensaje
echo.
echo ========================================
echo   Aplicacion detenida
echo ========================================
echo.
pause
