class ModulusHashing:

    def __init__(self) -> None:
        self.table = [None] * 10
    
    def get_load_factor(self):
        occupied_slots = sum(1 for slot in self.table if slot is not None)
        return occupied_slots / len(self.table)

    def H(self, data):
        return data % len(self.table)

    def insert(self, data):
        idx = self.H(data)
        self.table[idx] = data
        if self.get_load_factor() > 0.5:
            self.rehash()
    
    def rehash(self):
        new_size = 2 * len(self.table)
        new_table = [None] * new_size
        for data in self.table:
            if data is not None:
                new_idx = data % new_size
                new_table[new_idx] = data 
        self.table = new_table
    
    def retrieve(self, key):
        idx = self.H(key)
        if idx < len(self.table):
            return self.table[idx]
        else:
            return None