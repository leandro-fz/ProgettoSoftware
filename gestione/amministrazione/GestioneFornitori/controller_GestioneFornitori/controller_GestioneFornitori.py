class Controller_GestioneFornitori():


    def __init__(self, fornitore):
        self.model = fornitore

    def get_ente_fornitore(self):
        return self.model.ente

    def get_data_fornitore(self):
        return self.model.data

    def get_articolo_fornitore(self):
        return self.model.articolo

    def get_codicearticolo_fornitore(self):
        return self.model.codicearticolo

    def get_quantita_fornitore(self):
        return self.model.quantita

    def get_iva_fornitore(self):
        return self.model.iva

    def set_ente_fornitore(self, ente):
        self.model.ente = ente

    def set_data_fornitore(self, data):
        self.model.data = data

    def set_articolo_fornitore(self, articolo):
        self.model.articolo = articolo

    def set_codicearticolo_fornitore(self, codicearticolo):
        self.model.codicearticolo = codicearticolo

    def set_quantita_fornitore(self, quantita):
        self.model.quantita = quantita

    def set_iva_fornitore(self, iva):
        self.model.iva = iva