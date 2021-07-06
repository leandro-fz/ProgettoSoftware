from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class view_modifica_articolo(QWidget):

    def __init__(self, controllore_inventario, aggiorna_lista, lista_inventario, parent=None):

        super(view_modifica_articolo, self).__init__(parent)
        self.controller = controllore_inventario
        self.aggiorna_lista = aggiorna_lista
        self.lista_inventario = lista_inventario

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Yu Gothic UI Light", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Yu Gothic UI Light", 16)

        self.label_articolo = QLabel("Articolo:")
        self.label_articolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_articolo)

        self.campo_articolo = QLineEdit()
        self.campo_articolo.setFont(self.font_campi)
        self.campo_articolo.setText(self.controller.get_articolo_inventario())
        self.v_layout.addWidget(self.campo_articolo)


        self.label_quantita = QLabel("Quantità:")
        self.label_quantita.setFont(self.font_label)
        self.v_layout.addWidget(self.label_quantita)

        self.campo_quantita = QLineEdit()
        self.campo_quantita.setFont(self.font_campi)
        self.campo_quantita.setText(str(self.controller.get_quantita_inventario()))
        self.v_layout.addWidget(self.campo_quantita)

        self.label_codice = QLabel("Codice articolo:")
        self.label_codice.setFont(self.font_label)
        self.v_layout.addWidget(self.label_codice)

        self.campo_codice = QLineEdit()
        self.campo_codice.setFont(self.font_campi)
        self.campo_codice.setText(str(self.controller.get_codice_inventario()))
        self.v_layout.addWidget(self.campo_codice)

        self.label_prezzo = QLabel("Prezzo:")
        self.label_prezzo.setFont(self.font_label)
        self.v_layout.addWcodiceget(self.label_prezzo)

        self.campo_prezzo = QLineEdit()
        self.campo_prezzo.setFont(self.font_campi)
        self.campo_prezzo.setText(str(self.controller.get_prezzo_inventario()))
        self.v_layout.addWidget(self.campo_prezzo)

        self.h_layout = QHBoxLayout()

        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.bottone_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_chiudi)

        self.bottone_modifica = QPushButton("Modifica")
        self.bottone_modifica.setFont(self.font_campi)
        self.bottone_modifica.clicked.connect(self.modifica_inventario)
        self.bottone_modifica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.h_layout.addWidget(self.bottone_modifica)
        self.shortcut_modifica = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_modifica.activated.connect(self.modifica_inventario)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Inventario")
        self.resize(300, 400)

        self.setLayout(self.v_layout)
        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


    def chiudi_finestra(self):
        self.close()

    def controlla_codice_libero(self, codice):

        for inventario in self.lista_inventario:
            if inventario.codice == codice:
                return False
        return True

    def modifica_inventario(self):

        articolo = self.campo_articolo.text()
        quantita = self.campo_quantita.text()
        codice = self.campo_codice.text()
        prezzo = self.campo_prezzo.text()

        if articolo == "" or quantita == "" or codice == "" or prezzo == "":

            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            codice = int(self.campo_codice.text())
        except:

            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il codice dell'articolo", QMessageBox.Ok, QMessageBox.Ok)
            return

        if codice <10000:

            QMessageBox.critical(self, "Errore", "Il codice deve avere almeno 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if codice > 99999:

            QMessageBox.critical(self, "Errore", "Il codice può avere al massimo 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.controller.get_codice_inventario() == codice:
            pass

        elif not self.controlla_codice_libero(codice):

            QMessageBox.critical(self, "Errore", "Articolo già inserito. Modifica la quantità", QMessageBox.Ok,QMessageBox.Ok)
            return

        try:
            prezzo = float(self.campo_prezzo.text())

        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri con il punto per il prezzo", QMessageBox.Ok,QMessageBox.Ok)
            return

        if prezzo <= 0:

            QMessageBox.critical(self, "Errore", "Il prezzo non può essere negativo", QMessageBox.Ok, QMessageBox.Ok)
            return


        self.controller.set_articolo_inventario(articolo)
        self.controller.set_quantita_inventario(quantita)
        self.controller.set_codice_inventario(codice)
        self.controller.set_prezzo_inventario(prezzo)

        QMessageBox.about(self, "Completata", "Modifica completata")
        self.aggiorna_lista()
        self.close()