from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from gestione.amministrazione.fornitori.controller_fornitori.controller_fornitori import controller_fornitori
from gestione.amministrazione.fornitori.view_fornitori.view_inserisci_fornitori import view_inserisci_fornitori

from gestione.amministrazione.GestioneFornitori.controller_gestione_fornitori.controller_gestione_fornitori import \
   controller_gestione_fornitori
from gestione.amministrazione.GestioneFornitori.view_modifica_fornitori.view_modifica_fornitori import \
   view_modifica_fornitori


class view_fornitori(QWidget):

    def __init__(self, parent=None):
        super(view_fornitori, self).__init__(parent)

        self.controller = controller_fornitori()

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

        self.inserisci_fornitore = QPushButton("Inserisci fornitore")
        self.inserisci_fornitore.clicked.connect(self.mostra_inserisci_fornitore)
        self.inserisci_fornitore.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.inserisci_fornitore)
        self.inserisci_fornitore.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.elimina_fornitore = QPushButton("Elimina fornitore")
        self.elimina_fornitore.setFont(self.font_bottoni)
        self.elimina_fornitore.clicked.connect(self.mostra_elimina_fornitore)
        self.h_layout.addWidget(self.elimina_fornitore)
        self.elimina_fornitore.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.modifica_fornitore = QPushButton("Modifica fornitore")
        self.modifica_fornitore.setFont(self.font_bottoni)
        self.modifica_fornitore.clicked.connect(self.mostra_modifica_fornitore)
        self.h_layout.addWidget(self.modifica_fornitore)
        self.modifica_fornitore.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco fornitori")
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

        for fornitore in self.controller.get_lista_fornitori():
            item = QStandardItem()
            item.setText(fornitore.nome )
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def mostra_inserisci_fornitore(self):

        self.inserisci_fornitore = view_inserisci_fornitori(self.controller, self.aggiorna_dati)
        self.inserisci_fornitore.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def mostra_elimina_fornitore(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_fornitori()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un fornitore da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Vuoi eliminare il fornitore?", QMessageBox.Yes,
                                        QMessageBox.No)

        if risposta == QMessageBox.Yes:

            self.controller.elimina_fornitore_by_iva(da_eliminare.iva)
            QMessageBox.about(self, "Eliminato", "Il fornitore è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    def mostra_modifica_fornitore(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_fornitori()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un fornitore da visualizzare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        self.modifica_fornitore = view_modifica_fornitori(controller_gestione_fornitori(da_visualizzare),
                                                           self.aggiorna_dati, self.controller.get_lista_fornitori())
        self.modifica_fornitore.show()

