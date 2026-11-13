import pytest 
from mietvertrag import Mietvertrag
from kunde import Kunde
from fahrrad import Fahrrad
from e_bike import E_Bike

def test_negativer_tagespreis_wird_abgelehnt(): 
    with pytest.raises(ValueError): 
        Fahrrad("F-100", -1.00, True, 21) 

def test_mietdauer_muss_groesser_null_sein(): 
    kunde = Kunde("Mina Beispiel", 123) 
    fahrrad = Fahrrad("F-100", 15.00, True, 21) 

    with pytest.raises(ValueError): 
        Mietvertrag(1001, kunde, [fahrrad], 0) 

def test_nicht_verfuegbares_fahrzeug_kann_nicht_gemietet_werden(): 
    kunde = Kunde("Mina Beispiel", 123) 
    fahrrad = Fahrrad("F-100", 15.00, False, 21) 

    with pytest.raises(RuntimeError): 
        mietvertrag = Mietvertrag(1001, kunde, [fahrrad], 3)


def test_negativer_tagespreis_ebike_wird_abgelehnt(): 
    with pytest.raises(ValueError): 
        E_Bike("F-100", -5.00, True, 100) 