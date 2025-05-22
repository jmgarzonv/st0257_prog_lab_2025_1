import threading
from queue import Queue

class GenProdCons:
    def __init__(self, size=10):
        self.size = size
        self.buffer = Queue(maxsize=size)

    def put(self, e):
        self.buffer.put(e)  # bloquea si está lleno

    def get(self):
        return self.buffer.get()  # bloquea si está vacío

    def __len__(self):
        return self.buffer.qsize()


class RendezvousDEchange:
    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.first_value = None
        self.partner_ready = False

    def echanger(self, value):
        with self.condition:
            if not self.partner_ready:
                self.first_value = value
                self.partner_ready = True
                self.condition.wait()
                result = self.second_value
                self.partner_ready = False
                return result
            else:
                self.second_value = value
                self.condition.notify()
                return self.first_value
