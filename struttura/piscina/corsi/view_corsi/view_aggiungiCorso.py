from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt5.QtGui import QFont
from datetime import datetime, timedelta

from PyQt5 import QtGui, QtCore

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.piscina.corsi.corsiPiscina.modelPiscina.model_corsi_piscina import model_CorsiPiscina


class view_aggiungi_corso(QWidget):

    def __init__(self, data, controllore_gestionecorsipiscina, aggiorna_dati_corsi_piscina, parent=None):
        super(view_aggiungi_corso, self).__init__(parent)
        self.font = QFont("Yu Gothic UI Light", 15)
        self.aggiorna_dati_corsi_piscina = aggiorna_dati_corsi_piscina
        self.controllore = controllore_gestionecorsipiscina
        self.data1 = data


        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Yu Gothic UI Light", 15)
        self.font_label.setBold(True)

        self.font_label2 = QFont("Yu Gothic UI Light", 15)
        self.label_alto = QLabel("Form di prenotazione campo tennis del "+ self.data1.strftime("%d/%m/%Y"))
        self.label_alto.setFont(self.font_label2)
        self.v_layout.addWidget(self.label_alto)

        # self.v_layout.addSpacing(10)

        self.label_corso = QLabel("Corso:")
        self.label_corso.setFont(self.font_label)
        self.v_layout.addWidget(self.label_corso)

        self.campo_corso = QLineEdit()
        self.v_layout.addWidget(self.campo_corso)

        self.label_istruttore = QLabel("Istruttore:")
        self.label_istruttore.setFont(self.font_label)
        self.v_layout.addWidget(self.label_istruttore)

        self.campo_istruttore = QLineEdit()
        self.v_layout.addWidget(self.campo_istruttore)

        #orario
        self.label_orario = QLabel("Orario:")
        self.label_orario.setFont(self.font_label)
        self.v_layout.addWidget(self.label_orario)

        self.combo = QComboBox(self)
        self.combo.addItem("Seleziona un orario")
        self.combo.addItem("08:00-09:00")
        self.combo.addItem("09:00-10:00")
        self.combo.addItem("10:00-11:00")
        self.combo.addItem("11:00-12:00")
        self.combo.addItem("12:00-13:00")
        self.combo.addItem("13:00-14:00")
        self.combo.addItem("14:00-15:00")
        self.combo.addItem("15:00-16:00")
        self.combo.addItem("16:00-17:00")
        self.combo.addItem("17:00-18:00")
        self.combo.addItem("18:00-19:00")
        self.combo.addItem("19:00-20:00")
        self.combo.addItem("20:00-21:00")
        self.combo.addItem("21:00-22:00")
        self.combo.addItem("22:00-23:00")

        self.v_layout.addWidget(self.combo)

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
        self.bottone_conferma.clicked.connect(self.conferma_inserimento_corso_piscina)
        self.bottone_conferma.setFont(self.font_label)
        self.bottone_conferma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shortcut_conferma = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_conferma.activated.connect(self.conferma_inserimento_corso_piscina)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Corso Nuoto")
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
        reply = QMessageBox.question(self, 'Annullare', 'Sei sicuro di voler uscire?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            return


    def conferma_inserimento_corso_piscina(self):
        corso = self.campo_corso.text()
        istruttore = self.campo_istruttore.text()
        orario_premuto = str(self.combo.currentText())
        dataselezionata = self.data1
        idcorso = str(dataselezionata)+str(orario_premuto)

        if corso == "" or istruttore == "":
            QMessageBox.critical(self, "Errore", "Inserisci tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        if orario_premuto == "Seleziona un orario":
            QMessageBox.critical(self, "Errore", "Seleziona un orario valido ", QMessageBox.Ok, QMessageBox.Ok)
            return

        if not self.controlla_disponibilità(idcorso):
            QMessageBox.critical(self, "Conflitto", "Questa fascia oraria ha già un altro corso",QMessageBox.Ok, QMessageBox.Ok)
            return
        nuovocorso = model_CorsiPiscina(corso, istruttore, dataselezionata, orario_premuto, idcorso)

        self.controllore.aggiungi_corso(nuovocorso)
        self.controllore.save_data()
        QMessageBox.about(self, "Confermata", "Corso aggiunto")
        self.aggiorna_dati_corsi_piscina()
        self.close()
        return True

    def controlla_disponibilità(self, idcorso):
        for corso in self.controllore.get_lista_corsi():
            if corso.id == idcorso:
                return False
        return True