
from PySide6.QtWidgets import QWidget,QApplication
from rockwidget import RockWidget

import sys


app = QApplication(sys.argv)


window = RockWidget() 
window.show()
app.exec()