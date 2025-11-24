@echo off
REM Script para iniciar la aplicación en Windows

echo ========================================
echo   Sistema de Control de Informes
echo ========================================
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor instala Python 3.8 o superior
    pause
    exit /b 1
)

echo [1/3] Verificando dependencias...
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo Instalando dependencias...
    pip install -r requirements.txt
) else (
    echo Dependencias OK
)

echo.
echo [2/3] Verificando archivos de datos...
if not exist "LISTADO-CON-FASES.csv" (
    echo ADVERTENCIA: LISTADO-CON-FASES.csv no encontrado
    echo La aplicación iniciará con base de datos vacía
)

echo.
echo [3/3] Iniciando aplicación...
echo.
echo ========================================
echo   Aplicación iniciada correctamente
echo   URL: http://localhost:8501
echo   Presiona Ctrl+C para detener
echo ========================================
echo.

REM Iniciar Streamlit
python -m streamlit run app.py

pause
