import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


from home.views.VistaHome import MainWindow

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui=MainWindow()
    ui.setupUi(MainWindow)
    home.show()
    sys.exit(app.exec_())
