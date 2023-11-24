from lib.sectret_diary import *
from unittest.mock import Mock
import pytest

def test_diary_locked():
    diary1 = Mock()
    secret_diary1 = SecretDiary(diary1)
    with pytest.raises(Exception) as e:
        secret_diary1.read()
    assert str(e.value) == "Go away!"


def test_diary_unlocked():
    diary1 = Mock()
    diary1.read.return_value = "ENTRY"
    secret_diary1 = SecretDiary(diary1)
    secret_diary1.unlock()
    assert secret_diary1.read() == "ENTRY"

def test_diary_locked_again():
    diary1 = Mock()
    diary1.read.return_value = "ENTRY"
    secret_diary1 = SecretDiary(diary1)
    secret_diary1.unlock()
    secret_diary1.lock()
    with pytest.raises(Exception) as e:
        secret_diary1.read()
    assert str(e.value) == "Go away!"

def test_diary_unlocked_again():
    diary1 = Mock()
    diary1.read.return_value = "ENTRY"
    secret_diary1 = SecretDiary(diary1)
    secret_diary1.unlock()
    secret_diary1.lock()
    secret_diary1.unlock()
    assert secret_diary1.read() == "ENTRY"