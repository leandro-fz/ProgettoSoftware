from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.piscina.GestioneIscritti.controller_gestione_iscritti.controller_gestione_iscritti import \
    controller_gestione_iscritti
from struttura.piscina.GestioneIscritti.view_modifica_utente.view_modifica_utente import view_modifica_utente
from struttura.piscina.Iscritti.controller_iscritti.controller_iscritti import controller_iscritti
from struttura.piscina.Iscritti.view_iscritti.view_inserisci_utente import view_inserisci_utente


class view_iscritti(QWidget):

    def __init__(self, parent=None):
        super(view_iscritti, self).__init__(parent)

        self.controller = controller_iscritti()

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

        self.inserisci_utente = QPushButton("Inserisci utente")
        self.inserisci_utente.clicked.connect(self.mostra_inserisci_utente)
        self.inserisci_utente.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.inserisci_utente)
        self.inserisci_utente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.elimina_utente = QPushButton("Elimina utente")
        self.elimina_utente.setFont(self.font_bottoni)
        self.elimina_utente.clicked.connect(self.mostra_elimina_utente)
        self.h_layout.addWidget(self.elimina_utente)
        self.elimina_utente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.modifica_utente = QPushButton("Modifica utente")
        self.modifica_utente.setFont(self.font_bottoni)
        self.modifica_utente.clicked.connect(self.mostra_modifica_utente)
        self.h_layout.addWidget(self.modifica_utente)
        self.modifica_utente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco iscritti")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/sfondonuotosfocato2.jpeg")
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

        for utente in self.controller.get_lista_iscritti():
            item = QStandardItem()
            item.setText(utente.nome + " " + utente.cognome)
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def mostra_inserisci_utente(self):

        self.inserisci_utente = view_inserisci_utente(self.controller, self.aggiorna_dati)
        self.inserisci_utente.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def mostra_elimina_utente(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_iscritti()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un utente da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Vuoi eliminare l' utente?", QMessageBox.Yes,
                                        QMessageBox.No)

        if risposta == QMessageBox.Yes:

            self.controller.elimina_utente_by_codicefiscale(da_eliminare.codicefiscale)
            QMessageBox.about(self, "Eliminato", "L' utente è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    def mostra_modifica_utente(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_iscritti()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un utente da visualizzare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        self.modifica_utente = view_modifica_utente(controller_gestione_iscritti(da_visualizzare),
                                                           self.aggiorna_dati, self.controller.get_lista_iscritti())
        self.modifica_utente.show()
