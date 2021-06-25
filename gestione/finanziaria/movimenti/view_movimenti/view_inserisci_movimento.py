from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime

from gestione.finanziaria.gestione_movimenti.controller_gestione_movimenti.controller_gestione_movimenti import \
    Controller_GestioneMovimenti
from gestione.finanziaria.gestione_movimenti.model_gestione_movimenti.model_gestione_movimenti import GestioneMovimenti


class view_InserisciMovimenti(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):

        super(view_InserisciMovimenti, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 15)
        self.font_label.setBold(True)


        self.font_label2 = QFont("Yu Gothic UI Light", 20)
        self.label_alto = QLabel("Compila il form di inserimento del movimento")
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)

        # self.v_layout.addSpacing(10)

        self.label_importo = QLabel("Importo")
        self.label_importo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_importo)

        self.campo_importo = QLineEdit()
        self.v_layout.addWidget(self.campo_importo)

        self.label_data = QLabel("Data (gg/mm/aaaa)")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.campo_data = QLineEdit()
        self.v_layout.addWidget(self.campo_data)

        self.label_causale = QLabel("Causale")
        self.label_causale.setFont(self.font_label)
        self.v_layout.addWidget(self.label_causale)

        self.campo_causale = QLineEdit()
        self.v_layout.addWidget(self.campo_causale)

        self.label_fattura = QLabel("Numero fattura")
        self.label_fattura.setFont(self.font_label)
        self.v_layout.addWidget(self.label_fattura)

        self.campo_fattura = QLineEdit()
        self.v_layout.addWidget(self.campo_fattura)

        self.v_layout.addSpacing(10)
        self.font_label.setBold(False)

        self.h_layout = QHBoxLayout()

        self.bottone_annulla = QPushButton("Annulla")
        self.bottone_annulla.setFont(self.font_label)
        self.bottone_annulla.clicked.connect(self.mostra_annulla_ins)
        self.h_layout.addWidget(self.bottone_annulla)
        self.bottone_annulla.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.bottone_conferma = QPushButton("Conferma")
        self.h_layout.addWidget(self.bottone_conferma)
        self.bottone_conferma.clicked.connect(self.conferma_inserimento)
        self.bottone_conferma.setFont(self.font_label)
        self.bottone_conferma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shortcut_conferma = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_conferma.activated.connect(self.conferma_inserimento)



        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserimento movimento")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def mostra_annulla_ins(self):
        reply = QMessageBox.question(self, 'Annullare', 'Sei sicuro di voler uscire?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass


    def conferma_inserimento(self):

        importo = self.campo_importo.text()
        data = self.campo_data.text()
        causale = self.campo_causale.text()
        fattura = self.campo_fattura.text()


        if importo == "" or data == "" or causale == "" or fattura == " ":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:

            importo= int(self.campo_importo.text())
        except:

            QMessageBox.critical(self, "Errore", "Importo non può avere lettere", QMessageBox.Ok, QMessageBox.Ok)
            return

        if importo <= 0:

            QMessageBox.critical(self, "Errore", "L'importo non può essere negativo o nullo", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            data = datetime.strptime(data,"%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto", QMessageBox.Ok, QMessageBox.Ok)


        self.controller.aggiungi_movimenti(GestioneMovimenti(importo, data, causale, fattura))
        self.controller.save_data()

        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))
        QMessageBox.about(self, "Completato", "Inserimento completato")
        self.aggiorna_lista()
        self.close()

    def controlla_fattura_libero(self, fattura):

            for movimento in self.controller.get_lista_movimenti():
                if movimento.fattura == fattura:
                    return False
            return True
