class controller_corsi_piscina:

    def __init__(self, corso):
        self.model = corso

    def get_istruttore_corsiPalestra(self):
        return self.model.istruttore

    def get_corso_Palestra(self):
        return self.model.corso

    def get_orario_premuto_corsiPalestra(self):
        return self.model.orario

    def get_giorno__corsiPalestra(self):
        return self.model.data

    def get_id__corsiPalestra(self):
        return self.model.id

    def set_istruttore_corsiPiscina(self, istruttore):
        self.model.istruttore = istruttore

    def set_nome_pre_te(self, utente):
        self.model.utente = utente

    def set_orario_premuto_pre_te(self, orario):
        self.model.orario = orario

    def set_giorno_pre_te(self, giorno):
        self.model.data = giorno
