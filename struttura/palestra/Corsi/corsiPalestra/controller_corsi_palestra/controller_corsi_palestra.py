class controller_corsi_palestra:

    def __init__(self, corso):
        self.model = corso

    def get_istruttore_corsiPalestra(self):
        return self.model.istruttore

    def get_corso_Palestra(self):
        return self.model.corso

    def get_orario_premuto_corsiPalestra(self):
        return self.model.orario

    def get_giorno_corsiPalestra(self):
        return self.model.data

    def get_id_corsiPalestra(self):
        return self.model.id
