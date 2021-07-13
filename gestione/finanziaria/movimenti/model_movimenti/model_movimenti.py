import os
import pickle


class model_movimenti():

    #nella funzione c'è il collegamento con il file "lista_movimenti_salvata" dove i movimenti e le varie informazioni verranno salvate
    def __init__(self):
        super(model_movimenti, self).__init__()
        self.lista_movimenti = []
        if os.path.isfile("gestione/finanziaria/movimenti/data_movimenti/lista_movimenti_salvata.pickle"):
            with open("gestione/finanziaria/movimenti/data_movimenti/lista_movimenti_salvata.pickle", "rb") as file:
                try:
                    self.lista_movimenti = pickle.load(file)
                except EOFError:
                    return

    #la funzione inserisce il movimento alla lista
    def aggiungi_movimenti(self, movimenti):
        self.lista_movimenti.append(movimenti)

    #la funzione elimina il movimento dalla lista attraverso il campo "fattura"
    def rimuovi_movimenti_by_fattura(self, fattura):
        for movimento in self.lista_movimenti:
            if movimento.fattura == fattura:
                self.lista_movimenti.remove(movimento)
                return True
        return False

    #la funzione ridà la lista dei movimenti
    def get_lista_movimenti(self):
        return self.lista_movimenti


    #salva i dati dei movimenti inseriti
    def save_data(self):
        if os.path.isfile("gestione/finanziaria/movimenti/data_movimenti/lista_movimenti_salvata.pickle"):
            with open("gestione/finanziaria/movimenti/data_movimenti/lista_movimenti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_movimenti, handle, pickle.HIGHEST_PROTOCOL)