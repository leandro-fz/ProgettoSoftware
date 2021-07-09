from datetime import datetime, timedelta

class model_gestione_abbonamenti():

    def __init__(self, nome, cognome, nato, data, codicefiscale,residenza, email, cellulare,struttura, tipoabbonamento, attivazione):

        self.nome = nome
        self.cognome = cognome
        self.nato = nato
        self.data = data
        self.codicefiscale = codicefiscale
        self.residenza = residenza
        self.email = email
        self.cellulare = cellulare
        self.struttura = struttura
        self.tipoabbonamento = tipoabbonamento
        self.attivazione = attivazione

    def get_scadenza_abbonamento(self, durata, attivazione):
        if durata == "settimanale":
            date_final = datetime.date(attivazione) + timedelta(7)

        if durata == "mensile":
            date_final = datetime.date(attivazione) + timedelta(30)

        if durata == "trimestrale":
            date_final = datetime.date(attivazione) + timedelta(90)

        if durata == "semestrale":
            date_final = datetime.date(attivazione) + timedelta(180)

        if durata == "annuale":
            date_final = datetime.date(attivazione) + timedelta(365)

        return date_final