from struttura.piscina.Iscritti.model_iscritti.model_iscritti import Insieme_Iscritti


class Controller_iscritti():

    def __init__(self):
        super(Controller_iscritti, self).__init__()
        self.model = Insieme_Iscritti()

    def aggiungi_utente(self, utente):
        self.model.aggiungi_utente(utente)

    def get_lista_iscritti(self):
        return self.model.get_lista_iscritti()

    def get_utente_by_id(self, id):
        return self.model.get_utente_by_id(id)

    def elimina_utente_by_id(self, id):
        self.model.rimuovi_utente_by_id(id)

    def save_data(self):
        self.model.save_data()
