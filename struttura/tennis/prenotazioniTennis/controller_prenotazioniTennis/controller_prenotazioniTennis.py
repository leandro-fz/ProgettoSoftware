class ControllorePrenotazioneTennis:

    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_prezzo_totale(self):
        return self.model.get_prezzo_totale

    def get_nome_pre_te(self):
        return self.model.utente

    def get_recapito_pre_te(self):
        return self.model.recapito

    def get_orario_premuto_pre_te(self):
        return self.model.orario

    def get_giorno_pre_te(self):
        return self.model.data

    def get_id_pre_te(self):
        return self.model.id

    def set_id_pre_te(self, id_pre_te):
        self.model.id = id_pre_te

    def set_nome_pre_te(self, utente):
        self.model.utente = utente

    def set_recapito_pre_te(self, recapito):
        self.model.recapito = recapito

    def set_orario_premuto_pre_te(self, orario):
        self.model.orario = orario

    def set_giorno_pre_te(self, giorno):
        self.model.data = giorno
