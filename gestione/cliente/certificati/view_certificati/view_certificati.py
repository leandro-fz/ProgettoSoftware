from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *




from gestione.cliente.GestioneCertificati.controller_GestioneCertificati.controller_GestioneCertificati import \
    Controller_GestioneCertificati
from gestione.cliente.GestioneCertificati.view_GestioneCertificati.view_GestioneCertificati import \
    view_ModificaCertificato
from gestione.cliente.certificati.controller_certificati.controller_certficati import Controller_Certificati
from gestione.cliente.certificati.view_certificati.view_inserisci_certificato import view_InserisciCertificato


class view_certificati(QWidget):

    def __init__(self, parent=None):
        super(view_certificati, self).__init__(parent)

        self.controller = Controller_Certificati()

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.list_view.setGeometry(40, 60, 500, 401)

        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.font_bottoni = QFont("Yu Gothic UI Light", 12)

        self.indietro = QPushButton("⬅️")
        self.indietro.setIconSize(QtCore.QSize(40, 40))
        self.indietro.setDefault(False)
        self.indietro.setFont(self.font_bottoni)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.chiudi_schermata)

        self.h_layout.addWidget(self.indietro)
        self.indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.indietro.setIconSize(QtCore.QSize(40, 40))
        self.indietro.clicked.connect(self.chiudi_schermata)

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
            QMessageBox.critical(self, "Errore", "Seleziona un certificato da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Vuoi eliminare il certificato?", QMessageBox.Yes,
                                        QMessageBox.No)

        if risposta == QMessageBox.Yes:

            self.controller.elimina_certificato_by_codicefiscale(da_eliminare.codicefiscale)
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
                                                           self.aggiorna_dati, self.controller.get_lista_certificati())
        self.modifica_certificato.show()
