
'''
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

'''
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider
def respond_to_slider(data):
    print("slider moved to : ",data)
app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(1)

#you just do the connection. The Qt system takes care of 
# pasing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()