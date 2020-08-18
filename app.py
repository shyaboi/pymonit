from hardwareTracker import dateF
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
import threading

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")
# threading set interval timer

        label = QLabel("ok "+dateF)
        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)

        def setInterval(func, time):
            e = threading.Event()
            while not e.wait(time):
                func()

        def foo():
          lable.setText("new time: "+dateF)
        setInterval(foo, 1)
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()





# setInterval(foo,1)


