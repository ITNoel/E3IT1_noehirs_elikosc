class Fahrzeug:

    def __init__(self, kennzeichen: str, grundpreis: float, verfuegbar: bool):
        self.kennzeichen = kennzeichen
        self.grundpreis = grundpreis
        self.__verfuegbar = verfuegbar

    def set_verfuegbar(self, verfuegbar: bool):
        self.__verfuegbar = verfuegbar

    def ist_verfuegbar(self) -> bool:
        return self.__verfuegbar