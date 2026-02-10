@echo off
echo ========================================
echo    PYTHON & PACKAGES INSTALLER
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>nul
if %errorlevel% equ 0 (
    echo ✅ Python is installed
    goto :install_packages
)

echo ❌ Python not found or not in PATH
echo.
echo Please install Python:
echo 1. Go to: https://www.python.org/downloads/
echo 2. Download Windows 64-bit installer
echo 3. RUN AS ADMINISTRATOR
echo 4. CHECK: "Add Python to PATH"
echo 5. Click "Install Now"
echo.
echo After installation, CLOSE THIS WINDOW
echo and run this script again.
echo.
pause
exit /b 1

:install_packages
echo.
echo Installing Python packages...
echo ========================================

echo 1. Upgrading pip...
python -m pip install --upgrade pip

echo 2. Installing pandas...
python -m pip install pandas

echo 3. Installing scikit-learn...
python -m pip install scikit-learn

echo 4. Installing joblib...
python -m pip install joblib

echo 5. Installing fastapi...
python -m pip install fastapi

echo 6. Installing uvicorn...
python -m pip install uvicorn[standard]

echo.
echo ========================================
echo ✅ ALL PACKAGES INSTALLED!
echo ========================================
echo.
echo Verification:
python --version
python -m pip --version
echo.
pause