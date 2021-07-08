import os
import pickle

# iscritti/
class model_iscritti():
    def __init__(self):
        super(model_iscritti, self).__init__()
        self.lista_iscritti= []
        if os.path.isfile("struttura/piscina/Iscritti/data_iscritti/lista_iscritti_salvata.pickle"):
            with open("struttura/piscina/Iscritti/data_iscritti/lista_iscritti_salvata.pickle",
                      "rb") as file:
                try:
                    self.lista_iscritti = pickle.load(file)
                except EOFError:
                    return

    def aggiungi_utente(self, utente):
        self.lista_iscritti.append(utente)

    def elimina_utente_by_codicefiscale(self, codicefiscale):
        for utente in self.lista_iscritti:
            if utente.codicefiscale == codicefiscale:
                self.lista_iscritti.remove(utente)
                return True
        return False

    def get_lista_iscritti(self):
        return self.lista_iscritti

    def get_utente_by_codicefiscale(self, codicefiscale):
        for utente in self.lista_iscritti:
            if utente.codicefiscale == codicefiscale:
                return utente
        return None

    def save_data(self):
        if os.path.isfile("struttura/piscina/iscritti/data_iscritti/lista_iscritti_salvata.pickle"):
            with open("struttura/piscina/iscritti/data_iscritti/lista_iscritti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_iscritti, handle, pickle.HIGHEST_PROTOCOL)