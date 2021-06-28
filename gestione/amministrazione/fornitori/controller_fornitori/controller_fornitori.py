from gestione.amministrazione.fornitori.model_fornitori.model_fornitori import Insieme_Fornitori


class Controller_Fornitori():

    def __init__(self):
        super(Controller_Fornitori, self).__init__()
        self.model = Insieme_Fornitori()

    def aggiungi_fornitore(self, fornitore):
        self.model.aggiungi_fornitore(fornitore)

    def get_lista_fornitori(self):
        return self.model.get_lista_fornitori()

    def get_fornitore_by_codicearticolo(self, codicearticolo):
        return self.model.get_fornitore_by_codicearticolo(codicearticolo)

    def elimina_fornitore_by_codicearticolo(self, codicearticolo):
        self.model.rimuovi_fornitore_by_codicearticolo(codicearticolo)

    def save_data(self):
        self.model.save_data()
