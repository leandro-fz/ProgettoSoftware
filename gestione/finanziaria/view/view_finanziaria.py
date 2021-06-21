from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.finanziaria.view.view_inserisci_movimento import view_inserisci_movimento


class view_finanziaria(QWidget):

    def __init__(self, parent=None):
        super(view_finanziaria, self).__init__(parent)


        # self.controller = Controller_Dipendenti()

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
        self.h_layout.addWidget(self.mostra_inserisci_movimento)
        self.inserisci_movimento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.elimina_movimento = QPushButton("Elimina movimento")
        self.elimina_movimento.setFont(self.font_bottoni)
        self.elimina_movimento.clicked.connect(self.elimina_movimento)
        self.h_layout.addWidget(self.elimina_movimento)
        self.elimina_movimento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.modifica_movimento = QPushButton("Modifica movimento")
        self.modifica_movimento.setFont(self.font_bottoni)
        self.modifica_movimento.clicked.connect(self.modifica_movimento)
        self.h_layout.addWidget(self.modifica_movimento)
        self.modifica_movimento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

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

        pass



    def mostra_inserisci_movimento(self):

        self.inserisci_movimento = view_inserisci_movimento(self.controller, self.aggiorna_dati)
        self.inserisci_movimento.show()



    def closeEvent(self, event):
        self.controller.save_data()



    def mostra_elimina_movimento(self):
        pass



    def mostra_modifica_movimento(self):
        pass