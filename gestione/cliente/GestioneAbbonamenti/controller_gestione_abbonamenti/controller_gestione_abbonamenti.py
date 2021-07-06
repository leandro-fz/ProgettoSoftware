class controller_gestione_abbonamenti():


    def __init__(self, abbonamento):
        self.model = abbonamento

    def get_nome_abbonamento(self):
        return self.model.nome

    def get_cognome_abbonamento(self):
        return self.model.cognome

    def get_nato_abbonamento(self):
        return self.model.nato

    def get_data_abbonamento(self):
        return self.model.data

    def get_codicefiscale_abbonamento(self):
        return self.model.codicefiscale

    def get_residenza_abbonamento(self):
        return self.model.residenza

    def get_email_abbonamento(self):
        return self.model.email

    def get_cellulare_abbonamento(self):
        return self.model.cellulare

    def get_struttura_abbonamento(self):
        return self.model.struttura

    def get_tipoabbonamento_abbonamento(self):
        return self.model.tipoabbonamento

    def set_nome_abbonamento(self, nome):
        self.model.nome = nome

    def set_cognome_abbonamento(self, cognome):
        self.model.cognome = cognome

    def set_nato_abbonamento(self, nato):
        self.model.nato = nato

    def set_data_abbonamento(self, data):
        self.model.data = data

    def set_codicefiscale_abbonamento(self, codicefiscale):
        self.model.codicefiscale = codicefiscale

    def set_residenza_abbonamento(self, residenza):
        self.model.residenza = residenza

    def set_email_abbonamento(self, email):
        self.model.email = email

    def set_cellulare_abbonamento(self, cellulare):
        self.model.cellulare = cellulare

    def set_struttura_abbonamento(self, struttura):
        self.model.struttura = struttura

    def set_tipoabbonamento_abbonamento(self, tipoabbonamento):
        self.model.tipoabbonamento = tipoabbonamento

