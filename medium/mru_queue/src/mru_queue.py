class MruQueue:

    def __init__(self, n):
        self.n = n
        self.queue = list(range(1, n + 1))

    def fetch(self, k) -> int:
        index = k-1
        value = self.queue[index]
        self.queue.pop(index)
        self.queue.append(value)
        return value
