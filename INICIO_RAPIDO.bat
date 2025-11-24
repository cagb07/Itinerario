@echo off
REM Script rapido de inicio - Sin verificaciones
cd /d "%~dp0"
python -m streamlit run app.py
pause
