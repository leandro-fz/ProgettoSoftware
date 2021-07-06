from gestione.cliente.abbonamenti.model_abbonamenti.model_abbonamenti import model_abbonamenti


class controller_abbonamenti():

    def __init__(self):
        super(controller_abbonamenti, self).__init__()
        self.model = model_abbonamenti()

    def aggiungi_abbonamento(self, abbonamento):
        self.model.aggiungi_abbonamento(abbonamento)

    def get_lista_abbonamenti(self):
        return self.model.get_lista_abbonamenti()

    def get_abbonamento_by_codicefiscale(self, codicefiscale):
        return self.model.get_abbonamento_by_codicefiscale(codicefiscale)

    def elimina_abbonamento_by_codicefiscale(self, codicefiscale):
        self.model.elimina_abbonamento_by_codicefiscale(codicefiscale)

    def save_data(self):
        self.model.save_data()
