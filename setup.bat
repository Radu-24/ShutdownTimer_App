@echo off
setlocal

:: Check if Git is installed
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Git is not installed. Installing Git...
    winget install --id Git.Git -e --source winget --silent

    :: Update PATH so Git can be used immediately without restart
    set "GIT_PATH=C:\Program Files\Git\cmd"
    setx PATH "%PATH%;%GIT_PATH%" >nul

    echo Git installed successfully. Continuing setup...
)

:: Check if Python is installed, install if missing
where python >nul 2>&1 || winget install -e --id Python.Python.3

:: Check if PyInstaller is installed, install if missing
pip show pyinstaller >nul 2>&1 || pip install pyinstaller

:: Clone repository (if not already cloned)
if not exist "ShutdownTimer_App" (
    echo Cloning repository...
    git clone https://github.com/Radu-24/ShutdownTimer_App.git
)

:: Navigate to the project folder
cd ShutdownTimer_App || exit

:: Build the executable
echo Building executable...
pyinstaller --onefile --windowed --clean --icon=icon/shutdowntimer.ico shutdown_timer.py

:: Confirm setup complete
echo Setup complete!
pause
endlocal
