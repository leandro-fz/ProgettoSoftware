import os
import pickle

class model_abbonamenti():

    #nella funzione c'è il collegamento con il file "lista_abbonamenti_salvata" dove gli abboanamenti e le varie informazioni verranno salvate
    def __init__(self):
        super(model_abbonamenti, self).__init__()
        self.lista_abbonamenti = []
        if os.path.isfile("gestione/cliente/abbonamenti/data_abbonamenti/lista_abbonamenti_salvata.pickle"):
            with open("gestione/cliente/abbonamenti/data_abbonamenti/lista_abbonamenti_salvata.pickle", "rb") as file:
                try:
                    self.lista_abbonamenti = pickle.load(file)
                except EOFError:
                    return

    # la funzione inserisce l'abbonamento alla lista
    def aggiungi_abbonamento(self, abbonamento):
        self.lista_abbonamenti.append(abbonamento)

    # la funzione elimina l'abbonamento dalla lista attraverso il campo "codicefiscale"
    def elimina_abbonamento_by_codicefiscale(self, codicefiscale):
        for abbonamento in self.lista_abbonamenti:
            if abbonamento.codicefiscale == codicefiscale:
                self.lista_abbonamenti.remove(abbonamento)
                return True
        return False

    # la funzione ridà la lista degli abbonamenti
    def get_lista_abbonamenti(self):
        return self.lista_abbonamenti

    def get_abbonamento_by_codicefiscale(self, codicefiscale):
        for abbonamento in self.lista_abbonamenti:
            if abbonamento.codicefiscale == codicefiscale:
                return abbonamento
        return None

    # salva i dati degli abbonamenti inseriti
    def save_data(self):
        if os.path.isfile("gestione/cliente/abbonamenti/data_abbonamenti/lista_abbonamenti_salvata.pickle"):
            with open("gestione/cliente/abbonamenti/data_abbonamenti/lista_abbonamenti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_abbonamenti, handle, pickle.HIGHEST_PROTOCOL)