class Controller_GestioneIscritti():


    def __init__(self, utente):
        self.model = utente

    def get_nome_utente(self):
        return self.model.nome

    def get_cognome_utente(self):
        return self.model.cognome

    def get_nato_utente(self):
        return self.model.nato

    def get_data_utente(self):
        return self.model.data

    def get_codicefiscale_utente(self):
        return self.model.codicefiscale

    def get_residenza_utente(self):
        return self.model.residenza

    def get_email_utente(self):
        return self.model.email

    def get_cellulare_utente(self):
        return self.model.cellulare

    def set_nome_utente(self, nome):
        self.model.nome = nome

    def set_cognome_utente(self, cognome):
        self.model.cognome = cognome

    def set_nato_utente(self, nato):
        self.model.nato = nato

    def set_data_utente(self, data):
        self.model.data = data

    def set_codicefiscale_utente(self, codicefiscale):
        self.model.id = codicefiscale

    def set_residenza_utente(self, residenza):
        self.model.residenza = residenza

    def set_email_utente(self, email):
        self.model.email = email

    def set_cellulare_utente(self, cellulare):
        self.model.cellulare = cellulare