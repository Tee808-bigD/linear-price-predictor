@echo off
echo Installing Python packages...
echo.

REM Method 1: Try python -m pip
python -m pip install pandas scikit-learn joblib fastapi uvicorn

if %errorlevel% equ 0 (
    echo.
    echo ✅ Packages installed successfully!
    goto :success
)

echo.
echo ❌ Method 1 failed. Trying Method 2...
echo.

REM Method 2: Try with full path
where python >nul 2>nul
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('where python') do (
        echo Found Python at: %%i
        "%%i" -m pip install pandas scikit-learn joblib fastapi uvicorn
    )
) else (
    echo Python not found in PATH!
)

:success
echo.
echo Installation complete!
echo Run: python --version
echo Run: pip --version
pause