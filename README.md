# Shutdown Timer App

🛠️ Developed by **Radu**, a student at **ETTI (Electronics, Telecommunications, and Information Technology)**, with a passion for **cybersecurity** and software development.

A simple Python application that allows users to schedule a shutdown of their Windows computer at a specified time.

## 🖼️ Custom Icon

![Shutdown Timer Icon](icon/shutdowntimer.ico)

## 🛠️ Requirements

- 🐍 Python 3.x
- 🖥️ Windows OS

## 🚀 Features

- 🕒 Set a specific time for the computer to shut down.
- ❌ Cancel a scheduled shutdown if needed.
- 🎛️ Simple and user-friendly interface.

## 📥 Installation

Choose one of the following methods to install or run the Shutdown Timer app:

### 🔹 Option 1: Download Only the Executable (No setup required)

If you prefer using a precompiled `.exe`, follow these steps:

1. Go to the [Releases](https://github.com/Radu-24/ShutdownTimer_App/releases) page on GitHub.
2. Download `shutdown_timer.exe` from the latest release.
3. Run the `.exe`—no additional installation required!

### 🔹 Option 2: Install Using Winget (Windows Only)

For an easy installation via Winget:

```sh
winget install -e --id Radu24.ShutdownTimer
```

### 🔹 Option 3: Clone the Repository & Run from Source

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/Radu-24/ShutdownTimer_App.git
   ```

2. **Navigate to the Project Directory:**

   ```sh
   cd ShutdownTimer_App
   ```

3. **Ensure Python is installed:**

   Check your Python installation:

   ```sh
   python --version
   ```

   If Python is not installed, download it from [python.org](https://www.python.org/downloads/) or install via Winget:

   ```sh
   winget install -e --id Python.Python.3
   ```

4. **Install required dependencies:**

   ```sh
   pip install pyinstaller
   ```

5. **Run the script:**

   ```sh
   python shutdown_timer.py
   ```

## ▶️ Usage

Run the application:

```sh
python shutdown_timer.py
```

### 💡 Example Output

```
Current time is 14:30
Enter shutdown time (HH:MM): 15:00
System will shut down in 1800 seconds.
Enter 'Cancel' to abort, or press Enter to exit: Cancel
System shutdown cancelled.
```

## 🏗️ Build Your Own Executable

If you prefer creating your own `.exe` file, follow these steps:

### 📥 Required Software

- [Python 3.x](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/) (optional but recommended)
- PyInstaller (via `pip`)

### 🚀 Steps to Build the Executable

1. **Ensure Python is installed:**

   ```sh
   python --version
   ```

2. **Install PyInstaller:**

   ```sh
   pip install pyinstaller
   ```

3. **Compile the script into an executable:**

   ```sh
   pyinstaller --onefile --windowed shutdown_timer.py
   ```

4. **(Optional) Add custom icon:**

   ```sh
   pyinstaller --onefile --windowed --icon=icon/shutdowntimer.ico shutdown_timer.py
   ```

   If the custom icon fails, at least the executable will still be created.

5. **Locate the ************`.exe`************ in the ************`dist/`************ folder.**

### 🛠️ VS Code Setup (Optional)

If you're using VS Code:

- Install the **Python extension** for running and debugging scripts.

Run the app in VS Code terminal:

```sh
python shutdown_timer.py
```

## 🛡️ Security & Trust

This project is **open-source**, allowing full transparency. You can review the source code anytime. No hidden trackers, malware, or backdoors exist.

### ❗ Windows Defender Warning

Windows Defender may display a SmartScreen warning because the file is **unsigned**. This warning is normal for unsigned applications from individual developers.

### ✅ Verify Yourself

- **Scan the file** with antivirus software.
- **Review the source code** by cloning and inspecting it directly.
- **Build your own executable** using instructions above.

## 📜 Automated Setup (Batch Script)

For convenience, you can automate the setup using a batch script. Create a file or run the file named `setup.bat`:

```bat
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
```

Double-click the `setup.bat` to run the automatic setup.

## 🔮 Future Plans

🔹 **Linux Support**: Future updates may include compatibility with Linux.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to contribute!

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

🚀 **Enjoy your Shutdown Timer!**

