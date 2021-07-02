class GestioniCertificato():

    def __init__(self, nome, cognome, nato, codicefiscale, residenza, sportcertificato,certificatoagonistico, datainizio, datafine):

        self.nome = nome
        self.cognome = cognome
        self.nato = nato
        self.codicefiscale = codicefiscale
        self.residenza = residenza
        self.sportcertificato = sportcertificato
        self.certificatoagonistico = certificatoagonistico
        self.datainizio = datainizio
        self.datafine = datafine
        self.certificato_pdf = None
