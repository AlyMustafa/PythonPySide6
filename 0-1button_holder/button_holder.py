
from PySide6.QtWidgets import  QMainWindow, QPushButton
class ButtonHolder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Sigma Engineering !!")
        button = QPushButton("Press")

        #set up the button as our central widget
        self.setCentralWidget(button)