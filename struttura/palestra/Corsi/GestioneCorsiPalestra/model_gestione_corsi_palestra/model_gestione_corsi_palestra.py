import os
import pickle


class model_gestione_corsi_palestra():
    def __init__(self):
        self.lista_corsipalestra = []
        if os.path.isfile("struttura/palestra/Corsi/GestioneCorsiPalestra/data_gestione_corsi_palestra/data_gestione_corsi_palestra.pickle"):
            with open("struttura/palestra/Corsi/GestioneCorsiPalestra/data_gestione_corsi_palestra/data_gestione_corsi_palestra.pickle", "rb") as file:
                try:
                    self.lista_corsipalestra = pickle.load(file)
                except EOFError:
                    return

    def aggiungi_corso_palestra(self, corso):
        self.lista_corsipalestra.append(corso)

    def get_lista_corsi_palestra(self):
        return self.lista_corsipalestra

    def get_corso_palestra_by_idcorso(self, idtennis):
        for corso in self.lista_corsipalestra:
            if corso.id== idtennis:
                return corso
        return None

    def elimina_corso_palestra(self, idcorso):
        for corso in self.lista_corsipalestra:
            if corso.id == idcorso:
                self.lista_corsipalestra.remove(corso)
                return True
        return False

    def save_data(self):
        with open("struttura/palestra/Corsi/GestioneCorsiPalestra/data_gestione_corsi_palestra/data_gestione_corsi_palestra.pickle", "wb") as handle:
            pickle.dump(self.lista_corsipalestra, handle, pickle.HIGHEST_PROTOCOL)