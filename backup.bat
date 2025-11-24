@echo off
REM Script de backup automático para Windows

echo ========================================
echo   Backup de Datos
echo ========================================
echo.

REM Crear carpeta de backups si no existe
if not exist "backups" mkdir backups

REM Obtener fecha y hora actual
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "timestamp=%dt:~0,4%%dt:~4,2%%dt:~6,2%_%dt:~8,2%%dt:~10,2%%dt:~12,2%"

REM Crear carpeta de backup con timestamp
set "backup_dir=backups\backup_%timestamp%"
mkdir "%backup_dir%"

echo Creando backup en: %backup_dir%
echo.

REM Copiar archivos de datos
if exist "LISTADO-CON-FASES.csv" (
    copy "LISTADO-CON-FASES.csv" "%backup_dir%\" >nul
    echo [OK] LISTADO-CON-FASES.csv
) else (
    echo [SKIP] LISTADO-CON-FASES.csv no encontrado
)

if exist "seguimiento_informes.csv" (
    copy "seguimiento_informes.csv" "%backup_dir%\" >nul
    echo [OK] seguimiento_informes.csv
) else (
    echo [SKIP] seguimiento_informes.csv no encontrado
)

if exist "calendario.csv" (
    copy "calendario.csv" "%backup_dir%\" >nul
    echo [OK] calendario.csv
) else (
    echo [SKIP] calendario.csv no encontrado
)

echo.
echo ========================================
echo   Backup completado exitosamente
echo   Ubicación: %backup_dir%
echo ========================================
echo.

REM Limpiar backups antiguos (mantener solo los últimos 10)
for /f "skip=10 delims=" %%i in ('dir /b /ad /o-d backups\backup_*') do (
    rd /s /q "backups\%%i"
    echo Eliminado backup antiguo: %%i
)

pause
