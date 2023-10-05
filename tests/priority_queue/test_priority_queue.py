from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()
    pq.enqueue({'qtd_linhas': 7})
    assert len(pq.regular_priority.values) == 1

    pq.dequeue()
    assert len(pq.regular_priority.values) == 0
    with pytest.raises(IndexError) as excinfo:
        pq.search(1)
    assert str(excinfo.value) == "Índice Inválido ou Inexistente"

    pq.enqueue({'qtd_linhas': 10})
    pq.enqueue({'qtd_linhas': 1})
    assert len(pq.high_priority.values) == 1

    pq.enqueue({'qtd_linhas': 2})
    assert pq.search(1).get('qtd_linhas') == 2
