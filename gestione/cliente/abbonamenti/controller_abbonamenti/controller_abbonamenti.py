from gestione.cliente.abbonamenti.model_abbonamenti.model_abbonamenti import Insieme_Abbonamenti


class Controller_Abbonamenti():

    def __init__(self):
        super(Controller_Abbonamenti, self).__init__()
        self.model = Insieme_Abbonamenti()

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
