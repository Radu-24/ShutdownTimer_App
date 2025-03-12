import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSlider
from PyQt6.QtCore import Qt

class ShutdownTimer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shutdown Timer")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Hour Slider
        self.hour_label = QLabel("Hours: 0")
        self.hour_slider = QSlider()
        self.hour_slider.setOrientation(Qt.Orientation.Horizontal)
        self.hour_slider.setRange(0, 24)
        self.hour_slider.valueChanged.connect(lambda: self.hour_label.setText(f"Hours: {self.hour_slider.value()}"))

        # Minute Slider
        self.minute_label = QLabel("Minutes: 0")
        self.minute_slider = QSlider()
        self.minute_slider.setOrientation(Qt.Orientation.Horizontal)
        self.minute_slider.setRange(0, 59)
        self.minute_slider.valueChanged.connect(lambda: self.minute_label.setText(f"Minutes: {self.minute_slider.value()}"))

        # Second Slider
        self.second_label = QLabel("Seconds: 0")
        self.second_slider = QSlider()
        self.second_slider.setOrientation(Qt.Orientation.Horizontal)
        self.second_slider.setRange(0, 59)
        self.second_slider.valueChanged.connect(lambda: self.second_label.setText(f"Seconds: {self.second_slider.value()}"))

        # Shutdown Button
        self.shutdown_btn = QPushButton("Set Shutdown Timer")
        self.shutdown_btn.clicked.connect(self.set_shutdown)

        # Cancel Shutdown Button
        self.cancel_btn = QPushButton("Cancel Shutdown")
        self.cancel_btn.clicked.connect(self.cancel_shutdown)

        # Layout
        layout.addWidget(self.hour_label)
        layout.addWidget(self.hour_slider)
        layout.addWidget(self.minute_label)
        layout.addWidget(self.minute_slider)
        layout.addWidget(self.second_label)
        layout.addWidget(self.second_slider)
        layout.addWidget(self.shutdown_btn)
        layout.addWidget(self.cancel_btn)

        self.setLayout(layout)

    def set_shutdown(self):
        hours = self.hour_slider.value()
        minutes = self.minute_slider.value()
        seconds = self.second_slider.value()
        total_time = hours * 3600 + minutes * 60 + seconds
        os.system(f"shutdown /s /t {total_time}")

    def cancel_shutdown(self):
        os.system("shutdown /a")

app = QApplication(sys.argv)
window = ShutdownTimer()
window.show()
sys.exit(app.exec())
