from ting_file_management.priority_queue import PriorityQueue
import pytest

data = [
    {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 9,
        "linhas_do_arquivo": [
            "linha1", "linha2",
            "linha3", "linha4", "linha5",
            "linha6", "linha7", "linha8", "linha9"]
    },
    {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3", "linha4"]
    },
    {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ["linha1", "linha2"]
    },
    {
        "nome_do_arquivo": "arquivo4.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3", "linha4", "linha5"]
    },
    {
        "nome_do_arquivo": "arquivo5.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": [
            "linha1", "linha2", "linha3",
            "linha4", "linha5", "linha6",
            "linha7"]
    },
    {
        "nome_do_arquivo": "arquivo6.txt",
        "qtd_linhas": 11,
        "linhas_do_arquivo": [
            "linha1", "linha2", "linha3",
            "linha4", "linha5", "linha6",
            "linha7", "linha8", "linha9",
            "linha10", "linha11"]
    },
    {
        "nome_do_arquivo": "arquivo7.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3"]
    }
]


def test_basic_priority_queueing():
    queue = PriorityQueue()

    for item in data:
        queue.enqueue(item)

    assert len(queue) == 7
    assert queue.search(0) == data[1]

    queue.dequeue()

    assert len(queue) == 6
    assert queue.search(0) == data[2]

    with pytest.raises(IndexError):
        queue.search(65)
