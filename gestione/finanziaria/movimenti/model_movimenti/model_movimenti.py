import os
import pickle


class model_movimenti():
    def __init__(self):
        super(model_movimenti, self).__init__()
        self.lista_movimenti = []
        if os.path.isfile("finanziaria/movimenti/data_movimenti/lista_movimenti_salvata.pickle"):
            with open("finanziaria/movimenti/data_movimenti/lista_movimenti_salvata.pickle", "rb") as file:
                try:
                    self.lista_movimenti = pickle.load(file)
                except EOFError:
                    return


    def aggiungi_movimenti(self, movimenti):
        self.lista_movimenti.append(movimenti)

    def rimuovi_movimenti_by_fattura(self, fattura):
        for movimento in self.lista_movimenti:
            if movimento.fattura == fattura:
                self.lista_movimenti.remove(movimento)
                return True
        return False

    def get_lista_movimenti(self):
        return self.lista_movimenti


    def save_data(self):
        if os.path.isfile("finanziaria/movimenti/data_movimenti/lista_movimenti_salvata.pickle"):
            with open("finanziaria/movimenti/data_movimenti/lista_movimenti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_movimenti, handle, pickle.HIGHEST_PROTOCOL)