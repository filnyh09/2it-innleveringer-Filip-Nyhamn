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


@pytest.mark.parametrize("klasse", [
    (romkargoskip),
    (rompasasjerskip),
    (rommissil),
])
def test_romkargoskip_laster_rigtig_mengde(lager, mengde, forventetLager):
    testShip = romkargoskip("test", 0, 0, lager)
    testShip.last(mengde)
    assert testShip.lager == forventetLager