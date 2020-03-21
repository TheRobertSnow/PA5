import bucket, hashmap


class MyHashableKey:
    def __init__(self, int_value, str_value):
        self.buck = bucket.Bucket()
        self.hash = hashmap.HashMap()

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass
