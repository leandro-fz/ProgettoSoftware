import os
import pickle

# cliente/
class Insieme_Abbonamenti():
    def __init__(self):
        super(Insieme_Abbonamenti, self).__init__()
        self.lista_abbonamenti = []
        if os.path.isfile("gestione/cliente/abbonamenti/data_abbonamenti/lista_abbonamenti_salvata.pickle"):
            with open("gestione/cliente/abbonamenti/data_abbonamenti/lista_abbonamenti_salvata.pickle", "rb") as file:
                try:
                    self.lista_abbonamenti = pickle.load(file)
                except EOFError:
                    return


    def aggiungi_abbonamento(self, abbonamento):
        self.lista_abbonamenti.append(abbonamento)

    def elimina_abbonamento_by_codicefiscale(self, codicefiscale):
        for abbonamento in self.lista_abbonamenti:
            if abbonamento.codicefiscale == codicefiscale:
                self.lista_abbonamenti.remove(abbonamento)
                return True
        return False

    def get_lista_abbonamenti(self):
        return self.lista_abbonamenti

    def get_abbonamento_by_codicefiscale(self, codicefiscale):
        for abbonamento in self.lista_abbonamenti:
            if abbonamento.codicefiscale == codicefiscale:
                return abbonamento
        return None

    def save_data(self):
        if os.path.isfile("gestione/cliente/abbonamenti/data_abbonamenti/lista_abbonamenti_salvata.pickle"):
            with open("gestione/cliente/abbonamenti/data_abbonamenti/lista_abbonamenti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_abbonamenti, handle, pickle.HIGHEST_PROTOCOL)