from struttura.piscina.corsi.GestioneCorsiPiscina.model_gestione_corsi_piscina.model_gestione_corsi_piscina import \
    model_gestione_corsi_piscina


class controller_gestione_corsi_piscina:

    def __init__(self):
        self.model = model_gestione_corsi_piscina()

    def get_lista_corsi(self):
        return self.model.get_lista_corsi()

    def aggiungi_corso(self, corso):
        self.model.aggiungi_corso(corso)

    def elimina_corso_piscina(self, corso):
        self.model.elimina_corso_piscina(corso)

    def get_corso_by_idcorso(self, corso):
        self.model.get_corso_by_idcorso(corso)

    def save_data(self):
        self.model.save_data()