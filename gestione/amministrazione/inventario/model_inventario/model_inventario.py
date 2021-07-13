import os
import pickle

class model_inventario():

    # nella funzione c'è il collegamento con il file "lista_inventario_salvata" dove gli articoli e le varie informazioni verranno salvate
    def __init__(self):
        super(model_inventario, self).__init__()
        self.lista_inventario = []
        if os.path.isfile("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle"):
            with open("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle", "rb") as file:
                try:
                    self.lista_inventario = pickle.load(file)
                except EOFError:
                    return

    # la funzione inserisce l'articolo alla lista
    def aggiungi_inventario(self, inventario):
        self.lista_inventario.append(inventario)

    # la funzione elimina l'articolo dalla lista attraverso il campo "codice"
    def rimuovi_inventario_by_codice(self, codice):
        for inventario in self.lista_inventario:
            if inventario.codice == codice:
                self.lista_inventario.remove(inventario)
                return True
        return False

    # la funzione ridà la lista degli articoli
    def get_lista_inventario(self):
        return self.lista_inventario

    # la funzione ridà la lista degli articoli in base al codice
    def get_inventario_by_codice(self, codice):
        for inventario in self.lista_inventario:
            if inventario.codice == codice:
                return inventario
        return None

    # salva i dati degli articoli inseriti
    def save_data(self):
        if os.path.isfile("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle"):
            with open("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_inventario, handle, pickle.HIGHEST_PROTOCOL)