@echo off
echo ========================================
echo    PRICE PREDICTOR - COMPLETE SETUP
echo ========================================
echo.

REM 1. Install dependencies
echo 1. Installing dependencies...
python -m pip install pandas scikit-learn joblib fastapi uvicorn --quiet
echo ✅ Dependencies installed

REM 2. Train model
echo.
echo 2. Training model...
python test_model.py

REM 3. Start API
echo.
echo 3. Starting API...
echo    API will start on http://localhost:8000
echo    Press Ctrl+C to stop the API
echo.
python api.py