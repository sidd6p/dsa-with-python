class DoubleHashing:
    def __init__(self, size):
        self.table = [None] * size

    def H1(self, data):
        return data % len(self.table)

    def H2(self, data):
        return 1 + (data % (len(self.table) - 1))

    def H(self, data, i):
        return self.H1(data) + (i * self.H2(data))

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
