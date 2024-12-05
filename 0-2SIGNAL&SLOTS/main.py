#VERSION2 : SIGNALS SENDING VALUES, CAPTURE VALUES IN SLOTS
from PySide6.QtWidgets import QApplication, QPushButton
def button_clicked(data):
    print("You clicked the button, Didn't you checked : ", data)

app= QApplication()
button = QPushButton("Press here !!")
##data
button.setCheckable(True) ##will toggle data


button.clicked.connect(button_clicked)
button.show()
app.exec()

