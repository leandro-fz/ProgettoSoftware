import unittest

from gestione.cliente.GestioneAbbonamenti.model_GestioneAbbonamenti.model_GestioneAbbonamenti import GestioniAbbonamento
from gestione.cliente.abbonamenti.controller_abbonamenti.controller_abbonamenti import Controller_Abbonamenti


class Test(unittest.TestCase):
    def setUp(self):
        self.controller_lista_abbonamenti = Controller_Abbonamenti()
        self.abbonamento = GestioniAbbonamento("Filippo", "Caterbetti","Macerata", "13/04/2000", "1234567891234567", "Appignano","filippo@gmail.com","3348967115", "Piscina", "mensile")
        self.controller_lista_abbonamenti.aggiungi_abbonamento(self.abbonamento)
        self.model_lista_abbonamenti = self.controller_lista_abbonamenti.get_lista_abbonamenti()

    def test_aggiungi_abbonamento(self):
        self.assertIsNotNone(self.abbonamento.codicefiscale)
        self.controller_lista_abbonamenti.aggiungi_abbonamento(self.abbonamento)
        self.assertTrue(self.abbonamento in self.model_lista_abbonamenti)

    def test_elimina_abbonamento_by_codicefiscale(self):
        self.assertIsNotNone(self.model_lista_abbonamenti)
        self.controller_lista_abbonamenti.elimina_abbonamento_by_codicefiscale(self.abbonamento.codicefiscale)
        self.assertTrue(self.abbonamento not in self.model_lista_abbonamenti)

    def test_get_abbonamento_by_codicefiscale(self):
        self.assertIsNone(self.controller_lista_abbonamenti.get_abbonamento_by_codicefiscale("33333"))
        self.assertIsNotNone(self.controller_lista_abbonamenti.get_abbonamento_by_codicefiscale("1234567891234567"))

    def test_get_lista_abbonamenti(self):
        self.assertNotEqual(self.controller_lista_abbonamenti.get_lista_abbonamenti(), [])