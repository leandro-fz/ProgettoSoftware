from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.amministrazione.GestioneDipendenti.controller_GestioneDipendenti.Controller_GestioneDipendenti import Controller_GestioneDipendenti
from gestione.amministrazione.dipendenti.controller_dipendenti.controller_dipendenti import Controller_Dipendenti
from gestione.amministrazione.GestioneDipendenti.view_GestioneDipendenti.view_modificaDipendenti import view_ModificaDipendente
from gestione.amministrazione.dipendenti.view_dipendenti.view_inserisci_dipendente import view_InserisciDipendente


class view_dipendenti(QWidget):

    def __init__(self, parent=None):
        super(view_dipendenti, self).__init__(parent)


        self.controller = Controller_Dipendenti()

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.list_view.setGeometry(40, 60, 500, 401)
        # self.listView.setObjectName("listView")

        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.font_bottoni = QFont("Yu Gothic UI Light", 12)

        self.indietro = QPushButton("⬅️")
        self.indietro.setIconSize(QtCore.QSize(40, 40))
        self.indietro.setDefault(False)
        self.indietro.setFont(self.font_bottoni)

        self.h_layout.addWidget(self.indietro)
        self.indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.indietro.setGeometry(QtCore.QRect(20, 20, 51, 31))
        self.indietro.setIconSize(QtCore.QSize(40, 40))
        self.indietro.clicked.connect(self.chiudi_schermata)


        self.inserisci_dipendente = QPushButton("Inserisci Dipendente")
        self.inserisci_dipendente.clicked.connect(self.mostra_inserisci_dipendente)
        self.inserisci_dipendente.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.inserisci_dipendente)
        self.inserisci_dipendente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.elimina_dipendente = QPushButton("Elimina Dipendente")
        self.elimina_dipendente.setFont(self.font_bottoni)
        self.elimina_dipendente.clicked.connect(self.mostra_elimina_dipendente)
        self.h_layout.addWidget(self.elimina_dipendente)
        self.elimina_dipendente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.modifica_dipendente = QPushButton("Modifica Dipendente")
        self.modifica_dipendente.setFont(self.font_bottoni)
        self.modifica_dipendente.clicked.connect(self.mostra_modifica_dipendente)
        self.h_layout.addWidget(self.modifica_dipendente)
        self.modifica_dipendente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco Dipendenti")
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

        for dipendente in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)



    def mostra_inserisci_dipendente(self):

        self.inserisci_dipendente = view_InserisciDipendente(self.controller, self.aggiorna_dati)
        self.inserisci_dipendente.show()



    def closeEvent(self, event):
        self.controller.save_data()



    def mostra_elimina_dipendente(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_dipendenti()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un dipendente da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Vuoi eliminare il dipendente?",QMessageBox.Yes, QMessageBox.No)

        if risposta == QMessageBox.Yes:

            self.controller.elimina_dipendente_by_id(da_eliminare.id)
            QMessageBox.about(self, "Eliminato", "Il dipendente è stato eliminato")
            self.aggiorna_dati()
        else:
            return




    def mostra_modifica_dipendente(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_dipendenti()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un dipendente da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.modifica_dipendente = view_ModificaDipendente(Controller_GestioneDipendenti(da_visualizzare),self.aggiorna_dati,self.controller.get_lista_dipendenti())
        self.modifica_dipendente.show()
