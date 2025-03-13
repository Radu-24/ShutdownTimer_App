@echo off
setlocal

:: Check if Git is installed
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Git is not installed. Installing Git...
    winget install -e --id Git.Git
    echo Git installation complete. Please restart this script.
    pause
    exit /b
)

:: Install Python (if not already installed)
where python >nul 2>&1 || winget install -e --id Python.Python.3

:: Install PyInstaller (if not already installed)
pip show pyinstaller >nul 2>&1 || pip install pyinstaller

:: Clone repository (if not already cloned)
if not exist ShutdownTimer_App git clone https://github.com/Radu-24/ShutdownTimer_App.git
cd ShutdownTimer_App

:: Build the executable
pyinstaller --onefile --windowed --clean --icon=icon/shutdowntimer.ico shutdown_timer.py

:: Confirm setup complete
echo Setup complete!
pause
endlocal
