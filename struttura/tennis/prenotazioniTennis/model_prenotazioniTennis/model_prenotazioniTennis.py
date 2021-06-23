import os
import pickle


class model_prenotaioniTennis():

    def __init__(self):
        self.lista_prenotazioniTennis = []
        if os.path.isfile("ListaPrenotazioni/data/lista_prenotazioniTennis_salvata.pickle"):
            with open("ListaPrenotazioni/data/lista_prenotazioniTennis_salvata.pickle", "rb") as file:
                self.lista_prenotazioniTennis = pickle.load(file)

    def aggiungi_prenotazioneTennis(self, prenotazione):
        self.lista_prenotazioniTennis.append(prenotazione)
        self.lista_prenotazioniTennis.sort()


    def get_lista_prenotazioniTennis(self, email):
        lista_ritorno = []
        for prenotazione in self.lista_prenotazioniTennis:
            if prenotazione.email_cliente == email:
                lista_ritorno.append(prenotazione)
        return lista_ritorno

    def get_lista_prenotazioneTennis(self):
        return self.lista_prenotazioniTennis


    def elimina_prenotazioneTennis(self, email, data_inizio):
        for prenotazione in self.lista_prenotazioniTennis:
            if prenotazione.email_cliente == email and prenotazione.data_inizio == data_inizio:
                self.lista_prenotazioniTennis.remove(prenotazione)
                return

    def save_data(self):
        with open("ListaPrenotazioni/data/lista_prenotazioniTennis_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_prenotazioniTennis, handle, pickle.HIGHEST_PROTOCOL)