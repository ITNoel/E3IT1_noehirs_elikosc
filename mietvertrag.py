from kunde import Kunde
from fahrzeug import Fahrzeug
from datetime import datetime

class Mietvertrag:

    def __init__(self, vertragsnummer: int, mietbeginn: str, mietende: str, kunde: Kunde, fahrzeuge: list[Fahrzeug]):
        self.vertragsnummer = vertragsnummer
        self.mietbeginn = mietbeginn
        self.mietende = mietende
        self.kunde = kunde
        self.fahrzeug = fahrzeuge
    
    def mietpreis(self) -> float:
        preis = 0
        for einzel_fahrzeug in self.fahrzeug:
            end_datum = datetime.strptime(self.mietende, "%d.%m.%Y").date()
            beg_datum = datetime.strptime(self.mietbeginn, "%d.%m.%Y").date()

            preis += einzel_fahrzeug.grundpreis * (end_datum - beg_datum).days

        return preis

    def beenden():
        pass