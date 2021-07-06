import os
import pickle


class ListaPrenotazioniTennis():
    def __init__(self):
        self.lista_prenotazioni = []
        if os.path.isfile("struttura/tennis/lista_prenotazioniTennis/data_listaPrenotazioniTennis/lista_prenotazionitennis_salvata.pickle"):
            with open("struttura/tennis/lista_prenotazioniTennis/data_listaPrenotazioniTennis/lista_prenotazionitennis_salvata.pickle", "rb") as file:
                try:
                    self.lista_prenotazioni = pickle.load(file)
                    print("ok")
                except EOFError:
                    return

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    def get_lista_prenotazioni1(self):
        return self.lista_prenotazioni

    def get_lista_prenotazioni_tennis_by_day(self, data):
        lista_prenotazioni_tennis_by_day = []
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.data == data:
                lista_prenotazioni_tennis_by_day.append(prenotazione)
        return lista_prenotazioni_tennis_by_day


    def get_prenotazione_by_idtennis(self, idtennis):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.id== idtennis:
                return prenotazione
        return None

    def elimina_prenotazione_tennis(self, idtennis):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.id == idtennis:
                self.lista_prenotazioni.remove(prenotazione)
                return True
        return False

    def save_data(self):
        with open("struttura/tennis/lista_prenotazioniTennis/data_listaPrenotazioniTennis/lista_prenotazionitennis_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)