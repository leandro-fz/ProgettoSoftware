import os
import pickle

# amministrazione/
class Insieme_Dipendenti():
    def __init__(self):
        super(Insieme_Dipendenti, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile("gestione/amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle"):
            with open("gestione/amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle", "rb") as file:
                try:
                    self.lista_dipendenti = pickle.load(file)
                except EOFError:
                    return

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def elimina_dipendente_by_id(self, id):
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
        if os.path.isfile("gestione/amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle"):
            with open("gestione/amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)

