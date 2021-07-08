from struttura.piscina.Iscritti.model_iscritti.model_iscritti import model_iscritti


class controller_iscritti():

    def __init__(self):
        super(controller_iscritti, self).__init__()
        self.model = model_iscritti()

    def aggiungi_utente(self, utente):
        self.model.aggiungi_utente(utente)

    def get_lista_iscritti(self):
        return self.model.get_lista_iscritti()

    def get_utente_by_codicefiscale(self, codicefiscale):
        return self.model.get_utente_by_codicefiscale(codicefiscale)

    def elimina_utente_by_codicefiscale(self, codicefiscale):
        self.model.elimina_utente_by_codicefiscale(codicefiscale)

    def save_data(self):
        self.model.save_data()
