import os
import pickle

class model_certificati():

    # nella funzione c'è il collegamento con il file "lista_certificati_salvata" dove i certificati e le varie informazioni verranno salvate
    def __init__(self):
        super(model_certificati, self).__init__()
        self.lista_certificati = []
        if os.path.isfile("gestione/cliente/certificati/data_certificati/lista_certificati_salvata.pickle"):
            with open("gestione/cliente/certificati/data_certificati/lista_certificati_salvata.pickle", "rb") as file:
                try:
                    self.lista_certificati = pickle.load(file)
                except EOFError:
                    return

    # la funzione inserisce il certificato alla lista
    def aggiungi_certificato(self, certificato):
        self.lista_certificati.append(certificato)

    # la funzione elimina il certificato dalla lista attraverso il campo "codicefiscale"
    def elimina_certificato_by_codicefiscale(self, codicefiscale):
        for certificato in self.lista_certificati:
            if certificato.codicefiscale == codicefiscale:
                self.lista_certificati.remove(certificato)
                return True
        return False

    # la funzione ridà la lista dei certificati
    def get_lista_certificati(self):
        return self.lista_certificati

    def get_certificato_by_codicefiscale(self, codicefiscale):
        for certificato in self.lista_certificati:
            if certificato.codicefiscale == codicefiscale:
                return certificato
        return None

    # salva i dati dei certificati inseriti
    def save_data(self):
        if os.path.isfile("gestione/cliente/certificati/data_certificati/lista_certificati_salvata.pickle"):
            with open("gestione/cliente/certificati/data_certificati/lista_certificati_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_certificati, handle, pickle.HIGHEST_PROTOCOL)