class controller_gestione_fornitori():


    def __init__(self, fornitore):
        self.model = fornitore

    def get_nome_fornitore(self):
        return self.model.nome

    def get_indirizzo_fornitore(self):
        return self.model.indirizzo

    def get_citta_fornitore(self):
        return self.model.citta

    def get_email_fornitore(self):
        return self.model.email

    def get_cellulare_fornitore(self):
        return self.model.cellulare

    def get_iva_fornitore(self):
        return self.model.iva

    def set_nome_fornitore(self, nome):
        self.model.nome = nome

    def set_indirizzo_fornitore(self, indirizzo):
        self.model.indirizzo = indirizzo

    def set_citta_fornitore(self, citta):
        self.model.citta = citta

    def set_email_fornitore(self, email):
        self.model.email = email

    def set_cellulare_fornitore(self, cellulare):
        self.model.cellulare = cellulare

    def set_iva_fornitore(self, iva):
        self.model.iva = iva