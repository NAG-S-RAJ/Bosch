class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key {key} not found")

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key {key} not found")


hm = HashMap()
hm.put("apple", 1)
hm.put("banana", 2)
print("Get apple:", hm.get("apple"))
hm.put("apple", 3)
print("Get apple after update:", hm.get("apple"))
hm.remove("banana")
try:
    print(hm.get("banana"))
except KeyError as e:
    print(e)
