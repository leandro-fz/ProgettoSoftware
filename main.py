from PyQt5 import QtWidgets

from home.views.VistaHome import Ui_Schermataprincipale

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Schermataprincipale()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())