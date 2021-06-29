class Controller_GestioneInventario():


    def __init__(self, inventario):
        self.model = inventario

    def get_articolo_inventario(self):
        return self.model.articolo

    def get_quantita_inventario(self):
        return self.model.quantita

    def get_codice_inventario(self):
        return self.model.codice

    def get_prezzo_inventario(self):
        return self.model.prezzo

    def set_articolo_inventario(self, articolo):
        self.model.articolo = articolo

    def set_quantita_inventario(self, quantita):
        self.model.quantita = quantita

    def set_codice_inventario(self, codice):
        self.model.codice = codice

    def set_prezzo_inventario(self, prezzo):
        self.model.prezzo = prezzo
