from lib.diary import *

def test_enter_and_return():
    diary1 = Diary("ENTRY")
    assert diary1.read() == "ENTRY"
