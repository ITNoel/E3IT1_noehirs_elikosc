from fahrzeug import Fahrzeug

class E_Bike(Fahrzeug):

    def __init__(self, kennzeichen: str, grundpreis: float, verfuegbar: bool, akku_kapazitaet: int):
        super().__init__(kennzeichen = kennzeichen, grundpreis = grundpreis, verfuegbar = verfuegbar)
        self.akku_kapazitaet = akku_kapazitaet

    def get_akkukapazitaet(self) -> int:
        return self.akku_kapazitaet