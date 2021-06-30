class Controller_GestioneDipendenti():


    def __init__(self, dipendente):
        self.model = dipendente

    def get_nome_dipendente(self):
        return self.model.nome

    def get_cognome_dipendente(self):
        return self.model.cognome

    def get_luogo_dipendente(self):
        return self.model.luogo

    def get_data_dipendente(self):
        return self.model.data

    def get_codice_dipendente(self):
        return self.model.codice

    def get_contratto_dipendente(self):
        return self.model.contratto

    def get_ruolo_dipendente(self):
        return self.model.ruolo

    def get_id_dipendente(self):
        return self.model.id

    def get_stipendio_dipendente(self):
        return self.model.stipendio

    def set_nome_dipendente(self, nome):
        self.model.nome = nome

    def set_cognome_dipendente(self, cognome):
        self.model.cognome = cognome

    def set_luogo_dipendente(self, luogo):
        self.model.luogo = luogo

    def set_data_dipendente(self, data):
        self.model.data = data

    def set_codice_dipendente(self, codice):
        self.model.codice = codice

    def set_contratto_dipendente(self, contratto):
        self.model.contratto = contratto

    def set_ruolo_dipendente(self, ruolo):
        self.model.ruolo = ruolo

    def set_id_dipendente(self, id):
        self.model.id = id

    def set_stipendio_dipendente(self, stipendio):
        self.model.stipendio = stipendio