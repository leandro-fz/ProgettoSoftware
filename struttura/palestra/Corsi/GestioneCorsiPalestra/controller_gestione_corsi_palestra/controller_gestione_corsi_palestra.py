from struttura.palestra.Corsi.GestioneCorsiPalestra.model_gestione_corsi_palestra.model_gestione_corsi_palestra import \
    model_gestione_corsi_palestra

class controller_gestione_corsi_palestra:

    def __init__(self):
        self.model = model_gestione_corsi_palestra()

    def get_lista_corsi_palestra(self):
        return self.model.get_lista_corsi_palestra()

    def aggiungi_corso_palestra(self, corso):
        self.model.aggiungi_corso_palestra(corso)

    def elimina_corso_palestra(self, corso):
        self.model.elimina_corso_palestra(corso)

    def get_corso_palestra_by_idcorso(self, corso):
        self.model.get_corso_palestra_by_idcorso(corso)

    def save_data(self):
        self.model.save_data()