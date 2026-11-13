from abc import ABC, abstractmethod
class Fahrzeug(ABC):

    def __init__(self, kennzeichen: str, grundpreis: float, verfuegbar: bool):
        if grundpreis < 0:
            raise ValueError("Grundpreis darf nicht negativ sein.")
        
        self.kennzeichen = kennzeichen
        self.grundpreis = grundpreis
        self.__verfuegbar = verfuegbar

    def set_verfuegbar(self, verfuegbar: bool):
        self.__verfuegbar = verfuegbar

    def ist_verfuegbar(self) -> bool:
        return self.__verfuegbar
    
    def get_grundpreis(self) -> float:
        return self.grundpreis
    
    @abstractmethod
    def berechne_mietpreis(self, mietdauer:int) -> float:
        pass