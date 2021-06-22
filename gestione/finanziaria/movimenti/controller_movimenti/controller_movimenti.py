from gestione.finanziaria.movimenti.model_movimenti.model_movimenti import model_movimenti


class controller_movimenti():

    def __init__(self):
        super(controller_movimenti, self).__init__()
        self.model = model_movimenti()

    def aggiungi_movimenti(self, movimenti):
        self.model.aggiungi_movimenti(movimenti)

    def get_lista_movimenti(self):
        return self.model.get_lista_movimenti()

    def get_movimenti_by_id(self, id):
        return self.model.get_movimenti_by_id(id)

    def elimina_movimenti_by_id(self, id):
        self.model.rimuovi_movimenti_by_id(id)

    def save_data(self):
        self.model.save_data()
