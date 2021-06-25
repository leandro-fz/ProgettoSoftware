class ControllorePrenotazioneTennis:

    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_email_prenotazione(self):
        return self.model.email_cliente

    def get_data_inizio_prenotazione(self):
        return self.model.data_inizio

    def get_prezzo_totale(self):
        return self.model.get_prezzo_totale()