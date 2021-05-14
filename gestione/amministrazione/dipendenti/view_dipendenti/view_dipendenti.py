
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from gestione.amministrazione.dipendenti.controller_dipendenti.controller_dipendenti import ControlloreListaDipendenti
from gestione.amministrazione.dipendenti.view_dipendenti.view_inserisci_dipendente import VistaInserisciDipendente


class Ui_dipendenti(object):

    def __int__(self, parent= None):
        super(Ui_dipendenti, self).__int__(parent)
        self.controller = ControlloreListaDipendenti()
        self.setupUi()



    def setupUi(self, dipendenti):

        dipendenti.setObjectName("dipendenti")
        dipendenti.resize(781, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dipendenti.sizePolicy().hasHeightForWidth())
        dipendenti.setSizePolicy(sizePolicy)
        dipendenti.setMinimumSize(QtCore.QSize(781, 500))
        dipendenti.setMaximumSize(QtCore.QSize(781, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/immaginelogo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dipendenti.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(dipendenti)
        self.centralwidget.setObjectName("centralwidget")
        self.immaginepesi = QtWidgets.QLabel(self.centralwidget)
        self.immaginepesi.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.immaginepesi.setText("")
        self.immaginepesi.setPixmap(QtGui.QPixmap("images/immaginepesisfocata.jpeg"))
        self.immaginepesi.setScaledContents(True)
        self.immaginepesi.setAlignment(QtCore.Qt.AlignCenter)
        self.immaginepesi.setObjectName("immaginepesi")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(40, 50, 581, 381))
        self.listView.setObjectName("listView")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(600, 50, 22, 381))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setObjectName("verticalSlider")

        #self.verticalSlider.valueChanged.connect(self.listView)
        self.aggiungidipendente = QtWidgets.QPushButton(self.centralwidget)
        self.aggiungidipendente.setGeometry(QtCore.QRect(630, 50, 140, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.aggiungidipendente.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.aggiungidipendente.setFont(font)
        self.aggiungidipendente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aggiungidipendente.setObjectName("aggiungidipendente")
        self.eliminadipendente = QtWidgets.QPushButton(self.centralwidget)
        self.eliminadipendente.setGeometry(QtCore.QRect(630, 90, 140, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.eliminadipendente.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eliminadipendente.setFont(font)
        self.eliminadipendente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminadipendente.setObjectName("eliminasocio")
        self.freccia = QtWidgets.QPushButton(self.centralwidget)
        self.freccia.setGeometry(QtCore.QRect(20, 10, 51, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.freccia.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.freccia.setFont(font)
        self.freccia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.freccia.setIconSize(QtCore.QSize(40, 40))
        self.freccia.setDefault(False)
        self.freccia.setObjectName("freccia")
        dipendenti.setCentralWidget(self.centralwidget)

        self.retranslateUi(dipendenti)
        QtCore.QMetaObject.connectSlotsByName(dipendenti)

        self.listView_model = QStandardItemModel(self.listView)
        for dipendente in self.controller.get_lista_dipendenti():
            item= QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listView_model.appendRow(item)
        self.listView.setModel(self.listView_model)




        self.freccia.clicked.connect(dipendenti.close)

        self.aggiungidipendente.clicked.connect(self.view_nuovodipendente)








    def view_nuovodipendente(self):
        self.vista_inserisci_dipendente = view_inserisci_dipendente(self.controller,self)
        self.vista_inserisci_dipendente.sow()

    def retranslateUi(self, dipendenti):
        _translate = QtCore.QCoreApplication.translate
        dipendenti.setWindowTitle(_translate("dipendenti", "Dipendenti"))
        self.aggiungidipendente.setText(_translate("dipendenti", "Aggiungi dipendente"))
        self.eliminadipendente.setText(_translate("dipendenti", "Elimina dipendente"))
        self.freccia.setText(_translate("dipendenti", "⬅️"))
        self.freccia.setShortcut(_translate("dipendenti", "Alt+Left"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     dipendenti = QtWidgets.QMainWindow()
#     ui = Ui_dipendenti()
#     ui.setupUi(dipendenti)
#     dipendenti.show()
#     sys.exit(app.exec_())
