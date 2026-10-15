from kunde import Kunde
from fahrzeug import Fahrzeug
from mietvertrag import Mietvertrag

def test_mietpreis_berechnen(): 
    kunde = Kunde("Mina Beispiel", 123) 
    fahrzeug = Fahrzeug("AB-CD 123", 30.00, True) 
    mietvertrag = Mietvertrag(1001, kunde, [fahrzeug], 3) 
    assert mietvertrag.mietpreis() == 90.00 

def test_fahrzeug_nicht_verfuegbar():
    kunde = Kunde("Frank Der Goat", 123) 
    porsche = Fahrzeug("Porsche Cayman S", 300.00, True)
    audi = Fahrzeug("Irgendein Drecks Karren ist eh scheiß egal, weil nicht verfügbar", 10.00, False) 
    mietvertrag = Mietvertrag(1001, kunde, [porsche, audi], 3)

    # Nur die Kosten vom porsche sollten genommen werden, da der Audi nicht im Mietvertrag dazugehören sollte, da er nicht verfügbar ist
    assert mietvertrag.mietpreis() == 900.00 