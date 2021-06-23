
from PyQt5 import QtCore, QtGui, QtWidgets

from gestione.cliente.abbonamenti.view_abbonamenti.view_abbonamenti import view_abbonamenti
from gestione.cliente.certificati.view_certificati.view_certificati import view_certificati


class Ui_gestionefinanziaria(object):

    def setupUi(self, gestionefinanziaria):
        gestionefinanziaria.setObjectName("gestionefinanziaria")
        gestionefinanziaria.resize(781, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gestionefinanziaria.sizePolicy().hasHeightForWidth())
        gestionefinanziaria.setSizePolicy(sizePolicy)
        gestionefinanziaria.setMinimumSize(QtCore.QSize(781, 500))
        gestionefinanziaria.setMaximumSize(QtCore.QSize(781, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/immaginelogo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gestionefinanziaria.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(gestionefinanziaria)
        self.centralwidget.setObjectName("centralwidget")
        self.immaginepesi = QtWidgets.QLabel(self.centralwidget)
        self.immaginepesi.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.immaginepesi.setText("")
        self.immaginepesi.setTextFormat(QtCore.Qt.AutoText)
        self.immaginepesi.setPixmap(QtGui.QPixmap("images/immaginepesisfocata.jpeg"))
        self.immaginepesi.setScaledContents(True)
        self.immaginepesi.setAlignment(QtCore.Qt.AlignCenter)
        self.immaginepesi.setObjectName("immaginepesi")


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
        gestionefinanziaria.setCentralWidget(self.centralwidget)

        self.inserisci_certificato = QPushButton("Inserisci certificato")
        self.inserisci_certificato.clicked.connect(self.mostra_inserisci_certificato)
        self.inserisci_certificato.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.inserisci_certificato)
        self.inserisci_certificato.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.elimina_certificato = QPushButton("Elimina certificato")
        self.elimina_certificato.setFont(self.font_bottoni)
        self.elimina_certificato.clicked.connect(self.mostra_elimina_certificato)
        self.h_layout.addWidget(self.elimina_certificato)
        self.elimina_certificato.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.modifica_certificato = QPushButton("Modifica certificato")
        self.modifica_certificato.setFont(self.font_bottoni)
        self.modifica_certificato.clicked.connect(self.mostra_modifica_certificato)
        self.h_layout.addWidget(self.modifica_certificato)
        self.modifica_certificato.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco Certificati")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.show()

    def chiudi_schermata(self):
        self.close()

    def aggiorna_dati(self):

        self.list_view_model = QStandardItemModel(self.list_view)

        self.font_item = QFont("Yu Gothic UI Light", 12)

        for certificato in self.controller.get_lista_certificati():
            item = QStandardItem()
            item.setText(certificato.nome + " " + certificato.cognome)
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def mostra_inserisci_certificato(self):

        self.inserisci_certificato = view_InserisciCertificato(self.controller, self.aggiorna_dati)
        self.inserisci_certificato.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def mostra_elimina_certificato(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_certificati()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un certificato da eliminare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Vuoi eliminare il certificato?", QMessageBox.Yes,
                                        QMessageBox.No)

        if risposta == QMessageBox.Yes:

            self.controller.elimina_certificato_by_id(da_eliminare.id)
            QMessageBox.about(self, "Eliminato", "Il certificato è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    def mostra_modifica_certificato(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_certificati()[index]
            print("ok")
        except:
            QMessageBox.critical(self, "Errore", "Seleziona un certificato da visualizzare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        self.modifica_certificato = view_ModificaCertificato(Controller_GestioneCertificati(da_visualizzare),
                                                             self.aggiorna_dati,
                                                             self.controller.get_lista_certificati())
        self.modifica_certificato.show()

        self.retranslateUi(gestionefinanziaria)
        QtCore.QMetaObject.connectSlotsByName(gestionefinanziaria)

        self.indietro.clicked.connect(gestionefinanziaria.close)

        self.gestioneabbonamento.clicked.connect(self.mostra_abbonamento)

        self.gestionecertificato.clicked.connect(self.mostra_certificato)

    def mostra_abbonamento(self):
        self.gestioneabbonamenti = view_abbonamenti()
        self.gestioneabbonamenti.show()

    def mostra_certificato(self):
        self.gestionecertificati = view_certificati()
        self.gestionecertificati.show()

    def retranslateUi(self, gestionefinanziaria):
        _translate = QtCore.QCoreApplication.translate
        gestionefinanziaria.setWindowTitle(_translate("gestionefinanziaria", "Gestione clienti"))
        self.gestioneabbonamento.setText(_translate("gestionefinanziaria", "Gestione abbonamento"))
        self.gestionecertificato.setText(_translate("gestionefinanziaria", "Gestione certificato"))
        self.indietro.setText(_translate("gestionefinanziaria", "⬅️"))
        self.indietro.setShortcut(_translate("gestionefinanziaria", "Alt+Left"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     gestionefinanziaria = QtWidgets.QMainWindow()
#     ui = Ui_gestionefinanziaria()
#     ui.setupUi(gestionefinanziaria)
#     gestionefinanziaria.show()
#     sys.exit(app.exec_())
