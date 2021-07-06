import unittest

from gestione.amministrazione.GestioneDipendenti.model_gestione_dipendenti.model_gestione_dipendenti import \
    model_gestione_dipendenti
from gestione.amministrazione.dipendenti.controller_dipendenti.controller_dipendenti import controller_dipendenti


class Test(unittest.TestCase):
    def setUp(self):
        self.controller_listadipendenti = controller_dipendenti()
        self.dipendente = model_gestione_dipendenti("Filippo", "Caterbetti","Macerata", "13/04/2000", "1234567891234567","indeterminato", "addetto alle pulizie","99999", "1500")
        self.model_lista_dipendenti = self.controller_listadipendenti.get_lista_dipendenti()
        self.controller_listadipendenti.aggiungi_dipendente(self.dipendente)

    def test_aggiungi_dipendente(self):
        self.assertIsNotNone(self.dipendente.id)
        self.controller_listadipendenti.aggiungi_dipendente(self.dipendente)
        self.assertTrue(self.dipendente in self.model_lista_dipendenti)

    def test_elimina_dipendente_by_id(self):
        self.assertIsNotNone(self.model_lista_dipendenti)
        self.controller_listadipendenti.elimina_dipendente_by_id(self.dipendente.id)
        self.assertTrue(self.dipendente not in self.model_lista_dipendenti)

    def test_get_dipendente_by_id(self):
        self.assertIsNone(self.controller_listadipendenti.get_dipendente_by_id("33333"))
        self.assertIsNotNone(self.controller_listadipendenti.get_dipendente_by_id("99999"))

    def test_get_lista_dipendenti(self):
        self.assertNotEqual(self.controller_listadipendenti.get_lista_dipendenti(),[])