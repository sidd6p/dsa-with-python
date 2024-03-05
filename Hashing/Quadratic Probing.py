class QuadraticProbing:
    def __init__(self, size):
        self.table = [None] * size

    def H(self, data, i):
        return (data + (i * i)) % len(self.table)

    def insert(self, data):
        i = 0
        idx = self.H(data, i)

        while self.table[idx] is not None:
            i += 1
            idx = self.H(data, i)

        self.table[idx] = data

    def retrieve(self, data):
        i = 0
        idx = self.H(data, i)

        while self.table[idx] is not None:
            if self.table[idx] == data:
                return data
            else:
                i += 1
                idx = self.H(data, i)

        return None
