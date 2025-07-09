from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from modules.byte import Byte
from modules.debyte import deByte
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("qc.Compress")
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self.setWindowIcon(QIcon("icon.png"))

        compress_button = QPushButton("Compress")
        decompress_button = QPushButton("Decompress")

        compress_button.clicked.connect(self.run_compress)
        decompress_button.clicked.connect(self.run_decompress)

        layout = QVBoxLayout()
        layout.addWidget(compress_button)
        layout.addWidget(decompress_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_compress(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select a file to compress")
        if path:
            Byte(path)

    def run_decompress(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select a file to decompress")
        if path:
            deByte(path)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
