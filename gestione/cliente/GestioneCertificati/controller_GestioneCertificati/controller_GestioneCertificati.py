class Controller_GestioneCertificati():


    def __init__(self, certificato):
        self.model = certificato

    def get_nome_certificato(self):
        return self.model.nome

    def get_cognome_certificato(self):
        return self.model.cognome

    def get_nato_certificato(self):
        return self.model.nato

    def get_codicefiscale_certificato(self):
        return self.model.codicefiscale

    def get_residenza_certificato(self):
        return self.model.residenza

    def get_sportcertificato_certificato(self):
        return self.model.sportcertificato

    def get_datainizio_certificato(self):
        return self.model.datainizio

    def get_datafine_certificato(self):
        return self.model.datafine

    def set_nome_certificato(self, nome):
        self.model.nome = nome

    def set_cognome_certificato(self, cognome):
        self.model.cognome = cognome

    def set_nato_certificato(self, nato):
        self.model.nato = nato

    def set_codicefiscale_certificato(self, codicefiscale):
        self.model.id = codicefiscale

    def set_residenza_certificato(self, residenza):
        self.model.residenza = residenza

    def set_residenza_certificato(self, sportcertificato):
        self.model.sportcertificato = sportcertificato

    def set_datainizio_certificato(self, datainizio):
        self.model.datainizio = datainizio

    def set_datafine_certificato(self, datafine):
        self.model.datafine = datafine
