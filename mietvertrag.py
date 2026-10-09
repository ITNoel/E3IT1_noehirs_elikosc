from kunde import Kunde
from fahrzeug import Fahrzeug
from datetime import date

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
            preis += einzel_fahrzeug.grundpreis * ( date(self.mietende) - date(self.mietbeginn) )
        return preis