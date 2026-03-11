@echo off
chcp 65001 >nul
echo ========================================
echo Sheep Village Finance - Start
echo ========================================
echo.

echo [1/3] Checking Python...
python --version
if errorlevel 1 (
    echo ERROR: Python not found
    pause
    exit /b 1
)

echo.
echo [2/3] Checking packages...
python -c "import streamlit; import plotly; import pandas"
if errorlevel 1 (
    echo ERROR: Missing packages
    echo Installing...
    pip install -r requirements.txt
)

echo.
echo [3/3] Starting app...
echo.
echo App will open in browser
echo URL: http://localhost:8501
echo.
echo ========================================
echo Press Ctrl+C to stop
echo ========================================
echo.

streamlit run app.py

pause
