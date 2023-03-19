from PySide6.QtCore import QThread, Signal


class WorkerThread(QThread):
    result = Signal(int)

    def run(self):
        # Your function code here
        result = 42
        self.result.emit(result)


thread = WorkerThread()
thread.result.connect(lambda result: print(result))
thread.start()
