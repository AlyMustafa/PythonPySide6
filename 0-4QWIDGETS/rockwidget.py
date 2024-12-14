from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class RockWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aya Mustafa")

        button1 = QPushButton("اضربها")
        button2 = QPushButton("بوسها")

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)
