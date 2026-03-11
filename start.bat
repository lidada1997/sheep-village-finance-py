@echo off
echo ========================================
echo 羊村记账 - 一键启动
echo ========================================
echo.

echo [1/3] 检查Python环境...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python未安装
    pause
    exit /b 1
)

echo.
echo [2/3] 检查依赖包...
python -c "import streamlit; import plotly; import pandas"
if %errorlevel% neq 0 (
    echo ERROR: 缺少依赖包
    echo 正在安装...
    pip install -r requirements.txt
)

echo.
echo [3/3] 启动应用...
echo.
echo 应用将会在浏览器中自动打开
echo 访问地址：http://localhost:8501
echo.
echo ========================================
echo 按 Ctrl+C 停止应用
echo ========================================
echo.

streamlit run app.py

pause
