import os
import pickle

# amministrazione/
class model_dipendenti():
    # nella funzione c'è il
    # collegamento con il file "lista_dipendenti_salvata" dove i dipendenti e le varie informazioni verranno salvate
    def __init__(self):
        super(model_dipendenti, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile("gestione/amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle"):
            with open("gestione/amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle", "rb") as file:
                try:
                    self.lista_dipendenti = pickle.load(file)
                except EOFError:
                    return

    # la funzione inserisce il dipendente alla lista
    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    # la funzione elimina il dipendente dalla lista attraverso il campo "id"
    def elimina_dipendente_by_id(self, id):
        for dipendente in self.lista_dipendenti:
            if dipendente.id == id:
                self.lista_dipendenti.remove(dipendente)
                return True
        return False

    # la funzione ridà la lista dei dipendnenti
    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    # la funzione ridà la lista dei dipendenti in base al id
    def get_dipendente_by_id(self, id):
        for dipendente in self.lista_dipendenti:
            if dipendente.id == id:
                return dipendente
        return None

    # salva i dati dei dipendenti inseriti
    def save_data(self):
        if os.path.isfile("gestione/amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle"):
            with open("gestione/amministrazione/dipendenti/data_dipendenti/lista_dipendenti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)

