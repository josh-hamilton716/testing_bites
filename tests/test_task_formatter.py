from lib.task_formater import *
from unittest.mock import Mock

def test_returns_as_complete():
    task1 = Mock()
    task1.title = "text"
    task1.is_complete.return_value = True
    formated_task = TaskFormatter(task1)
    assert formated_task.format() == "- [x] text"
    

def test_returns_as_incomplete():
    task1 = Mock()
    task1.title = "text"
    task1.is_complete.return_value = False
    formated_task = TaskFormatter(task1)
    assert formated_task.format() == "- [ ] text"