import unittest

from gestione.cliente.GestioneAbbonamenti.model_gestione_abbonamenti.model_gestione_abbonamenti import \
    model_gestione_abbonamenti
from gestione.cliente.abbonamenti.controller_abbonamenti.controller_abbonamenti import controller_abbonamenti


class Test(unittest.TestCase):
    def setUp(self):
        self.controller_lista_abbonamenti = controller_abbonamenti()
        self.abbonamento = model_gestione_abbonamenti("Filippo", "Caterbetti","Macerata", "13/04/2000", "1234567891234567", "Appignano","filippo@gmail.com","3348967115", "Piscina", "mensile", "12/12/2000")
        self.controller_lista_abbonamenti.aggiungi_abbonamento(self.abbonamento)
        self.model_lista_abbonamenti = self.controller_lista_abbonamenti.get_lista_abbonamenti()

    #Dopo aver aggiunto un abbonamento, verifichiamo che questo sia stato effettivamente aggiunto all'interno della lista
    def test_aggiungi_abbonamento(self):
        self.assertIsNotNone(self.abbonamento.codicefiscale)
        self.controller_lista_abbonamenti.aggiungi_abbonamento(self.abbonamento)
        self.assertTrue(self.abbonamento in self.model_lista_abbonamenti)

    #Dopo aver eliminato un abbonamento, verifichiamo che questo sia stato effettivamente eliminato all'interno della lista
    def test_elimina_abbonamento_by_codicefiscale(self):
        self.assertIsNotNone(self.model_lista_abbonamenti)
        self.controller_lista_abbonamenti.elimina_abbonamento_by_codicefiscale(self.abbonamento.codicefiscale)
        self.assertTrue(self.abbonamento not in self.model_lista_abbonamenti)

    #Verifichiamo che riusciamo a filtrare un abbonamento usando il suo codice fiscale associato
    def test_get_abbonamento_by_codicefiscale(self):
        self.assertIsNone(self.controller_lista_abbonamenti.get_abbonamento_by_codicefiscale("33333"))
        self.assertIsNotNone(self.controller_lista_abbonamenti.get_abbonamento_by_codicefiscale("1234567891234567"))

    #Verifichiamo di poter estrapolare tutti gli abbonamenti presenti nella lista
    def test_get_lista_abbonamenti(self):
        self.assertNotEqual(self.controller_lista_abbonamenti.get_lista_abbonamenti(), [])