class LinearProbingHashTable:
    def __init__(self, size):
        self.table = [None] * size

    def H(self, value, i):
        return (value + i) % len(self.table)

    def insert(self, value):
        i = 0
        idx = self.H(value, i)

        while self.table[idx] is not None:
            i += 1
            idx = self.H(value, i)

        self.table[idx] = value

    def retrieve(self, value):
        """
        With a low load factor, the hash table is less crowded, resulting in an average-case retrieval complexity close to O(1).
        As the load factor increases, the efficiency of retrieval operations decreases, approaching O(n) in the worst case.
        """

        i = 0
        idx = self.H(value, i)

        while self.table[idx] is not None:
            if self.table[idx] == value:
                return value
            else:
                i += 1
                idx = self.H(value, idx)

        return None
