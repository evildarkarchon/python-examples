from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Slot, Signal


class MyWidget(QWidget):
    value_changed = Signal(int)

    def __init__(self):
        super().__init__()

        # Set up layout and widgets
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Value: 0")
        layout.addWidget(self.label)

        button = QPushButton("Increment")
        layout.addWidget(button)

        # Connect button clicked signal to increment function
        button.clicked.connect(self.increment_value) # type: ignore

    @Slot()
    def increment_value(self):
        # Get current value from label text
        current_value = int(self.label.text().split()[-1])

        # Increment value and update label
        new_value = current_value + 1
        self.label.setText(f"Value: {new_value}")

        # Emit signal with new value
        self.value_changed.emit(new_value)


# Create application and widget
app = QApplication([])
widget = MyWidget()

# Connect value changed signal to print function
widget.value_changed.connect(lambda value: print(f"New value: {value}"))

# Show widget and run event loop
widget.show()
app.exec()
