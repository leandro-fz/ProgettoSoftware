from gestione.finanziaria.movimenti.model_movimenti.model_movimenti import model_movimenti

#classe che al suo interno richiama il model di movimenti e fa uso delle funzioni implementate da esso
class controller_movimenti():


    def __init__(self):
        super(controller_movimenti, self).__init__()
        self.model = model_movimenti()

    def aggiungi_movimenti(self, movimenti):
        self.model.aggiungi_movimenti(movimenti)

    def get_lista_movimenti(self):
        return self.model.get_lista_movimenti()

    def get_movimenti_by_fattura(self, fattura):
        return self.model.get_movimenti_by_fattura(fattura)

    def rimuovi_movimenti_by_fattura(self, fattura):
        self.model.rimuovi_movimenti_by_fattura(fattura)

    def save_data(self):
        self.model.save_data()
