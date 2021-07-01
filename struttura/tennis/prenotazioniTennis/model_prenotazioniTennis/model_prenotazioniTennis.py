class model_PrenotazioniTennis:

    def __init__(self,utente, dataselezionata, orario, recapito):
        self.utente = utente
        self.data = dataselezionata
        self.orario = orario
        self.recapito = recapito

    def get_prezzo_totale(self):
        prezzo = 10
        return prezzo