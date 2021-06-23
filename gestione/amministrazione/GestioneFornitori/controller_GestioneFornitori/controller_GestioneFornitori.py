class Controller_GestioneFornitori():


    def __init__(self, fornitore):
        self.model = fornitore

    def get_nome_fornitore(self):
        return self.model.nome

    def get_cognome_fornitore(self):
        return self.model.cognome

    def get_ruolo_fornitore(self):
        return self.model.ruolo

    def get_id_fornitore(self):
        return self.model.id

    def get_stipendio_fornitore(self):
        return self.model.stipendio

    def set_nome_fornitore(self, nome):
        self.model.nome = nome

    def set_cognome_fornitore(self, cognome):
        self.model.cognome = cognome

    def set_ruolo_fornitore(self, ruolo):
        self.model.ruolo = ruolo

    def set_id_fornitore(self, id):
        self.model.id = id

    def set_stipendio_fornitore(self, stipendio):
        self.model.stipendio = stipendio