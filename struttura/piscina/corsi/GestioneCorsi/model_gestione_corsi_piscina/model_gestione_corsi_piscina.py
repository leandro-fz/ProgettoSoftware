import os
import pickle


class model_gestione_corsi_piscina():
    def __init__(self):
        self.lista_corsipiscina = []
        if os.path.isfile("struttura/piscina/corsi/GestioneCorsi/DataGestionePiscina/data_gestioneCorsiPiscina.pickle"):
            with open("struttura/piscina/corsi/GestioneCorsi/DataGestionePiscina/data_gestioneCorsiPiscina.pickle", "rb") as file:
                try:
                    self.lista_corsipiscina = pickle.load(file)
                except EOFError:
                    return

    def aggiungi_corso(self, corso):
        self.lista_corsipiscina.append(corso)

    def get_lista_corsi(self):
        return self.lista_corsipiscina

    def get_corso_by_idcorso(self, idtennis):
        for corso in self.lista_corsipiscina:
            if corso.id== idtennis:
                return corso
        return None

    def elimina_corso_piscina(self, idcorso):
        for corso in self.lista_corsipiscina:
            if corso.id == idcorso:
                self.lista_corsipiscina.remove(corso)
                return True
        return False

    def save_data(self):
        with open("struttura/piscina/corsi/GestioneCorsi/DataGestionePiscina/data_gestioneCorsiPiscina.pickle", "wb") as handle:
            pickle.dump(self.lista_corsipiscina, handle, pickle.HIGHEST_PROTOCOL)