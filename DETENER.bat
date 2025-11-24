@echo off
REM ========================================
REM   DETENER SISTEMA DE CONTROL DE INFORMES
REM ========================================

color 0E
title Detener Aplicacion

echo.
echo ========================================
echo   DETENER APLICACION
echo ========================================
echo.

echo Buscando procesos de Streamlit...
echo.

REM Buscar y mostrar procesos de Streamlit
tasklist | findstr /I "streamlit" >nul 2>&1
if errorlevel 1 (
    echo [INFO] No se encontraron procesos de Streamlit ejecutandose
    echo.
    pause
    exit /b 0
)

echo Procesos encontrados:
tasklist | findstr /I "streamlit"
echo.

REM Confirmar antes de detener
set /p confirmar="Deseas detener todos los procesos de Streamlit? (S/N): "
if /I "%confirmar%" NEQ "S" (
    echo.
    echo Operacion cancelada
    echo.
    pause
    exit /b 0
)

echo.
echo Deteniendo procesos...
taskkill /F /IM streamlit.exe >nul 2>&1
taskkill /F /IM python.exe /FI "WINDOWTITLE eq streamlit*" >nul 2>&1

echo.
echo [OK] Procesos detenidos
echo.
echo ========================================
echo   Aplicacion detenida correctamente
echo ========================================
echo.
pause
