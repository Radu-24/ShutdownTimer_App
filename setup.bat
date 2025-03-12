@echo off
setlocal

:: Install Python (if not already installed)
where python >nul 2>&1 || winget install -e --id Python.Python.3

:: Install PyInstaller
pip install pyinstaller

:: Clone repository (if not already cloned)
if not exist ShutdownTimer_App git clone https://github.com/Radu-24/ShutdownTimer_App.git
cd ShutdownTimer_App

:: Build the executable
pyinstaller --onefile --windowed --icon=icon/shutdowntimer.ico shutdown_timer.py

:: Confirm setup complete
echo Setup complete!
pause
endlocal