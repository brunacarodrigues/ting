from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.values = []

    def __len__(self):
        return len(self.values)

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.values.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def search(self, index):
        if 0 <= index < len(self.values):
            return self.values[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")

    def is_empty(self):
        return len(self.values) == 0
