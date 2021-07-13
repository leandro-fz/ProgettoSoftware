from  PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime

class view_modifica_movimenti(QWidget):

    def __init__(self, controllore_movimenti, aggiorna_lista, lista_movimenti, parent=None):

        super(view_modifica_movimenti, self).__init__(parent)
        self.controller = controllore_movimenti
        self.aggiorna_lista = aggiorna_lista
        self.lista_movimenti = lista_movimenti

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 16)

        self.label_importo = QLabel("Importo:")
        self.label_importo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_importo)

        self.campo_importo = QLineEdit()
        self.campo_importo.setFont(self.font_campi)
        self.campo_importo.setText(str(self.controller.get_importo_movimenti()))
        self.v_layout.addWidget(self.campo_importo)

        self.label_data = QLabel("Data (gg/mm/aaaa):")
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.campo_data = QLineEdit()
        self.campo_data.setFont(self.font_campi)
        self.stringa = str(self.controller.get_data_movimenti().strftime("%d/%m/%Y"))
        self.campo_data.setText(self.stringa)
        self.v_layout.addWidget(self.campo_data)

        self.label_causale = QLabel("Causale:")
        self.label_causale.setFont(self.font_label)
        self.v_layout.addWidget(self.label_causale)

        self.campo_causale = QLineEdit()
        self.campo_causale.setFont(self.font_campi)
        self.campo_causale.setText(self.controller.get_causale_movimenti())
        self.v_layout.addWidget(self.campo_causale)

        self.label_fattura = QLabel("Numero fattura:")
        self.label_fattura.setFont(self.font_label)
        self.v_layout.addWidget(self.label_fattura)

        self.campo_fattura = QLineEdit()
        self.campo_fattura.setFont(self.font_campi)
        self.campo_fattura.setText(str(self.controller.get_fattura_movimenti()))
        self.v_layout.addWidget(self.campo_fattura)

        self.h_layout = QHBoxLayout()

        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.bottone_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_chiudi)

        self.bottone_modifica = QPushButton("Modifica")
        self.bottone_modifica.setFont(self.font_campi)
        self.bottone_modifica.clicked.connect(self.modifica_movimenti)
        self.bottone_modifica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_modifica)
        self.shortcut_modifica = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_modifica.activated.connect(self.modifica_movimenti)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("movimenti")
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

    #poermette di chiudere la finestra di modifica del movimento
    def chiudi_finestra(self):
        self.close()

    #controlla se nel movimento modificato, la fattura modificata sia già esistente
    def controlla_fattura_libero(self, fattura):

        for movimento in self.lista_movimenti:
            if movimento.fattura == fattura:
                return False
        return True

    #dopo aver compilato la modifica, l'utente preme il pulsante "modifica" e la seguente funzione controlla se tutto è stato inserito correttamente
    # e se si, salva sul file
    def modifica_movimenti(self):

        importo = self.campo_importo.text()
        data = self.campo_data.text()
        causale = self.campo_causale.text()
        fattura = self.campo_fattura.text()

        if importo == "" or data == "" or causale == "" or fattura == " " :

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            importo = int(self.campo_importo.text())

        except:

            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per l'importo", QMessageBox.Ok, QMessageBox.Ok)
            return

        if importo == 0:

            QMessageBox.critical(self, "Errore", "L'importo non può essere nullo", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            data = datetime.strptime(data,"%d/%m/%Y")

        except:

            QMessageBox.critical(self, "Errore", "Inserisci il formato della data richiesto.", QMessageBox.Ok, QMessageBox.Ok)
            return


        self.controller.set_importo_movimenti(importo)
        self.controller.set_data_movimenti(data)
        self.controller.set_causale_movimenti(causale)
        self.controller.set_fattura_movimenti(fattura)

        QMessageBox.about(self, "Completata", "Modifica completata")
        # salva sulla lista la modifica
        self.aggiorna_lista()
        self.close()