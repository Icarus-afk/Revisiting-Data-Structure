class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def __len__(self):
        return self.size

    # O(1) average case, O(n) worst case
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return True
        return False

    # O(1) average case, O(n) worst case
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        else:
            bucket.append((key, value))
            self.size += 1

    # O(1) average case, O(n) worst case
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key {key} not found in HashMap.")

    # O(1) average case, O(n) worst case
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError(f"Key {key} not found in HashMap.")

    # O(n) time complexity
    def keys(self):
        keys_list = []
        for bucket in self.buckets:
            for k, v in bucket:
                keys_list.append(k)
        return keys_list

    # O(n) time complexity
    def values(self):
        values_list = []
        for bucket in self.buckets:
            for k, v in bucket:
                values_list.append(v)
        return values_list

    # O(n) time complexity
    def items(self):
        items_list = []
        for bucket in self.buckets:
            for k, v in bucket:
                items_list.append((k, v))
        return items_list

    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0
        for char in key_string:
            hash_result = (hash_result * 31 + ord(char)) % self.capacity
        return hash_result


if __name__ == "__main__":
    hashmap = HashMap(10)
    hashmap.put("apple", 1)
    hashmap.put("banana", 2)
    hashmap.put("orange", 3)
    hashmap.put("strawberry", 4)

    print(hashmap.get("apple"))  # Output: 1
    print(hashmap.get("banana"))  # Output: 2
    print(hashmap.get("orange"))  # Output: 3
    print(hashmap.get("strawberry"))  # Output: 4

    print(hashmap.keys())  # Output: ['apple', 'banana', 'orange', 'strawberry']
    print(hashmap.values())  # Output: [1, 2, 3, 4]
    print(
        hashmap.items()
    )  # Output: [('apple', 1), ('banana', 2), ('orange', 3), ('strawberry', 4)]
    hashmap.remove("banana")
    print(hashmap.get("banana"))  # Raises KeyError: Key banana not found in HashMap.
