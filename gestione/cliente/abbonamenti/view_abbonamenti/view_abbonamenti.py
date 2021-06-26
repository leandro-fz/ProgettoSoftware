from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.cliente.GestioneAbbonamenti.controller_GestioneAbbonamenti.Controller_GestioneAbbonamenti import \
    Controller_GestioneAbbonamenti
from gestione.cliente.abbonamenti.controller_abbonamenti.controller_abbonamenti import Controller_Abbonamenti
from gestione.cliente.GestioneAbbonamenti.view_GestioneAbbonamenti.view_modificaAbbonamenti import \
    view_ModificaAbbonamento
from gestione.cliente.abbonamenti.view_abbonamenti.view_inserisci_abbonamento import view_InserisciAbbonamento


class view_abbonamenti(QWidget):

    def __init__(self, parent=None):
        super(view_abbonamenti, self).__init__(parent)

        self.controller = Controller_Abbonamenti()

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

        self.inserisci_abbonamento = QPushButton("Inserisci Abbonamento")
        self.inserisci_abbonamento.clicked.connect(self.mostra_inserisci_abbonamento)
        self.inserisci_abbonamento.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.inserisci_abbonamento)
        self.inserisci_abbonamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.elimina_abbonamento = QPushButton("Elimina Abbonamento")
        self.elimina_abbonamento.setFont(self.font_bottoni)
        self.elimina_abbonamento.clicked.connect(self.mostra_elimina_abbonamento)
        self.h_layout.addWidget(self.elimina_abbonamento)
        self.elimina_abbonamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.modifica_abbonamento = QPushButton("Modifica Abbonamento")
        self.modifica_abbonamento.setFont(self.font_bottoni)
        self.modifica_abbonamento.clicked.connect(self.mostra_modifica_abbonamento)
        self.h_layout.addWidget(self.modifica_abbonamento)
        self.modifica_abbonamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco Abbonamenti")
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

        for abbonamento in self.controller.get_lista_abbonamenti():
            item = QStandardItem()
            item.setText(abbonamento.nome + " " + abbonamento.cognome)
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def mostra_inserisci_abbonamento(self):

        self.inserisci_abbonamento = view_InserisciAbbonamento(self.controller, self.aggiorna_dati)
        self.inserisci_abbonamento.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def mostra_elimina_abbonamento(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_abbonamenti()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un abbonamento da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Vuoi eliminare il abbonamento?", QMessageBox.Yes,
                                        QMessageBox.No)

        if risposta == QMessageBox.Yes:

            self.controller.elimina_abbonamento_by_codicefiscale(da_eliminare.codicefiscale)
            QMessageBox.about(self, "Eliminato", "L' abbonamento è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    def mostra_modifica_abbonamento(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_abbonamenti()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un abbonamento da visualizzare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        self.modifica_abbonamento = view_ModificaAbbonamento(Controller_GestioneAbbonamenti(da_visualizzare),
                                                           self.aggiorna_dati, self.controller.get_lista_abbonamenti())
        self.modifica_abbonamento.show()
