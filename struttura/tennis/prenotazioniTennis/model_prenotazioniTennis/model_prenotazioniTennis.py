class model_PrenotazioniTennis:

    def __init__(self,utente, dataselezionata, orario, recapito, id):
        self.utente = utente
        self.data = dataselezionata
        self.orario = orario
        self.recapito = recapito
        self.id = id

    def get_prezzo_totale(self):
        prezzo = 10
        return prezzo