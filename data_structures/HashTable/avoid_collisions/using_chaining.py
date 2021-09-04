class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]  # To avoid collisions

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                print("del",index)
                del self.arr[h][index]

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

