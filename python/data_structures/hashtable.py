from data_structures.linked_list import LinkedList, Node


class Hashtable:
    """
    Put docstring here
    """
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):

        hash = 0

        for char in key:
            hash += ord(char)

        hash = (hash * 19) % self.size

        return hash

    def set(self, key, value):

        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        if not bucket:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].insert([key, value])

    def get(self, key):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]

        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        raise KeyError(f'key not found: {key}')

    def has(self, key):
        idx = self._hash(key)

        if self._buckets[idx]:

            if self._buckets[idx].head.value[0] == key:
                return True

            else:
                current = self._buckets[idx].head

            while current:
                if current.value[0] == key:
                    return True
                current = current.next

        return False

    def keys(self):
        keys = []
        for item in self._buckets:
            if item:
                current = item.head
                while current:
                    keys.append(current.value[0])
                    current = current.next
        return keys


if __name__ == "__main__":
    ht_1 = Hashtable()
    ht_1.set('name', 'ADAM')
    print(ht_1.get('name'))
    print(ht_1.has('name'))
    print(ht_1.keys())

