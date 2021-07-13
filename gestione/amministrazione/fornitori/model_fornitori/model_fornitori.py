import os
import pickle

class model_fornitori():

    # nella funzione c'è il collegamento con il file "lista_fornitori_salvata" dove i fornitori e le varie informazioni verranno salvate
    def __init__(self):
        super(model_fornitori, self).__init__()
        self.lista_fornitori = []
        if os.path.isfile("gestione/amministrazione/fornitori/data_fornitori/lista_fornitori_salvata.pickle"):
            with open("gestione/amministrazione/fornitori/data_fornitori/lista_fornitori_salvata.pickle", "rb") as file:
                try:
                    self.lista_fornitori = pickle.load(file)
                except EOFError:
                    return

    # la funzione inserisce lil fornitore alla lista
    def aggiungi_fornitore(self, fornitore):
        self.lista_fornitori.append(fornitore)

    # la funzione elimina il fornitore dalla lista attraverso il campo "iva"
    def rimuovi_fornitore_by_iva(self, iva):
        for fornitore in self.lista_fornitori:
            if fornitore.iva== iva:
                self.lista_fornitori.remove(fornitore)
                return True
        return False

    # la funzione ridà la lista dei fornitori
    def get_lista_fornitori(self):
        return self.lista_fornitori

    # la funzione ridà la lista dei fornitori in base all'iva
    def get_fornitore_by_iva(self, iva):
        for fornitore in self.lista_fornitori:
            if fornitore.iva== iva:
                return fornitore
        return None

    # salva i dati dei fornitori inseriti
    def save_data(self):
        if os.path.isfile("gestione/amministrazione/fornitori/data_fornitori/lista_fornitori_salvata.pickle"):
            with open("gestione/amministrazione/fornitori/data_fornitori/lista_fornitori_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_fornitori, handle, pickle.HIGHEST_PROTOCOL)