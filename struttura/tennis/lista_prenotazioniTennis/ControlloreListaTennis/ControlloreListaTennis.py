from struttura.tennis.lista_prenotazioniTennis.ModelListaPrenotazioneTennis.model_listaPrenotazioneTennis import \
    ListaPrenotazioniTennis


class ControlloreListaPrenotazioniTennis:

    def __init__(self):
        self.model = ListaPrenotazioniTennis()

    def get_lista_prenotazioni_tennis1(self):
        return self.model.get_lista_prenotazioni1()

    def aggiungi_prenotazione_tennis(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)

    def elimina_prenotazione_tennis(self, idtennis):
        self.model.elimina_prenotazione_tennis(idtennis)

    def get_prenotazione_by_idtennis(self, idtennis):
        self.model.get_prenotazione_by_idtennis(idtennis)

    def get_lista_prenotazioni_tennis_by_day(self, data):
        self.model.get_lista_prenotazioni_tennis_by_day(data)

    def save_data(self):
        self.model.save_data()