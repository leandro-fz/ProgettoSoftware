class Controller_GestioneAbbonamenti():


    def __init__(self, abbonamento):
        self.model = abbonamento

    def get_nome_abbonamento(self):
        return self.model.nome

    def get_cognome_abbonamento(self):
        return self.model.cognome

    def get_ruolo_abbonamento(self):
        return self.model.ruolo

    def get_id_abbonamento(self):
        return self.model.id

    def get_stipendio_abbonamento(self):
        return self.model.stipendio

    def set_nome_abbonamento(self, nome):
        self.model.nome = nome

    def set_cognome_abbonamento(self, cognome):
        self.model.cognome = cognome

    def set_ruolo_abbonamento(self, ruolo):
        self.model.ruolo = ruolo

    def set_id_abbonamento(self, id):
        self.model.id = id

    def set_stipendio_abbonamento(self, stipendio):
        self.model.stipendio = stipendio