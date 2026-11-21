#jeg har brukt ai for å feilsøke eit import problem

import pytest
from main import romkargoskip, rompasasjerskip, rommissil

@pytest.mark.parametrize("klasse", [
    (romkargoskip),
    (rompasasjerskip),
    (rommissil),
])
#def test_atributer_blir_arvet(klasse):
#    assert hasattr(klasse, 'presenter()')