from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.amministrazione.dipendenti.controller_dipendenti.controller_dipendenti import ControlloreListaDipendenti


class Ui_gestionedipendente(QWidget):

    def __init__(self, parent=None):
        super(Ui_gestionedipendente, self).__init__(parent)

        self.controller = ControlloreListaDipendenti()

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.list_view.setGeometry(40, 60, 500, 401)
        # self.listView.setObjectName("listView")

        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.font_bottoni = QFont("Yu Gothic UI Light", 12)

        self.indietro = QPushButton("⬅️")
        self.indietro.resize(150,50)
        self.indietro.setFont(self.font_bottoni)
        self.indietro.clicked.connect(Ui_gestionedipendente.close)
        self.h_layout.addWidget(self.indietro)
        self.indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # self.indietro.setGeometry(QtCore.QRect(20, 20, 51, 31))
        # self.indietro.setIconSize(QtCore.QSize(40, 40))

        self.inserisci_dipendente = QPushButton("Inserisci Dipendente")
        self.inserisci_dipendente.clicked.connect(self.mostra_inserisci_dipendente)
        self.inserisci_dipendente.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.inserisci_dipendente)
        self.inserisci_dipendente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.elimina_dipendente = QPushButton("Elimina Dipendente")
        self.elimina_dipendente.setFont(self.font_bottoni)
        self.elimina_dipendente.clicked.connect(self.mostra_elimina_dipendente)
        self.h_layout.addWidget(self.elimina_dipendente)
        self.indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.modifica_dipendente = QPushButton("Modifica Dipendente")
        self.modifica_dipendente.setFont(self.font_bottoni)
        self.modifica_dipendente.clicked.connect(self.mostra_modifica_dipendente)
        self.h_layout.addWidget(self.modifica_dipendente)
        self.indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        # self.setStyleSheet(QWidget(background-image:url(.images/immaginepesisfocata.jpeg))
        # self.resize(781, 500)
        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Lista Dipendenti")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        self.show()

    def aggiorna_dati(self):
        self.list_view_model = QStandardItemModel(self.list_view)

        self.font_item = QFont("Arial", 16)

        for dipendente in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)


    def mostra_inserisci_dipendente(self):
        self.inserisci_dipendente = VistaInserisciDipendente(self.controller, self.aggiorna_dati)
        self.inserisci_dipendente.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def mostra_elimina_dipendente(self):
        try:
            indice = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_dipendenti()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona il dipendente da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Sei sicuro di volere eliminare il dipendente?",
                                        QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controller.elimina_dipendente_by_id(da_eliminare.id)
            QMessageBox.about(self, "Eliminato", "Il dipendente è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    def mostra_modifica_dipendente(self):
        try:
            indice = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_dipendenti()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona il dipendente da visualizzare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return
        self.modifica_dipendente = VistaModificaDipendente(ControlloreDipendente(da_visualizzare),
                                                                 self.aggiorna_dati,
                                                                 self.controller.get_lista_dipendenti())
        self.modifica_dipendente.show()
