from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_add_two_tasks():
    task_list = TaskList()
    mock1 = Mock()
    mock2 = Mock()
    task_list.add(mock1)
    task_list.add(mock2)
    assert task_list.all() == [mock1, mock2]

def test_add_two_tasks_one_complet():
    task_list = TaskList()
    mock1 = Mock()
    mock2 = Mock()
    mock1.is_complete.return_value = False
    mock2.is_complete.return_value = True
    task_list.add(mock1)
    task_list.add(mock2)
    assert task_list.all_complete() == False


def test_add_two_tasks_both_complet():
    task_list = TaskList()
    mock1 = Mock()
    mock2 = Mock()
    mock1.is_complete.return_value = True
    mock2.is_complete.return_value = True
    task_list.add(mock1)
    task_list.add(mock2)
    assert task_list.all_complete() == True