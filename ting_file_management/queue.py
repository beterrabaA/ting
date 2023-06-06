from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    ""'Classe que implementa uma fila'""
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        """Método que retorna o valor de um elemento da fila"""
        if index < 0 or index > len(self.queue) - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
