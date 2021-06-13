import os
import pickle


class Insieme_Dipendenti():


    def __init__(self):
        self.lista_dipendenti = []
        if os.path.isfile("amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle"):
            with open("amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle", "rb") as file:
                self.lista_dipendenti = pickle.load(file)

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def rimuovi_dipendente_by_id(self, id):

        for dipendente in self.lista_dipendenti:
            if dipendente.id == id:
                self.lista_dipendenti.remove(dipendente)
                return True
        return False

    def get_lista_dipendenti(self):

        return self.lista_dipendenti

    def get_dipendente_by_id(self, id):
        for dipendente in self.lista_dipendenti:
            if dipendente.id == id:
                return dipendente
        return None

    def save_data(self):
        if os.path.isfile("amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle"):
            with open("amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)