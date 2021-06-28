import os
import pickle

# amministrazione/
class Insieme_Inventario():
    def __init__(self):
        super(Insieme_Inventario, self).__init__()
        self.lista_inventario = []
        if os.path.isfile("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle"):
            with open("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle", "rb") as file:
                try:
                    self.lista_inventario = pickle.load(file)
                except EOFError:
                    return

    def aggiungi_inventario(self, inventario):
        self.lista_inventario.append(inventario)

    def rimuovi_inventario_by_id(self, codice):
        for inventario in self.lista_inventario:
            if inventario.codice == codice:
                self.lista_inventario.remove(inventario)
                return True
        return False

    def get_lista_inventario(self):
        return self.lista_inventario

    def get_inventario_by_id(self, codice):
        for inventario in self.lista_inventario:
            if inventario.codice == codice:
                return inventario
        return None

    def save_data(self):
        if os.path.isfile("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle"):
            with open("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_inventario, handle, pickle.HIGHEST_PROTOCOL)