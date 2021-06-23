from gestione.amministrazione.Inventario.model_inventario.model_inventario import Insieme_Inventario


class Controller_Inventario():

    def __init__(self):
        super(Controller_Inventario, self).__init__()
        self.model = Insieme_Inventario()

    def aggiungi_inventario(self, inventario):
        self.model.aggiungi_inventario(inventario)

    def get_lista_inventario(self):
        return self.model.get_lista_inventario()

    def get_inventario_by_id(self, id):
        return self.model.get_inventario_by_id(id)

    def elimina_inventario_by_id(self, id):
        self.model.rimuovi_inventario_by_id(id)

    def save_data(self):
        self.model.save_data()
