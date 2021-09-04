class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
           
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)


if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 130
    t['march 7'] = 140
    t['march 8'] = 150
    t['march @'] = 248
    t['march   '] = 260
    t['march   '] = 456
    t['march 1'] = 451
    t['march 2'] = 452
    t['march 3'] = 453
    t['march 4'] = 454
    t['march 5'] = 400
    t['march 0'] = 500
    print(t.arr)
    print(t['march 6'])
    print(t['march 7'])
    print(t['march 8'])
    print(t['march @'])
    print(t['march   '])
    print(t.arr)
    del t['march   ']
    print(t.arr)
