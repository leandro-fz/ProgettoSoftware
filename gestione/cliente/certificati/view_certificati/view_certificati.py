from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.cliente.GestioneCertificati.controller_gestione_certificati.controller_gestione_certificati import \
    controller_gestione_certificati
from gestione.cliente.GestioneCertificati.view_modifica_certificati.view_modifica_certificati import \
    view_modifica_certificati
from gestione.cliente.abbonamenti.controller_abbonamenti.controller_abbonamenti import controller_abbonamenti
from gestione.cliente.certificati.controller_certificati.controller_certficati import controller_certificati
from gestione.cliente.certificati.view_certificati.view_inserisci_certificati import view_inserisci_certificati


class view_certificati(QWidget):

    # view generale di certificati collegata alle funzioni sottostanti
    def __init__(self, parent=None):
        super(view_certificati, self).__init__(parent)

        self.controller = controller_certificati()

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()

        self.font_label = QFont("Yu Gothic UI Light", 13)
        self.font_label.setBold(True)

        self.font_label2 = QFont("Yu Gothic UI Light", 13)
        self.label_alto = QLabel("Inserisci il certificato medico solo dopo aver inserito il cliente tra gli abbonamenti")
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)
        self.v_layout.addSpacing(10)

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

    #funzione che chiude la finestra
    def chiudi_schermata(self):
        self.close()

    #funzione che mostra all'utente i certificati inseriti attraverso una list view
    #la funzione fa ausilio del get_lista_abbonamenti, infatti tutti i certificati sono collegati a un utente inserito prima da "gestione abbonamenti"
    def aggiorna_dati(self):

        self.controlloreabbonamento = controller_abbonamenti()

        self.list_view_model = QStandardItemModel(self.list_view)

        self.font_item = QFont("Yu Gothic UI Light", 12)


        for certificato in self.controller.get_lista_certificati():
            for abbonamento in self.controlloreabbonamento.get_lista_abbonamenti():
                if certificato.codicefiscale == abbonamento.codicefiscale:
                    item = QStandardItem()
                    item.setText(abbonamento.nome + " " + abbonamento.cognome)
                    item.setEditable(False)
                    item.setFont(self.font_item)
                    self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    #funzione che richiama la view di insersci certificato per l'inserimento di un certificato
    def mostra_inserisci_certificato(self):

        self.inserisci_certificato = view_inserisci_certificati(self.controller, self.aggiorna_dati)
        self.inserisci_certificato.show()

    def closeEvent(self, event):
        self.controller.save_data()

    #elimina dalla lista il certificato selezionato in base al codice fiscale inserito in "gestione abbonamenti"
    def mostra_elimina_certificato(self):

        try:


            listcertificati = []
            index = self.list_view.selectedIndexes()[0].row()
            for certificato in self.controller.get_lista_certificati():
                for abbonamento in self.controlloreabbonamento.get_lista_abbonamenti():
                    if certificato.codicefiscale == abbonamento.codicefiscale:
                        listcertificati.append(certificato)
            da_eliminare = listcertificati[index]

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

    #richiama la view di modifica certificato per modificare il certificato, avvalendosi dei dati inseriti in "gestione abbonamenti"
    def mostra_modifica_certificato(self):

        try:
            listacertificati = []
            index = self.list_view.selectedIndexes()[0].row()
            for certificato in self.controller.get_lista_certificati():
                for abbonamento in self.controlloreabbonamento.get_lista_abbonamenti():
                    if certificato.codicefiscale == abbonamento.codicefiscale:
                        listacertificati.append(certificato)
            da_visualizzare = listacertificati[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un certificato da visualizzare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        self.modifica_certificato = view_modifica_certificati(controller_gestione_certificati(da_visualizzare),
                                                           self.aggiorna_dati, self.controller.get_lista_certificati())
        self.modifica_certificato.show()
