import os
import pickle

# amministrazione/
class Insieme_Inventario():
    def __init__(self):
        super(Insieme_Inventario, self).__init__()
        self.lista_inventario = []
        # print("ok")
        # k = os.path.isfile("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle")
        # print(k)
        if os.path.isfile("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle"):
            # print("ok2")
            with open("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle", "rb") as file:
                # print("file recuperato")
                self.lista_inventario = pickle.load(file)
                print("file recuperato2")

    def aggiungi_inventario(self, inventario):
        self.lista_inventario.append(inventario)

    def rimuovi_inventario_by_id(self, id):
        for inventario in self.lista_inventario:
            if inventario.id == id:
                self.lista_inventario.remove(inventario)
                return True
        return False

    def get_lista_inventario(self):
        return self.lista_inventario

    def get_inventario_by_id(self, id):
        for inventario in self.lista_inventario:
            if inventario.id == id:
                return inventario
        return None

    def save_data(self):
        if os.path.isfile("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle"):
            with open("gestione/amministrazione/inventario/data_inventario/lista_inventario_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_inventario, handle, pickle.HIGHEST_PROTOCOL)