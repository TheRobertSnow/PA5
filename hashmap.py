from bucket import *


class HashMap:
    def __init__(self):
        self.size = 16
        self.items = 0
        self.bucket_list = [Bucket() for _ in range(self.size)]

    def insert(self, key, data):
        k = self.contains(key)
        if k == True:
            raise ItemExistsException()
        else:
            newKey = self.compress(key)
            self.bucket_list[newKey].insert(key, data)
            self.items += 1


    def update(self, key, data):
        pos = self.compress(key)
        if self.contains(key):
            self.bucket_list[pos].update(key, data)
        else:
            raise NotFoundException()

    def find(self, key):
        pos = self.compress(key)
        if self.contains(key):
            data = self.bucket_list[pos].find(key)
            return data
        else:
            raise NotFoundException()

    def contains(self, key):
        k = self.compress(key)
        if self.bucket_list[k].contains(key):
            return True
        return False

    def remove(self, key):
        pos = self.compress(key)
        if self.bucket_list[pos].contains(key):
            self.bucket_list[pos].remove(key)
            self.items -= 1
        else:
            raise NotFoundException()

    def __setitem__(self, key, data):
        pos = self.compress(key)
        if self.bucket_list[pos].contains(key):
            self.bucket_list[pos].update(key, data)
        else:
            self.bucket_list[pos].insert(key, data)
            self.items += 1

    def __getitem__(self, key):
        pos = self.compress(key)
        if self.bucket_list[pos].contains(key):
            return self.bucket_list[pos].find(key)
        else:
            raise NotFoundException()

    def __len__(self):
        items = 0
        for i in self.bucket_list:
            items += len(i)
        return items

    def compress(self, key):
        return key % self.size


if __name__=="__main__":
    hmap = HashMap()
    hmap.insert(15, "Hello")
    hmap.insert(120, "There!")
    hmap.insert(77, "Kenobi")
    print(hmap.find(15))
    print(hmap.find(120))
    print(hmap.find(77))
    try:
        print(hmap.find(17))
    except Exception as e:
        print(e)

    newitem = hmap[15]
    print(newitem)
    hmap[12] = "I'm Bob"
    print(hmap.find(12))

    hmap.update(77, "Ah, General Kenobi!")
    print(hmap.find(15), hmap.find(120), hmap.find(77))

    print(len(hmap))
