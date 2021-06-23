class Controller_GestioneInventario():


    def __init__(self, inventario):
        self.model = inventario

    def get_nome_inventario(self):
        return self.model.nome

    def get_cognome_inventario(self):
        return self.model.cognome

    def get_ruolo_inventario(self):
        return self.model.ruolo

    def get_id_inventario(self):
        return self.model.id

    def get_stipendio_inventario(self):
        return self.model.stipendio

    def set_nome_inventario(self, nome):
        self.model.nome = nome

    def set_cognome_inventario(self, cognome):
        self.model.cognome = cognome

    def set_ruolo_inventario(self, ruolo):
        self.model.ruolo = ruolo

    def set_id_inventario(self, id):
        self.model.id = id

    def set_stipendio_inventario(self, stipendio):
        self.model.stipendio = stipendio