#jeg har brukt ai for å feilsøke

import pytest
from main2 import romkargoskip, rompasasjerskip, rommissil, romfartooy


@pytest.mark.parametrize("klasse", [
    (romkargoskip),
    (rompasasjerskip),
    (rommissil),
])
def test_atributer_blir_arvet(klasse):
    assert hasattr(klasse, "presenter") and hasattr(klasse, "ookeHastigheten")


@pytest.mark.parametrize("lager, mengde, forventetLager", [
    (10, 57, 67),
    (83, 66, 149),
    (4, 7, 11),
])
def test_romkargoskip_laster_rigtig_mengde(lager, mengde, forventetLager):
    testShip = romkargoskip("test", 0, 0, lager)
    testShip.last(mengde)
    assert testShip.lager == forventetLager


@pytest.mark.parametrize("lager", [
    (10),
    (83),
    (4),
])
def test_romkargoskip_levering_resulterer_med_tomt_lager(lager):
    testShip = romkargoskip("test", 0, 0, lager)
    testShip.lever()
    assert testShip.lager == 0


@pytest.mark.parametrize("oksygen", [
    (10),
    (83),
    (4),
])
def test_rompasasjerskip_oksygenivaa_blir_hundre_prosent_når_den_lander(oksygen):
    testShip = rompasasjerskip("test", 0, 0, oksygen, 0)
    testShip.landing(0,0)
    assert testShip.oksygen == 100


