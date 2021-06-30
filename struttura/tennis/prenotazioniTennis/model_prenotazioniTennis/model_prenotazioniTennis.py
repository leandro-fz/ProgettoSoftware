class model_PrenotazioniTennis:

    def __init__(self,utente, dataselezionata, orario_premuto, recapito):
        self.utente=utente
        self.data = dataselezionata
        self.ora = orario_premuto
        self.recapito = recapito
        # self.numeroUtenti = numero

    def get_prezzo_totale(self):
        prezzo = 10
        return prezzo