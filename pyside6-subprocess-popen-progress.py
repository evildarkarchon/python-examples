import sys
import subprocess
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QApplication, QProgressBar

app = QApplication(sys.argv)

progressBar = QProgressBar()
progressBar.setRange(0, 100)
progressBar.show()

process = subprocess.Popen('your_program', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True:
    output = process.stdout.readline() # type: ignore
    if output == '' and process.poll() is not None:
        break
    if output:
        progressBar.setValue(progressBar.value() + 1)

sys.exit(app.exec())
