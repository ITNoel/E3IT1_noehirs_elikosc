from kunde import Kunde
from fahrzeug import Fahrzeug
from mietvertrag import Mietvertrag
from pytest import raises

def test_fahrzeugstatus_wird_kontrolliert_geaendert(): 
    kunde = Kunde("Mina Beispiel", 123) 
    fahrzeug = Fahrzeug("AB-CD 123", 30.00, True) 
    mietvertrag = Mietvertrag(1001, kunde, [fahrzeug], 3) 

    assert fahrzeug.ist_verfuegbar() is True 
    assert mietvertrag.mietpreis() == 90.00 

    mietvertrag.starten() 
    assert fahrzeug.ist_verfuegbar() is False 

    mietvertrag.beenden() 
    assert fahrzeug.ist_verfuegbar() is True

def test_valider_mietbeginn():
    kunde = Kunde("Mina Beispiel", 123) 
    fahrzeug = Fahrzeug("AB-CD 123", 30.00, True) 
    with raises(ValueError):
        mietvertrag = Mietvertrag(1001, kunde, [fahrzeug], -1) 

    