class MruQueue:

    def __init__(self, n):
        self.n = n
        self.__queue = list(range(1, n + 1))

    def fetch(self, k) -> int:
        index = k-1
        value = self.__queue[index]
        self.__queue.pop(index)
        self.__queue.append(value)
        return value
