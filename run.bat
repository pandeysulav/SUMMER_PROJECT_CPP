@echo off
echo Starting ML Fitness Predictor...
echo.

REM Change to the project directory
cd /d "E:\SUMMER_PROJECT_CPP\ML"

REM Create necessary directories
if not exist "outputs" mkdir outputs
if not exist "outputs\visualizations" mkdir "outputs\visualizations"

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking dependencies...
python -c "import pandas, numpy, sklearn; print('All dependencies found!')" 2>nul
if %errorlevel% neq 0 (
    echo Installing required packages...
    pip install pandas numpy scikit-learn matplotlib seaborn
)

REM Run the main script
echo.
echo Running fitness predictor...
cd src
python main.py

REM Check if execution was successful
if %errorlevel% equ 0 (
    echo.
    echo SUCCESS: Fitness predictions completed!
    echo Check the outputs folder for results.
) else (
    echo.
    echo ERROR: Execution failed. Check the log file for details.
)

echo.
pause