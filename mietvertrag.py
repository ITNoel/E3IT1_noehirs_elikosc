from kunde import Kunde
from fahrzeug import Fahrzeug
from datetime import datetime, timedelta

class Mietvertrag:

    def __init__(self, vertragsnummer: int, kunde: Kunde, fahrzeuge: list[Fahrzeug], mietdauer: int):
        self.vertragsnummer = vertragsnummer
        self.mietdauer = mietdauer
        self.kunde = kunde

        for fahrzeug in fahrzeuge:
            if fahrzeug.verfuegbar == False:
                print(f"Fahrzeug: {fahrzeug.kennzeichen}, wird aus dem Vertrag entfernt, da nicht verfügbar.")
                fahrzeuge.remove(fahrzeug)

        self.fahrzeuge = fahrzeuge
        self.mietbeginn = datetime.now().date()
        self.mietende = self.mietbeginn + timedelta(days=self.mietdauer)

    def mietpreis(self) -> float:
        preis = 0

        for fahrzeug in self.fahrzeuge:
            preis += fahrzeug.grundpreis * self.mietdauer

        return preis

    def beenden():
        pass