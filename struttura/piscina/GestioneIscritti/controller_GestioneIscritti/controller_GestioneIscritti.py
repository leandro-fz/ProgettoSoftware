class Controller_GestioneIscritti():


    def __init__(self, utente):
        self.model = utente

    def get_nome_utente(self):
        return self.model.nome

    def get_cognome_utente(self):
        return self.model.cognome

    def get_codicefiscale_utente(self):
        return self.model.codicefiscale

    def get_cellulare_utente(self):
        return self.model.cellulare

    def get_certificato_utente(self):
        return self.model.certificato

    def get_certificatoagonistico_utente(self):
        return self.model.certificatoagonistico

    def get_tipoabbonamento_utente(self):
        return self.model.tipoabbonamento

    def set_nome_utente(self, nome):
        self.model.nome = nome

    def set_cognome_utente(self, cognome):
        self.model.cognome = cognome

    def set_codicefiscale_utente(self, codicefiscale):
        self.model.id = codicefiscale

    def set_cellulare_utente(self, cellulare):
        self.model.cellulare = cellulare

    def set_certificato_utente(self, certificato):
        self.model.certificato = certificato

    def set_tipoabbonamento_utente(self, tipoabbonamento):
        self.model.tipoabbonamento = tipoabbonamento

    def set_certificatoagonistico_utente(self, certificatoagonistico):
        self.model.certificatoagonistico = certificatoagonistico