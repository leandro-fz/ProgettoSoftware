import os
import pickle

# amministrazione/
class Insieme_Fornitori():
    def __init__(self):
        super(Insieme_Fornitori, self).__init__()
        self.lista_fornitori = []
        if os.path.isfile("gestione/amministrazione/fornitori/data_fornitori/lista_fornitori_salvata.pickle"):
            with open("gestione/amministrazione/fornitori/data_fornitori/lista_fornitori_salvata.pickle", "rb") as file:
                try:
                    self.lista_fornitori = pickle.load(file)
                except EOFError:
                    return

    def aggiungi_fornitore(self, fornitore):
        self.lista_fornitori.append(fornitore)

    def rimuovi_fornitore_by_iva(self, iva):
        for fornitore in self.lista_fornitori:
            if fornitore.iva== iva:
                self.lista_fornitori.remove(fornitore)
                return True
        return False

    def get_lista_fornitori(self):
        return self.lista_fornitori

    def get_fornitore_by_iva(self, iva):
        for fornitore in self.lista_fornitori:
            if fornitore.iva== iva:
                return fornitore
        return None

    def save_data(self):
        if os.path.isfile("gestione/amministrazione/fornitori/data_fornitori/lista_fornitori_salvata.pickle"):
            with open("gestione/amministrazione/fornitori/data_fornitori/lista_fornitori_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_fornitori, handle, pickle.HIGHEST_PROTOCOL)