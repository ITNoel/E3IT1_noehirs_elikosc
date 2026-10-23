from kunde import Kunde
from fahrzeug import Fahrzeug
from fahrrad import Fahrrad
from e_bike import E_Bike
from mietvertrag import Mietvertrag
from pytest import raises

def test_unterschiedliche_fahrzeuge():
    kunde = Kunde("Mina Beispiel", 123)

    fahrrad = Fahrrad("F-100", 15.00, True, 21)
    e_bike = E_Bike("E-200", 30.00, True, 500)

    mietvertrag_fahrrad = Mietvertrag(1001, kunde, [fahrrad], 3)
    mietvertrag_e_bike = Mietvertrag(1002, kunde, [e_bike], 3)

    assert fahrrad.get_grundpreis() == 15.00
    assert fahrrad.get_anzahl_gaenge() == 21
    assert mietvertrag_fahrrad.mietpreis() == 45

    assert e_bike.get_grundpreis() == 30.00
    assert e_bike.get_akkukapazitaet() == 500
    assert mietvertrag_e_bike.mietpreis() == 90.00
