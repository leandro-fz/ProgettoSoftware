
from PyQt5 import QtCore, QtGui, QtWidgets

from gestione.cliente.abbonamenti.view_abbonamenti.view_abbonamenti import view_abbonamenti
from gestione.cliente.certificati.view_certificati.view_certificati import view_certificati


class view_cliente(object):

    #view generale di clienti usata per la creazione di tre bottoni: indietro, gestione certificati e gestione abbonamenti
    def setupUi(self, gestioneclienti):
        gestioneclienti.setObjectName("gestioneclienti")
        gestioneclienti.resize(781, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gestioneclienti.sizePolicy().hasHeightForWidth())
        gestioneclienti.setSizePolicy(sizePolicy)
        gestioneclienti.setMinimumSize(QtCore.QSize(781, 500))
        gestioneclienti.setMaximumSize(QtCore.QSize(781, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/immaginelogo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gestioneclienti.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(gestioneclienti)
        self.centralwidget.setObjectName("centralwidget")
        self.immaginepesi = QtWidgets.QLabel(self.centralwidget)
        self.immaginepesi.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.immaginepesi.setText("")
        self.immaginepesi.setTextFormat(QtCore.Qt.AutoText)
        self.immaginepesi.setPixmap(QtGui.QPixmap("images/immaginepesisfocata.jpeg"))
        self.immaginepesi.setScaledContents(True)
        self.immaginepesi.setAlignment(QtCore.Qt.AlignCenter)
        self.immaginepesi.setObjectName("immaginepesi")
        self.gestioneabbonamento = QtWidgets.QPushButton(self.centralwidget)
        self.gestioneabbonamento.setGeometry(QtCore.QRect(120, 220, 220, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gestioneabbonamento.sizePolicy().hasHeightForWidth())
        self.gestioneabbonamento.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 157, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 28, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 157, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.gestioneabbonamento.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gestioneabbonamento.setFont(font)
        self.gestioneabbonamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gestioneabbonamento.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gestioneabbonamento.setAutoExclusive(False)
        self.gestioneabbonamento.setAutoDefault(False)
        self.gestioneabbonamento.setDefault(False)
        self.gestioneabbonamento.setFlat(False)
        self.gestioneabbonamento.setObjectName("gestioneabbonamento")

        self.gestionecertificato = QtWidgets.QPushButton(self.centralwidget)
        self.gestionecertificato.setGeometry(QtCore.QRect(420, 220, 220, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gestionecertificato.sizePolicy().hasHeightForWidth())
        self.gestionecertificato.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 157, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 157, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.gestionecertificato.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gestionecertificato.setFont(font)
        self.gestionecertificato.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gestionecertificato.setDefault(False)
        self.gestionecertificato.setFlat(False)
        self.gestionecertificato.setObjectName("gestionecertificato")

        self.indietro = QtWidgets.QPushButton(self.centralwidget)
        self.indietro.setGeometry(QtCore.QRect(30, 20, 51, 31))
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
        self.indietro.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.indietro.setFont(font)
        self.indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.indietro.setIconSize(QtCore.QSize(40, 40))
        self.indietro.setDefault(False)
        self.indietro.setObjectName("indietro")
        gestioneclienti.setCentralWidget(self.centralwidget)

        self.retranslateUi(gestioneclienti)
        QtCore.QMetaObject.connectSlotsByName(gestioneclienti)

        self.indietro.clicked.connect(gestioneclienti.close)

        self.gestioneabbonamento.clicked.connect(self.mostra_abbonamento)

        self.gestionecertificato.clicked.connect(self.mostra_certificato)

    #funzione che collega la view di clienti alla view di abbonamenti
    def mostra_abbonamento(self):
        self.gestioneabbonamenti = view_abbonamenti()
        self.gestioneabbonamenti.show()

    # funzione che collega la view di clienti alla view di certificati
    def mostra_certificato(self):
        self.gestionecertificati = view_certificati()
        self.gestionecertificati.show()

    #funzione che nomina i tre bottoni: indietro, gestione abbonamenti e gestione certificati
    def retranslateUi(self, gestioneclienti):
        _translate = QtCore.QCoreApplication.translate
        gestioneclienti.setWindowTitle(_translate("gestioneclienti", "Gestione clienti"))
        self.gestioneabbonamento.setText(_translate("gestioneclienti", "Gestione abbonamenti"))
        self.gestionecertificato.setText(_translate("gestioneclienti", "Gestione certificati"))
        self.indietro.setText(_translate("gestioneclienti", "⬅️"))
        self.indietro.setShortcut(_translate("gestioneclienti", "Alt+Left"))
