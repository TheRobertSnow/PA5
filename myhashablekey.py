

class MyHashableKey:
    def __init__(self, int_value, str_value):
        self.int_value = int_value
        self.str_value = str_value

    def __eq__(self, other):
        first = hash(self)
        second = hash(other)
        if first == second:
            return True
        else:
            return False

    def __hash__(self):
        #   Return positive int
        myVar = 0
        for i in self.str_value:
            myVar += ord(i)
        return myVar + self.int_value * 13441


if __name__ == "__main__":
    k1 = MyHashableKey(1, "one")
    print(hash(k1))
    k2a = MyHashableKey(2, "two")
    print(hash(k2a))
    k2b = MyHashableKey(2, "two")
    print(hash(k2b))
    print(k1 == k2a)
    print(k2a == k2b)
