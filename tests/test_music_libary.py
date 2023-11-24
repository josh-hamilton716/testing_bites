from lib.music_libary import MusicLibrary
from unittest.mock import Mock

def test_music_libary_two_matches():
    libary1 = MusicLibrary()
    mock1 = Mock()
    mock1.matches.return_value = True
    mock2 = Mock()
    mock2.matches.return_value = False
    mock3 = Mock()
    mock3.matches.return_value = True
    libary1.add(mock1)
    libary1.add(mock2)
    libary1.add(mock3)
    assert libary1.search("junk") == [mock1, mock3]


def test_music_libary_three_matches():
    libary1 = MusicLibrary()
    mock1 = Mock()
    mock1.matches.return_value = True
    mock2 = Mock()
    mock2.matches.return_value = True
    mock3 = Mock()
    mock3.matches.return_value = True
    libary1.add(mock1)
    libary1.add(mock2)
    libary1.add(mock3)
    assert libary1.search("junk") == [mock1, mock2, mock3]