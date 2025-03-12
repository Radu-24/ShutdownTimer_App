# Shutdown Timer App

A simple Python application that allows users to schedule a shutdown of their Windows computer at a specified time.

## 🚀 Features

- 🕒 Set a specific time for the computer to shut down.
- ❌ Cancel a scheduled shutdown if needed.
- 🎛️ Simple and user-friendly interface.

## 🖼️ Custom Icon

![Shutdown Timer Icon](icon/shutdowntimer.ico)

## 🛠️ Requirements

- 🐍 Python 3.x
- 🖥️ Windows OS

## 📥 Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Radu-24/ShutdownTimer_App.git
   ```

2. **Navigate to the Project Directory:**
   ```sh
   cd ShutdownTimer_App
   ```

## ▶️ Usage

1. **Run the Application:**
   ```sh
   python shutdown_timer.py
   ```

2. **Follow the Prompts:**
   - The application will display the current time.
   - Enter the desired shutdown time in the format `HH:MM`.
   - The application will calculate the time difference and schedule the shutdown.
   - To cancel the scheduled shutdown, type `Cancel` when prompted.

### 💡 Example Output

```
Current time is 14:30
Enter shutdown time (HH:MM): 15:00
System will shut down in 1800 seconds.
Enter 'Cancel' to abort, or press Enter to exit: Cancel
System shutdown cancelled.
```

## 🏗️ Building an Executable (Optional)

To create a `.exe` version of the script with the custom icon, use **PyInstaller**:

1. Install PyInstaller:
   ```sh
   pip install pyinstaller
   ```

2. Create the executable:
   ```sh
   pyinstaller --onefile --windowed --icon=icon/shutdowntimer.ico shutdown_timer.py
   ```

3. The `.exe` file will be found in the `dist/` folder.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

If you’d like to contribute, feel free to fork this repository and submit a pull request.

---

🚀 **Enjoy your Shutdown Timer!**

