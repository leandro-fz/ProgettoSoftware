class model_gestione_movimenti():

    def __init__(self, importo, data, causale, fattura):

        self.importo = importo
        self.data = data
        self.causale = causale
        self.fattura = fattura

    def get_resoconto(self):
        resoconto = 10
        return resoconto