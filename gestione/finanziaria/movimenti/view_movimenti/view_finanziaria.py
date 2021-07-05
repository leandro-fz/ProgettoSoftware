from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.finanziaria.gestione_movimenti.controller_gestione_movimenti.controller_gestione_movimenti import \
    controller_gestione_movimenti
from gestione.finanziaria.gestione_movimenti.view_gestione_movimenti.view_gestione_movimenti import \
    view_gestione_movimenti
from gestione.finanziaria.movimenti.controller_movimenti.controller_movimenti import controller_movimenti
from gestione.finanziaria.movimenti.view_movimenti.view_inserisci_movimento import view_inserisci_movimento


class view_finanziaria(QWidget):

    def __init__(self, parent=None):
        super(view_finanziaria, self).__init__(parent)

        self.controller = controller_movimenti()

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

        self.inserisci_movimento = QPushButton("Inserisci movimento")
        self.inserisci_movimento.clicked.connect(self.mostra_inserisci_movimento)
        self.inserisci_movimento.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.inserisci_movimento)
        self.inserisci_movimento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.elimina_movimento = QPushButton("Elimina movimento")
        self.elimina_movimento.setFont(self.font_bottoni)
        self.elimina_movimento.clicked.connect(self.mostra_elimina_movimento)
        self.h_layout.addWidget(self.elimina_movimento)
        self.elimina_movimento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.modifica_movimento = QPushButton("Modifica movimento")
        self.modifica_movimento.setFont(self.font_bottoni)
        self.modifica_movimento.clicked.connect(self.mostra_modifica_movimento)
        self.h_layout.addWidget(self.modifica_movimento)
        self.modifica_movimento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco movimenti")
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

        for movimento in self.controller.get_lista_movimenti():
            item = QStandardItem()
            item.setText((str(movimento.importo) + " " + movimento.causale))
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def mostra_inserisci_movimento(self):

        self.inserisci_movimento = view_inserisci_movimento(self.controller, self.aggiorna_dati)
        self.inserisci_movimento.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def mostra_elimina_movimento(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_movimenti()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un movimento da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Vuoi eliminare il movimento?", QMessageBox.Yes,
                                        QMessageBox.No)

        if risposta == QMessageBox.Yes:

            self.controller.rimuovi_movimenti_by_fattura(da_eliminare.fattura)
            QMessageBox.about(self, "Eliminato", "Il movimento è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    def mostra_modifica_movimento(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_movimenti()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un movimento da visualizzare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        self.modifica_movimenti = view_gestione_movimenti(controller_gestione_movimenti(da_visualizzare),
                                                           self.aggiorna_dati, self.controller.get_lista_movimenti())
        self.modifica_movimenti.show()
