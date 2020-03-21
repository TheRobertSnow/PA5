class BucketItem:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class Bucket:
    def __init__(self):
        self.bucket = []

    def insert(self, key, data):
        itemExists = self.contains(key)
        if itemExists:
            raise ItemExistsException()
        else:
            item = BucketItem(key, data)
            self.bucket.append(item)

    def update(self, key, data):
        itemExists = self.contains(key)
        if itemExists:
            for item in self.bucket:
                if item.key == key:
                    item.data = data
        else:
            raise NotFoundException()

    def find(self, key):
        item = None
        for i in self.bucket:
            if i.key == key:
                item = i.data
        if item != None:
            return item
        else:
            raise NotFoundException()

    def contains(self, key):
        for item in self.bucket:
            if item.key == key:
                return True
        return False

    def remove(self, key):
        item = self.contains(key)
        if item:
            self.bucket.remove(item)
        else:
            raise NotFoundException()

    def __setitem__(self, key, data):
        try:
            self.insert(key, data)
        except ItemExistsException:
            item = self.find(key)
            item.data = data

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        counter = 0
        for i in self.bucket:
            counter += 1
        return counter



if __name__ == "__main__":
    bucket = Bucket()

    bucket.insert(12, "Hello Mr. Bob")
    bucket.insert(15, "Mr. Jeff")
    bucket[8] = "Something"
    bucket.update(15, "i love refrigerators")
    print(len(bucket))
    print(bucket.find(12))
    myItem = bucket[15]
    print(myItem)
    print("Print all:")
    for i in bucket.bucket:
        print(i.key, i.data)
