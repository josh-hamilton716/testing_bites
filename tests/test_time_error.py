from lib.time_error import *
from unittest.mock import Mock

def test_time():
    request_mock = Mock()
    responce_mock = Mock()
    curreent_time_mock = Mock()
    time1 = TimeError(request_mock, curreent_time_mock)
    request_mock.get.return_value = responce_mock
    responce_mock.json.return_value = {"unixtime":1700670224}
    curreent_time_mock.time.return_value = 1700670224.5
    result1 = time1.error()
    
    assert result1 == -0.5
