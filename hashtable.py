# Class for creating Hash Table data structure
class HashTable:
    # Initialize the list and set the capacity to 20 and the number of items added to 0
    def __init__(self, initial_capacity=10):
        self.list = [[] for _ in range(initial_capacity)]  # creates a list of empty lists
        self.num_items = 0

    # checks if the data has filled the list
    # if so, True is returned
    def need_rehash(self):
        return self.num_items / len(self.list) == 1.0

    # function to compute the index where the key-value pair should be stored
    def compute_hash(self, key):
        return hash(key) % len(self.list)

    # insert function to add a new key-value pair to the list
    # if rehash is needed, function to double the list size and rehash is called
    def insert(self, key, item):
        if self.need_rehash():
            self.double_table_size_and_rehash()
        bucket = self.compute_hash(key)
        for kv in self.list[bucket]:
            if kv[0] == key:
                kv[1] = item
                return True
        self.list[bucket].append([key, item])
        self.num_items += 1
        return True

    # function to double the size of the list and rehash all key-value pairs
    # old_table is saved, new list of double size is created and then all items are reinserted in new list
    def double_table_size_and_rehash(self):
        old_list = self.list
        self.list = [[] for _ in range(2 * len(old_list))]
        self.num_items = 0
        for bucket_list in old_list:
            for kv in bucket_list:
                self.insert(kv[0], kv[1])

    # function to find the index of the value in the bucket for a given key
    # return the index if found, None otherwise
    def find_value_index(self, bucket, key):
        for i, kv in enumerate(self.list[bucket]):
            if kv[0] == key:
                return i
        return None

    # function to search and return the value for a given key
    # the return value is None if key is not found, else value corresponding to the key
    def search(self, key):
        bucket = self.compute_hash(key)
        bucket_list = self.list[bucket]
        for kv in bucket_list:
            if key == kv[0]:
                return kv[1]
        return None

    # function to remove a key-value pair from the list
    # the key-value pair at the given index in the bucket is removed
    def remove(self, key):
        bucket = self.compute_hash(key)
        index = self.find_value_index(bucket, key)
        if index is not None:
            del self.list[bucket][index]

    # function to format and print the hashtable as a list of buckets with its index and values
    def __str__(self):
        s = "   --------\n"
        for index, item in enumerate(self.list):
            value = str(item) if item else ' Empty'
            s += str(index) + value.center(6) + '\n'
        s += "   --------"
        return s

# C950 - Webinar-1 - Let’s Go Hashing
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Pulled some repeating code out into own functions and added self adjusting rehash functions and checks
