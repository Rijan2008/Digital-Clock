"""
DigitalClock.py
Description: A simple digital clock application built with PyQt5.
Author: Rijan Adhikari
Date: 2026/07/17
Purpose: Displays the current system time in a digital clock interface that updates every second.
Note: Before running this program, install PyQt5 using: pip install PyQt5
"""

import sys

# Import the required PyQt5 classes for creating the GUI
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


# Create a DigitalClock class that inherits from QWidget
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label to display the current time
        self.time_label = QLabel(self)

        # Create a timer that updates the clock every second
        self.timer = QTimer(self)

        # Initialize the user interface
        self.initUI()

    def initUI(self):
        # Set the window title and initial size
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 200, 100)

        # Create a vertical layout and add the time label
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Center the time within the window
        self.time_label.setAlignment(Qt.AlignCenter)

        # Style the time label with a large red font
        self.time_label.setStyleSheet(
            "font-size: 60px;"
            "color: yellow;"
            "font-family: Consolas;"
            "font-weight: bold;"
        )

        # Set the window background color to black
        self.setStyleSheet("background-color: black;")

        # Connect the timer to the update_time() method
        self.timer.timeout.connect(self.update_time)

        # Start the timer to update every 1000 milliseconds (1 second)
        self.timer.start(1000)

        # Display the current time immediately when the program starts
        self.update_time()

    def update_time(self):
        # Get the current system time in 12-hour format with AM/PM
        current_time = QTime.currentTime().toString("hh:mm:ss AP")

        # Update the label with the current time
        self.time_label.setText(current_time)


# Run the application
if __name__ == "__main__":
    # Create the PyQt application
    app = QApplication(sys.argv)

    # Create and display the digital clock window
    clock = DigitalClock()
    clock.show()

    # Start the application's event loop
    sys.exit(app.exec_())