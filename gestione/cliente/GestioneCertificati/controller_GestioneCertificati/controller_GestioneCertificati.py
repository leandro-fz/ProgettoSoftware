class Controller_GestioneCertificati():


    def __init__(self, certificato):
        self.model = certificato

    def get_nome_certificato(self):
        return self.model.nome

    def get_cognome_certificato(self):
        return self.model.cognome

    def get_ruolo_certificato(self):
        return self.model.ruolo

    def get_id_certificato(self):
        return self.model.id

    def get_stipendio_certificato(self):
        return self.model.stipendio

    def set_nome_certificato(self, nome):
        self.model.nome = nome

    def set_cognome_certificato(self, cognome):
        self.model.cognome = cognome

    def set_ruolo_certificato(self, ruolo):
        self.model.ruolo = ruolo

    def set_id_certificato(self, id):
        self.model.id = id

    def set_stipendio_certificato(self, stipendio):
        self.model.stipendio = stipendio