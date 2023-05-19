import sys
import time
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QProgressBar, QWidget


class WorkerThread(QThread):
    increment = Signal()

    def run(self):
        for _ in range(10):
            time.sleep(1)  # Simulate some work
            self.increment.emit() # type: ignore


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Progress Bar Example')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.start_button = QPushButton('Start')
        layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self.start_thread) # type: ignore

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_thread(self):
        self.worker = WorkerThread()
        self.worker.increment.connect(self.increment_progress) # type: ignore
        self.worker.start()

    def increment_progress(self):
        self.progress_bar.setValue(self.progress_bar.value() + 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
