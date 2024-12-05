#Version1 : setting everything up in tehe global scope

"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#The system Module is responsible for processing command line argments
import sys
app = QApplication(sys.argv)

window= QMainWindow()
window.setWindowTitle("Aly Mustafa Enaya !!")

button= QPushButton()
button.setText("Press Here") 
window.setCentralWidget(button)
window.show()

#Start the event loop
app.exec()
"""


import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
#Start the event loop
app.exec() 

