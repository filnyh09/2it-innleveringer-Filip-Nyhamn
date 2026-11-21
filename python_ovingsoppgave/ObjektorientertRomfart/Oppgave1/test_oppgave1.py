#jeg har brukt ai for å feilsøke eit import problem

import pytest
from main import romfartooy

def test_romfartooy_ooker_hastighet_og_konsumerer_drivstoff():
    testfartooy = romfartooy("test", 0, 10)
    testfartooy.ookeHastigheten()
    assert testfartooy.drivstoffmengde == 9 and testfartooy.hastighet == 1

def test_romfartooy_bruker_ikke_meir_drivstoff_en_den_har_og_ooker_dermed_ikke_hastighet():
    testfartooy = romfartooy("test", 10, 0)
    testfartooy.ookeHastigheten()
    assert testfartooy.drivstoffmengde == 0 and testfartooy.hastighet == 10