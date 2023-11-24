from unittest.mock import Mock
from lib.cat_face import CatFacts

def test_cat_facts():
    request_mock = Mock()
    result_mock = Mock()
    new_cat = CatFacts(request_mock)
    request_mock.get.return_value = result_mock
    result_mock.json.return_value = {"fact":"The leopard is the most widespread of all big cats."}
    result = new_cat.provide()
    assert result == "Cat fact: The leopard is the most widespread of all big cats."
