import os
import pickle

# iscritti/
class Insieme_Iscritti():
    def __init__(self):
        super(Insieme_Iscritti, self).__init__()
        self.lista_iscritti = []
        # print("ok")
        # k = os.path.isfile("gestione/amministrazione/iscritti/data_iscritti/lista_iscritti_salvata.pickle")
        # print(k)
        if os.path.isfile("struttura/piscina/iscritti/data_iscritti/lista_iscritti_salvata.pickle"):
            # print("ok2")
            with open("struttura/piscina/iscritti/data_iscritti/lista_iscritti_salvata.pickle", "rb") as file:
                # print("file recuperato")
                self.lista_iscritti = pickle.load(file)
                print("file recuperato2")

    def aggiungi_utente(self, utente):
        self.lista_iscritti.append(utente)

    def rimuovi_utente_by_id(self, id):
        for utente in self.lista_iscritti:
            if utente.id == id:
                self.lista_iscritti.remove(utente)
                return True
        return False

    def get_lista_iscritti(self):
        return self.lista_iscritti

    def get_utente_by_id(self, id):
        for utente in self.lista_iscritti:
            if utente.id == id:
                return utente
        return None

    def save_data(self):
        if os.path.isfile("struttura/piscina/iscritti/data_iscritti/lista_iscritti_salvata.pickle"):
            with open("struttura/piscina/iscritti/data_iscritti/lista_iscritti_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_iscritti, handle, pickle.HIGHEST_PROTOCOL)