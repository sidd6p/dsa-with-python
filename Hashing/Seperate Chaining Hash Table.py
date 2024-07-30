class ChainingHashTable:
    def __init__(self, size):
        self.table = [None] * size

    def H(self, value):
        return value % len(self.table)

    def insert(self, value):
        key = self.H(value)
        if self.table[key] is None:
            self.table[key] = [value]
        else:
            self.table[key].append(value)

    def retrieve(self, value):
        """
        On average, retrieval function has a time complexity of O(ʎ).
        where,
        ʎ: load factor
        A successful retrieval takes around 1 + ʎ/2 time whereas a failed retrieval takes an average of 1 + ʎ time
        """
        key = self.H(value)
        value_chain = self.table[key]
        if value_chain is not None:
            for value_chain in value_chain:
                if value_chain == value:
                    return value
        return None
