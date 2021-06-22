from gestione.cliente.abbonamenti.model_abbonamenti.model_abbonamenti import Insieme_Abbonamenti


class Controller_Abbonamenti():

    def __init__(self):
        super(Controller_Abbonamenti, self).__init__()
        self.model = Insieme_Abbonamenti()

    def aggiungi_abbonamento(self, abbonamento):
        self.model.aggiungi_abbonamento(abbonamento)

    def get_lista_abbonamenti(self):
        return self.model.get_lista_abbonamenti()

    def get_abbonamento_by_id(self, id):
        return self.model.get_abbonamento_by_id(id)

    def elimina_abbonamento_by_id(self, id):
        self.model.rimuovi_abbonamento_by_id(id)

    def save_data(self):
        self.model.save_data()
