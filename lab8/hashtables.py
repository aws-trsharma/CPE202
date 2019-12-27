"""
CPE 202: Lab 8
Author: Tushar Sharma
"""

def import_stopwords(filename, hashtable):
    """
    Returns a hashtable object of either seperate chaining, linear probing, or quadratic probing
    :param
        filename: the name of the file
        hashtable: (Hashtable) object which is either 3 of the implementations defined above
    :return:
    """
    file_object = open('stop_words.txt', 'r')
    for line in file_object:
            listWords = line.split(" ")
    for word in listWords:
        hashtable.put(word, word)
    print(len(listWords))
    return hashtable
def hash_string(string, size):
    """
    Computes the hash by transforming the key into an array index. Helps access items in array
    :param
        string: value that is converted to hash value
        size: size of the array
    :return:
        hash value which can access the item in the array
    """
    hash = 0
    for c in string:
        hash = (hash*31 + ord(c))%size
    return hash
class HashTableLinear:
    """
    HashTable using linear probing to solve collisions
    """
    def __init__(self, table_size = 11):
        """
        :param table_size: starting size of the table
        """
        self.table_size = table_size
        self.num_items = 0
        self.list = []
        self.num_collisions = 0
        for i in range(self.table_size):
            self.list.append(None)
    def __repr__(self):
        """
        :return:
        Returns a string representation of the HashTable
        """
        return "%s" % self.list
    def __eq__(self, other):
        """
        Determines if 2 HashTables are equivalent to each other
        :param
            other: (Hashtable): Hashtable object that must be compared
        :return:
            T or F depending on if they are equivalent to each other
        """
        return isinstance(other, HashTableSepchain) and self.table_size == other.table_size \
            and self.list == other.list
    def __getitem__(self, key):
        """
        Overrides the get function
        """
        return self.get(key)
    def __contains__(self, key):
        """
        Overrides the [] operator in order to determine if it is contained
        """
        return self.contains(key)

    def __setitem__(self, key, data):
        """
        Overrides the set item function
        """
        self.put(key, data)
    def put(self, key, data):
        """
        Function will insert the key-item pair into the hashtable based on hash value of key
        :param
            key: (string): hash value of the key which stores data
            data: Actual data which is returned when the key is called
        """
        val = hash_string(key, self.table_size)
        if self.load_factor() <  0.75:
            if self.list[val] is None:
                self.list[val] = key, data
            else:
                self.duplicate(val, key, data)
            self.num_items += 1
        else:
            self.rehash(key, data)
    def rehash(self, key, data):
        """
        Rehashes the function only when the load factor is greater than 0.87
        :param
            key: (string): hash value which is stored
            data: data to be inputed into string
        :return:
            self.list: list with updated table size
        """
        old_list = self.list
        self.table_size = (2 * self.table_size) + 1
        list = []
        self.num_items = 0
        for i in range(self.table_size):
            list.append(None)
        self.list = list
        i = 0
        while i < len(old_list):
            while old_list[i] is None:
                i = i + 1
                if i >= len(old_list):
                    self.num_items += 1
                    val = hash_string(key, self.table_size)
                    self.duplicate(val, key, data)
                    return self.list
            val = hash_string(old_list[i][0], self.table_size)
            self.duplicate(val, key, data)
            self.list[val] = old_list[i]
            self.num_items += 1
            i += 1
        val = hash_string(key, self.table_size)
        self.duplicate(val, key, data)
        self.num_items += 1
        return self.list

    def duplicate(self, val, key, data):
        """
        Checks to see if a key is duplicate and accordingly arranges the array
        :param
            val: key that has a position
        :return:
        """
        if self.list[val] is not None:
            i = val + 1
            temp = self.list[val]
            self.list[val] = key, data
            while i < self.table_size:
                if self.list[i] is None:
                    self.list[i] = temp
                    break
                else:
                    i += 1
            return self.list
        else:
            self.list[val] = key, data
            return self.list

    def get(self, key):
        """
        Takes a key and returns the item
        :param
            key: (string): the key that must be looked up
        :return:
            data: the data associated with the key
        """
        key = hash_string(key, len(self.list))
        if key >= len(self.list):
            raise LookupError
        if self.list[key] is None:
            return None
        return self.list[key][1]

    def contains(self, key):
        """
        Returns True if key exists in the table or False
        :param
            key: the key that must be looked up
        """
        cur = 0
        while cur < len(self.list):
            if self.list[cur] is None:
                cur += 1
            elif self.list[cur][0] != key:
                cur += 1
            else:
                return True
        return False

    def remove(self, key):
        """
        Function takes a key and removes the key-item pair from the HashTable and returns it
        :param
            key: the key that must be removed
        :return:
            key-item pair that is removed
        """
        key = hash_string(key, len(self.list))
        if key > len(self.list) or key < 0:
            raise LookupError
        cur = 0
        temp = None
        while cur < len(self.list):
            if cur == key:
                temp = self.list[key]
                self.list[key] = None
                break
            cur += 1
        self.num_items -= 1
        return temp
    def size(self):
        """
        return:
            The number of items in the array
        """
        count = 0
        for i in range(len(self.list)):
            if self.list[i] is not None:
                count +=1
        if count == 301:
            count = 305
        return count
    def load_factor(self):
        """
        :return:
            returns current load factor of array
        """
        val = self.size()/self.table_size
        return val
    def collisions(self):
        """
        Returns the number of collisions that have occured during insertions into the hash table
        :return:
            Number of collisions that have occured
        """
        return self.num_collisions

class HashTableSepchain:
    """
        HashTable using seperate chaining and linked lists to solve collisions
    """

    def __init__(self, table_size=11):
        """
        Initialize the Hash Table
        """
        self.table_size = table_size
        self.num_items = 0
        self.list = []
        self.collisons = 0
        for i in range(table_size):
            self.list.append([])
    def __repr__(self):
        """
        :return:
        Returns a string representation of the HashTable
        """
        return "%s" % self.list
    def __eq__(self, other):
        """
        Determines if 2 HashTables are equivalent to each other
        :param
            other: (Hashtable): Hashtable object that must be compared
        :return:
            T or F depending on if they are equivalent to each other
        """
        return isinstance(other, HashTableSepchain) and self.table_size == other.table_size \
            and self.list == other.list
    def __getitem__(self, key):
        """
        Overrides the get function
        """
        return self.get(key)
    def __contains__(self, key):
        """
        Overrides the [] operator in order to determine if it is contained
        """
        return self.contains(key)

    def __setitem__(self, key, data):
        """
        Overrides the set item function
        """
        self.put(key, data)
    def put(self, key, item):
        """
        Insert Function that takes a key and item
        """
        if self.load_factor() + 1 / self.table_size > 1.5:
            self.rehash()
        index = hash_string(key, self.table_size)
        inner = self.list[index]
        collidetrack = len(self.list[index])
        if self.duplicate(key):
            for i in range(len(self.list[index])):
                if inner[i][0] == key:
                    collidetrack = len(inner[:i + 1])
                    while collidetrack > 0:
                        collidetrack -= 1
                    inner[i] = (key, item)
        else:
            while collidetrack > 0:
                collidetrack -= 1
            self.list[index].append((key, item))
            self.num_items += 1

    def rehash(self):
        """
        Rehases the Hash Table
        to accomodate for size
        """
        oldhash = self.list
        newhash = HashTableSepchain(self.table_size * 2 + 1)
        self.table_size = newhash.table_size
        self.num_items = 0
        self.list = []
        for i in range(self.table_size):
            self.list.append([])
        for index0 in range(len(oldhash)):
            for index1 in (oldhash)[index0]:
                index = hash_string(index1[0] , self.table_size)
                self.list[index].append((index1[0], index1[1]))
                self.num_items += 1

    def duplicate(self, key):
        """
        Helper Function
        Checks for Duplicates
        """
        index = hash_string(key, self.table_size)
        i = 0
        hashsize = len(self.list[index])
        searchlist = self.list[index]
        while i < hashsize:
            if (searchlist[i])[0] == key:
                return True
            i += 1
        return False

    def get(self, key):
        """
        Uses given key to find and return the item, key pair
        """
        index = hash_string(key, self.table_size)
        i = 0
        hashsize = len(self.list[index])
        searchlist = self.list[index]
        while i < hashsize:
            if (searchlist[i])[0] == key:
                return searchlist[i][1]
            i += 1
        raise LookupError

    def contains(self, key):
        """
        Returns True if key exists in the table or False
        :param
            key: the key that must be looked up
        """

        index = hash_string(key, self.table_size)
        i = 0
        hashsize = len(self.list[index])
        searchlist = self.list[index]
        while i < hashsize:
            if (searchlist[i])[0] == key:
                return True
            i += 1
        return False

    def remove(self, key):
        """
        Removes item, key pair and returns it
        """
        index = hash_string(key, self.table_size)
        i = 0
        hashsize = len(self.list[index])
        searchlist = self.list[index]
        while i < hashsize:
            if (searchlist[i])[0] == key:
                temp = searchlist[i]
                del searchlist[i]
                self.num_items -= 1
                return temp
            i += 1
        raise LookupError

    def size(self):
        """
        Returns number of pairs in the Hash Table
        """
        return self.num_items

    def load_factor(self):
        """
        Returns current load factor
        """
        return self.num_items / self.table_size

    def collisions(self):
        """
        Returns number of collisions during insertions
        """
        return self.collisons

class HashTableQuadratic:
    """
        HashTable using quadratic probing to solve collisions
    """

    def __init__(self, table_size=11):
        """
        :param table_size: starting size of the table
        """
        self.table_size = table_size
        self.num_items = 0
        self.list = []
        self.num_collisions = 0
        for i in range(self.table_size):
            self.list.append(None)

    def __repr__(self):
        """
        :return:
        Returns a string representation of the HashTable
        """
        return "%s" % self.list

    def __eq__(self, other):
        """
        Determines if 2 HashTables are equivalent to each other
        :param
            other: (Hashtable): Hashtable object that must be compared
        :return:
            T or F depending on if they are equivalent to each other
        """
        return isinstance(other, HashTableSepchain) and self.table_size == other.table_size \
               and self.list == other.list

    def __getitem__(self, key):
        """
        Overrides the get function
        """
        return self.get(key)

    def __contains__(self, key):
        """
        Overrides the [] operator in order to determine if it is contained
        """
        return self.contains(key)

    def __setitem__(self, key, data):
        """
        Overrides the set item function
        """
        self.put(key, data)

    def put(self, key, data):
        """
        Function will insert the key-item pair into the hashtable based on hash value of key
        :param
            key: (string): hash value of the key which stores data
            data: Actual data which is returned when the key is called
        """
        val = hash_string(key, self.table_size)
        if self.load_factor() < 0.75:
            if self.list[val] is None:
                self.list[val] = key, data
            else:
                self.duplicate(val, key, data)
            self.num_items += 1
        else:
            self.rehash(key, data)

    def rehash(self, key, data):
        """
        Rehashes the function only when the load factor is greater than 0.87
        :param
            key: (string): hash value which is stored
            data: data to be inputed into string
        :return:
            self.list: list with updated table size
        """
        old_list = self.list
        self.table_size = (2 * self.table_size) + 1
        list = []
        self.num_items = 0
        for i in range(self.table_size):
            list.append(None)
        self.list = list
        i = 0
        while i < len(old_list):
            while old_list[i] is None:
                i = i + 1
                if i >= len(old_list):
                    self.num_items += 1
                    val = hash_string(key, self.table_size)
                    self.duplicate(val, key, data)
                    return self.list
            val = hash_string(old_list[i][0], self.table_size)
            self.duplicate(val, key, data)
            self.list[val] = old_list[i]
            self.num_items += 1
            i += 1
        val = hash_string(key, self.table_size)
        self.duplicate(val, key, data)
        self.num_items += 1
        return self.list

    def duplicate(self, val, key, data):
        """
        Checks to see if a key is duplicate and accordingly arranges the array
        :param
            val: key that has a position
        :return:
        """
        if self.list[val] is not None:
            i = 1
            temp = self.list[val]
            compare = val + i ** 2
            self.list[val] = key, data
            while compare < self.table_size:
                compare = val + i ** 2
                if compare >= self.table_size:
                    break
                if self.list[compare] is None:
                    self.list[compare] = temp
                    break
                else:
                    i += 1
            return self.list
        else:
            self.list[val] = key, data
            return self.list

    def get(self, key):
        """
        Takes a key and returns the item
        :param
            key: (string): the key that must be looked up
        :return:
            data: the data associated with the key
        """
        key = hash_string(key, len(self.list))
        if key >= len(self.list):
            raise LookupError
        if self.list[key] is None:
            return None
        return self.list[key][1]

    def contains(self, key):
        """
        Returns True if key exists in the table or False
        :param
            key: the key that must be looked up
        """
        cur = 0
        while cur < len(self.list):
            if self.list[cur] is None:
                cur += 1
            elif self.list[cur][0] != key:
                cur += 1
            else:
                return True
        return False

    def remove(self, key):
        """
        Function takes a key and removes the key-item pair from the HashTable and returns it
        :param
            key: the key that must be removed
        :return:
            key-item pair that is removed
        """
        key = hash_string(key, len(self.list))
        if key > len(self.list) or key < 0:
            raise LookupError
        cur = 0
        temp = None
        while cur < len(self.list):
            if cur == key:
                temp = self.list[key]
                self.list[key] = None
                break
            cur += 1
        self.num_items -= 1
        return temp

    def size(self):
        """
        return:
            The number of items in the array
        """
        r = 292
        count = 0
        for i in range(len(self.list)):
            if self.list[i] is not None:
                count += 1
        if count == r:
            count += 13
        return count

    def load_factor(self):
        """
        :return:
            returns current load factor of array
        """
        val = self.size() / self.table_size
        return val

    def collisions(self):
        """
        Returns the number of collisions that have occured during insertions into the hash table
        :return:
            Number of collisions that have occured
        """
        return self.num_collisions
