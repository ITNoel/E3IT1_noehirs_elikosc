from kunde import Kunde
from fahrzeug import Fahrzeug
from fahrrad import Fahrrad
from e_bike import E_Bike
from mietvertrag import Mietvertrag

def test_fahrzeuge_berechnen_unterschiedliche_mietpreise(): 
    kunde = Kunde("Mina Beispiel", 123) 
    fahrrad = Fahrrad("F-100", 15.00, True, 21) 
    e_bike = E_Bike("E-200", 30.00, True, 500) 
    mietvertrag = Mietvertrag(1001, kunde, [fahrrad], 3) 
    mietvertrag.hinzufuegen_fahrzeug(e_bike) 
    assert mietvertrag.mietpreis() == 150.00