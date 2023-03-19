from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Signal, Slot, QThread, QObject
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the progress bar widget
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(30, 40, 200, 25)

        # Create a button to trigger the signal
        button = QPushButton("Start", self)
        button.clicked.connect(self.startTask) # type: ignore

        # Create a layout for the window and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.progressbar)
        layout.addWidget(button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    @Slot(int)
    def updateProgress(self, value):
        self.progressbar.setValue(value)

    def startTask(self):
        # Connect the signal to the updateProgress method
        self.task.signal_progress.connect(self.updateProgress) # type: ignore

        # Start the task in a separate thread
        self.task.start() # type: ignore


class MyTask(QObject):
    signal_progress = Signal(int)

    def __init__(self):
        super().__init__()

    def start(self):
        # Your task code here
        for i in range(101):
            self.signal_progress.emit(i)
            # Add a delay to simulate a long-running task
            QThread.msleep(50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.task = MyTask() # type: ignore
    window.show()
    sys.exit(app.exec_())
