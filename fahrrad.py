from fahrzeug import Fahrzeug

class Fahrrad(Fahrzeug):

    def __init__(self, kennzeichen: str, grundpreis: float, verfuegbar: bool, anzahl_gaenge: int):
        super().__init__(kennzeichen = kennzeichen, grundpreis = grundpreis, verfuegbar = verfuegbar)
        self.anzahl_gaenge = anzahl_gaenge

    def get_anzahl_gaenge(self) -> int:
        return self.anzahl_gaenge