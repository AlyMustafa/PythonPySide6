from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class RockWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PWM")

        button1 = QPushButton("Duty")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Bob")
        button2.clicked.connect(self.button2_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)

    def button1_clicked(self):
        print("antesh")
    def button2_clicked(self):
        print("Arza3")
