from kunde import Kunde
from fahrzeug import Fahrzeug
from datetime import datetime, timedelta

class Mietvertrag:

    def __init__(self, vertragsnummer: int, kunde: Kunde, fahrzeuge: list[Fahrzeug], mietdauer: int):
        self.vertragsnummer = vertragsnummer

        if mietdauer < 1:
            raise ValueError("Mietdauer darf nicht Negativ sein.")
        
        self.mietdauer = mietdauer
        self.kunde = kunde

        for fahrzeug in fahrzeuge:
            if fahrzeug.ist_verfuegbar() == False:
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

    def beenden(self):
        for fahrzeug in self.fahrzeuge:
            fahrzeug.set_verfuegbar(True)

    def starten(self):
        for fahrzeug in self.fahrzeuge:
            fahrzeug.set_verfuegbar(False)