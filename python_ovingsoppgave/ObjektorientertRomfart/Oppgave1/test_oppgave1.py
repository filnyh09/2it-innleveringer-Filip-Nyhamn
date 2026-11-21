#jeg har brukt ai for å feilsøke eit import problem

import pytest
from main1 import romfartooy

@pytest.mark.parametrize("starthastighet, startdrivstoff, forventethastighet, forventetdrivstoff", [
    (5, 4, 6, 3),
    (7, 1, 8, 0),
    (19, 68, 20, 67),
])
def test_romfartooy_ooker_hastighet_og_konsumerer_drivstoff(starthastighet, startdrivstoff, forventethastighet, forventetdrivstoff):
    testfartooy = romfartooy("test", starthastighet, startdrivstoff)
    testfartooy.ookeHastigheten()
    assert testfartooy.drivstoffmengde == forventetdrivstoff and testfartooy.hastighet == forventethastighet

def test_romfartooy_bruker_ikke_meir_drivstoff_en_den_har_og_ooker_dermed_ikke_hastighet():
    testfartooy = romfartooy("test", 10, 0)
    testfartooy.ookeHastigheten()
    assert testfartooy.drivstoffmengde == 0 and testfartooy.hastighet == 10