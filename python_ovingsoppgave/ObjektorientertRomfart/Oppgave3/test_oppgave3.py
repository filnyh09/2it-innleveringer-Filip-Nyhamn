#jeg har brukt ai for å feilsøke eit import problem

import pytest
from main3 import SveiseRobot, RengjøringsEnhet, Datamaskin

@pytest.mark.parametrize("enhet, status, forventetresultat", [
    (SveiseRobot, True, "Reparerer skader på romstasjonen."),
    (RengjøringsEnhet, True, "Tømmer luftfilter."),
    (Datamaskin, True, "Behandler teleskopdata."),
    (SveiseRobot, False, "Må vere aktive for å utføre oppdrag"),
    (RengjøringsEnhet, False, "Må vere aktive for å utføre oppdrag"),
    (Datamaskin, False, "Må vere aktive for å utføre oppdrag"),
])
def test_utfoor_oppdrag_gir_rigtig_resultat(enhet, status, forventetresultat):
    testenhet = enhet("test", status)
    assert testenhet.utfoorOppdrag() == forventetresultat