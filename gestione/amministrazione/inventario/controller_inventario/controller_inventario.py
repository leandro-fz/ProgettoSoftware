from gestione.amministrazione.inventario.model_inventario.model_inventario import model_inventario


class controller_inventario():

    def __init__(self):
        super(controller_inventario, self).__init__()
        self.model = model_inventario()

    def aggiungi_inventario(self, inventario):
        self.model.aggiungi_inventario(inventario)

    def get_lista_inventario(self):
        return self.model.get_lista_inventario()

    def get_inventario_by_codice(self, codice):
        return self.model.get_inventario_by_codice(codice)

    def elimina_inventario_by_codice(self, codice):
        self.model.rimuovi_inventario_by_codice(codice)

    def save_data(self):
        self.model.save_data()
