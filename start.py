from mietvertrag import Mietvertrag
from kunde import Kunde
from fahrrad import Fahrrad
from e_bike import E_Bike

kunde = Kunde("Mina Beispiel", 123) 
fahrrad = Fahrrad("F-100", 15.00, True, 21) 
e_bike = E_Bike("F-100", 15.00, True, 13) 
mietvertrag = Mietvertrag(1001, kunde, [fahrrad], 3)

print(f"Das Fahrrad hat {fahrrad.get_anzahl_gaenge()} Gänge!")
print(f"Das E-Bike hat eine Akkukapazität von {e_bike.get_akkukapazitaet()}!")

mietvertrag.hinzufuegen_fahrzeug(e_bike)
mietvertrag.starten()

print(f"Die kompletten Mietkosten betragen: {mietvertrag.mietpreis()}")

try:
    mietvertrag.starten()
except RuntimeError:
    print("Fehler wird richtig geworfen")
mietvertrag.beenden()