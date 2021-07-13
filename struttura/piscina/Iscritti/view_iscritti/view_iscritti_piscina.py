from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.cliente.GestioneAbbonamenti.controller_gestione_abbonamenti.controller_gestione_abbonamenti import \
    controller_gestione_abbonamenti
from gestione.cliente.abbonamenti.controller_abbonamenti.controller_abbonamenti import controller_abbonamenti
from gestione.cliente.certificati.controller_certificati.controller_certficati import controller_certificati

from struttura.piscina.Iscritti.view_iscritti.view_visualizza_utente_piscina import view_visualizza_utente_piscina


class view_iscritti_piscina(QWidget):

    def __init__(self, parent=None):
        super(view_iscritti_piscina, self).__init__(parent)

        self.controllerAbbonamento = controller_abbonamenti()
        self.controllerCertificato = controller_certificati()

        self.v_layout = QVBoxLayout()

        self.label_iscritti_piscina = QLabel("Qui verranno visualizzati i clienti con abbonamento valido per la piscina e certificato medico inserito")
        self.label_iscritti_piscina.setFont(QFont("Yu Gothic UI Light", 10))
        self.v_layout.addWidget(self.label_iscritti_piscina)
        self.v_layout.addSpacing(10)

        self.list_view = QListView()

        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.font_bottoni = QFont("Yu Gothic UI Light", 12)

        #tasto indietro
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

        #tasto visualzza utente
        self.visualizza_utente = QPushButton("Visualizza utente")
        self.visualizza_utente.clicked.connect(self.mostra_visualizza_utente_piscina)
        self.visualizza_utente.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.visualizza_utente)
        self.visualizza_utente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shortcut_visualizza = QShortcut(QKeySequence('Return'), self)
        self.shortcut_visualizza.activated.connect(self.mostra_visualizza_utente_piscina)


        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco iscritti piscina")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/sfondonuotosfocato2.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.show()

    #funzione per la chisuura della pagina
    def chiudi_schermata(self):
        self.close()

    #list view in cui vengono visualizzati le persone che hanno un abbonamento per la piscina e un certificato medioc inserito
    def aggiorna_dati(self):

        self.list_view_model = QStandardItemModel(self.list_view)

        self.font_item = QFont("Yu Gothic UI Light", 12)
        # doppio ciclo for per controllare che un codice fiscale sia presente sia su certificati che su abbonamento
        # e che la struttura sia piscina
        for certificato in self.controllerCertificato.get_lista_certificati():
            for abbonamento in self.controllerAbbonamento.get_lista_abbonamenti():
                if certificato.codicefiscale == abbonamento.codicefiscale and abbonamento.struttura == "Piscina":
                    item = QStandardItem()
                    item.setText(abbonamento.nome + " " + abbonamento.cognome)
                    item.setEditable(False)
                    item.setFont(self.font_item)
                    self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    #funzione per visualizzare l'utente della piscina selezionato
    def mostra_visualizza_utente_piscina(self):
        try:
            index = self.list_view.selectedIndexes()[0].row()
            lista_iscritti_piscina_abbonamento = []
            #doppio ciclo for per controllare che un codice fiscale sia presente sia su certificati che su abbonamento
            # e che la struttura sia piscina
            for certificato in self.controllerCertificato.get_lista_certificati():
                for abbonamento in self.controllerAbbonamento.get_lista_abbonamenti():
                    if certificato.codicefiscale == abbonamento.codicefiscale and abbonamento.struttura == "Piscina":
                        lista_iscritti_piscina_abbonamento.append(abbonamento)

            da_visualizzareabbonamento = lista_iscritti_piscina_abbonamento[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un utente da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = view_visualizza_utente_piscina(controller_gestione_abbonamenti(da_visualizzareabbonamento))
        self.vista_prenotazione.show()

