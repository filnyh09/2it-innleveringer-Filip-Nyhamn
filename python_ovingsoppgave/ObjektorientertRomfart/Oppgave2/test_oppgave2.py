#jeg har brukt ai for å feilsøke

import pytest
from main import romkargoskip, rompasasjerskip, rommissil, romfartooy

@pytest.mark.parametrize("klasse", [
    (romkargoskip),
    (rompasasjerskip),
    (rommissil),
])
def test_atributer_blir_arvet(klasse):
    assert hasattr(klasse, klasse.presenter)