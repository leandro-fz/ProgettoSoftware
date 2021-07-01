from struttura.tennis.lista_prenotazioniTennis.ModelListaPrenotazioneTennis.model_listaPrenotazioneTennis import \
    ListaPrenotazioniTennis


class ControlloreListaPrenotazioniTennis:

    def __init__(self):
        self.model = ListaPrenotazioniTennis()

    def get_lista_prenotazioni_tennis1(self):
        return self.model.get_lista_prenotazioni1()

    def aggiungi_prenotazione_tennis(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)

    def get_lista_prenotazioni_tennis(self):
        return self.model.get_lista_prenotazioni_cliente()
    #
    # def get_lista_prenotazione_cliente_oraria(self, data, ora):
    #     return self.model.get_lista_prenotazione_cliente_oraria(data, ora)

    def elimina_prenotazione_tennis(self, data):
        self.model.elimina_prenotazione_singola(data)

    def save_data(self):
        self.model.save_data()