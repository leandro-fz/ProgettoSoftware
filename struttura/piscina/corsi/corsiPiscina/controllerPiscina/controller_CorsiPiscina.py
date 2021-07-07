class controller_CorsiPiscina:

    def __init__(self, corso):
        self.model = corso

    def get_istruttore_corsiPiscina(self):
        return self.model.istruttore

    def get_corso_Piscina(self):
        return self.model.corso

    def get_orario_premuto_corsiPiscina(self):
        return self.model.orario

    def get_giorno__corsiPiscina(self):
        return self.model.data

    def get_id__corsiPiscina(self):
        return self.model.id

    def set_id_pre_te(self, id_pre_te):
        self.model.id = id_pre_te

    def set_istruttore_corsiPiscina(self, istruttore):
        self.model.istruttore = istruttore

    def set_nome_pre_te(self, utente):
        self.model.utente = utente


    def set_orario_premuto_pre_te(self, orario):
        self.model.orario = orario

    def set_giorno_pre_te(self, giorno):
        self.model.data = giorno
