class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, data):
        if self.is_full():
            return
        else:
            idx = self.front + self.count
            self.queue[idx] = data
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            return
        else:
            self.queue[self.front] = None
            self.count -= 1
            self.front = (self.front + 1) % self.size
