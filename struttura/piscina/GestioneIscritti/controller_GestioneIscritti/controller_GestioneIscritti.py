class Controller_GestioneIscritti():


    def __init__(self, utente):
        self.model = utente

    def get_nome_utente(self):
        return self.model.nome

    def get_cognome_utente(self):
        return self.model.cognome

    def get_ruolo_utente(self):
        return self.model.ruolo

    def get_id_utente(self):
        return self.model.id

    def get_stipendio_utente(self):
        return self.model.stipendio

    def set_nome_utente(self, nome):
        self.model.nome = nome

    def set_cognome_utente(self, cognome):
        self.model.cognome = cognome

    def set_ruolo_utente(self, ruolo):
        self.model.ruolo = ruolo

    def set_id_utente(self, id):
        self.model.id = id

    def set_stipendio_utente(self, stipendio):
        self.model.stipendio = stipendio