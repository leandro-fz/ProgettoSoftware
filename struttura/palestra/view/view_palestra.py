
from PyQt5 import QtCore, QtGui, QtWidgets

from struttura.palestra.Corsi.view_corsi.view_corsi_palestra import view_corsi_palestra
from struttura.palestra.Iscritti.view_iscritti.view_iscritti_palestra import view_iscritti_palestra

#visualizzazione schermata palestra
class view_palestra(object):

    def setupUi(self, gestionepalestra):
        gestionepalestra.setObjectName("gestionepalestra")
        gestionepalestra.resize(781, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gestionepalestra.sizePolicy().hasHeightForWidth())
        gestionepalestra.setSizePolicy(sizePolicy)
        gestionepalestra.setMinimumSize(QtCore.QSize(781, 500))
        gestionepalestra.setMaximumSize(QtCore.QSize(781, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/immaginelogo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gestionepalestra.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(gestionepalestra)
        self.centralwidget.setObjectName("centralwidget")
        self.immaginepesi = QtWidgets.QLabel(self.centralwidget)
        self.immaginepesi.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.immaginepesi.setText("")
        self.immaginepesi.setTextFormat(QtCore.Qt.AutoText)
        self.immaginepesi.setPixmap(QtGui.QPixmap("images/immaginepesisfocata.jpeg"))
        self.immaginepesi.setScaledContents(True)
        self.immaginepesi.setAlignment(QtCore.Qt.AlignCenter)
        self.immaginepesi.setObjectName("immaginepesi")
        self.iscritti = QtWidgets.QPushButton(self.centralwidget)
        self.iscritti.setGeometry(QtCore.QRect(100, 200, 220, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iscritti.sizePolicy().hasHeightForWidth())
        self.iscritti.setSizePolicy(sizePolicy)
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
        self.iscritti.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.iscritti.setFont(font)
        self.iscritti.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.iscritti.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iscritti.setAutoExclusive(False)
        self.iscritti.setAutoDefault(False)
        self.iscritti.setDefault(False)
        self.iscritti.setFlat(False)
        self.iscritti.setObjectName("iscritti")
        self.gestionecorsi = QtWidgets.QPushButton(self.centralwidget)
        self.gestionecorsi.setGeometry(QtCore.QRect(430, 200, 220, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gestionecorsi.sizePolicy().hasHeightForWidth())
        self.gestionecorsi.setSizePolicy(sizePolicy)
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
        self.gestionecorsi.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gestionecorsi.setFont(font)
        self.gestionecorsi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gestionecorsi.setDefault(False)
        self.gestionecorsi.setFlat(False)
        self.gestionecorsi.setObjectName("gestionecorsi")
        self.freccia = QtWidgets.QPushButton(self.centralwidget)
        self.freccia.setGeometry(QtCore.QRect(30, 20, 51, 31))
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
        gestionepalestra.setCentralWidget(self.centralwidget)

        self.retranslateUi(gestionepalestra)
        QtCore.QMetaObject.connectSlotsByName(gestionepalestra)

        self.freccia.clicked.connect(gestionepalestra.close)

        self.gestionecorsi.clicked.connect(self.mostra_corsi)

        self.iscritti.clicked.connect(self.mostra_iscritti)

    #funzione per mostrare gli iscritti della palestra
    def mostra_iscritti(self):
        self.gestioneiscritti = view_iscritti_palestra()
        self.gestioneiscritti.show()

    #funzione per mostrare i corsi della palestra
    def mostra_corsi(self):
        self.gestionecorsi = view_corsi_palestra()
        self.gestionecorsi.show()

    def retranslateUi(self, gestionepalestra):
        _translate = QtCore.QCoreApplication.translate
        gestionepalestra.setWindowTitle(_translate("gestionepalestra", "Gestione palestra"))
        self.iscritti.setText(_translate("gestionepalestra", "Iscritti"))
        self.gestionecorsi.setText(_translate("gestionepalestra", "Gestione corsi"))
        self.freccia.setText(_translate("gestionepalestra", "⬅️"))
        self.freccia.setShortcut(_translate("gestionepalestra", "Alt+Left"))
