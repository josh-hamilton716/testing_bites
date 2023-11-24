from lib.sectret_diary import *
from lib.diary import *
import pytest

def test_diary_locked():
    diary1 = Diary("ENTRY")
    secret_diary1 = SecretDiary(diary1)
    with pytest.raises(Exception) as e:
        secret_diary1.read()
    assert str(e.value) == "Go away!"


def test_diary_unlocked():
    diary1 = Diary("ENTRY")
    secret_diary1 = SecretDiary(diary1)
    secret_diary1.unlock()
    assert secret_diary1.read() == "ENTRY"

def test_diary_locked_again():
    diary1 = Diary("ENTRY")
    secret_diary1 = SecretDiary(diary1)
    secret_diary1.unlock()
    secret_diary1.lock()
    with pytest.raises(Exception) as e:
        secret_diary1.read()
    assert str(e.value) == "Go away!"

def test_diary_unlocked_again():
    diary1 = Diary("ENTRY")
    secret_diary1 = SecretDiary(diary1)
    secret_diary1.unlock()
    secret_diary1.lock()
    secret_diary1.unlock()
    assert secret_diary1.read() == "ENTRY"