from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QHBoxLayout
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem

# Prenotazione/views/VistaPrenotazione/
class VistaPrenotazioneTennis(QWidget):
    pass

    # def __init__(self, controllore_prenotazione, parent=None):
    #     super(VistaPrenotazioneTennis, self).__init__(parent)
    #     self.controllore_prenotazione = controllore_prenotazione
    #     self.font_label = QFont("Arial", 14)
    #
    #     self.v_layout = QVBoxLayout()

        # labels
    #     self.create_label("Email: ", self.controllore_prenotazione.get())
    #     self.create_label("Periodo: ", self.controllore_prenotazione.get_data_inizio_prenotazione().strftime('%d/%m/%Y')
    #                             + " - " + self.controllore_prenotazione.get_data_fine_prenotazione().strftime('%d/%m/%Y'))
    #     self.create_label("Servizio ristorazione: ", self.controllore_prenotazione.get_servizio_ristorazione().nome)
    #     self.create_label("Servizio alloggio: ", self.controllore_prenotazione.get_servizio_alloggio().nome)
    #     #self.create_label("Numero di persone: ", self.controllore_prenotazione.get_servizio_alloggio().numero_persone_max)
    #
    #     # label servizi aggiuntivi
    #
    #     self.v_layout.addSpacing(20)
    #
    #     self.setLayout(self.v_layout)
    #     self.setWindowTitle("Prenotazione")
    #     self.resize(800, 500)
    #
    # def create_label(self, testo, text_label):
    #     h_layout = QHBoxLayout()
    #
    #     label = QLabel(testo)
    #     h_layout.addWidget(label)
    #
    #     label_di_testo = QLabel(text_label)
    #     label_di_testo.setFont(self.font_label)
    #     h_layout.addWidget(label_di_testo)
    #
    #     self.v_layout.addLayout(h_layout)
    #     self.v_layout.addSpacing(20)
