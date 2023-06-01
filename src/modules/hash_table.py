import random

import tabulate


class Pair:
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second
        self.used = False

    def is_empty(self):
        if self.first is None or self.second is None:
            return True
        return False

    def __str__(self):
        return f'({self.first} -> {self.second})'


class HashTable:
    def __init__(self):
        self.max_size = 20
        self.size = 0
        self.koef = 1.7
        self.data = []
        for i in range(self.max_size):
            self.data.append(Pair())

    def __str__(self):
        ret_string = ''
        for i in self.data:
            ret_string += str(i) + '\n'
        return ret_string

    def print(self):
        head = ['key', 'value']
        arr = []
        for i in range(self.max_size):
            arr.append([str(self.data[i].first), str(self.data[i].second)])
        print(tabulate.tabulate(arr, headers=head, tablefmt="outline"))

    def expand_table(self):
        for i in range(self.max_size):
            self.data.append(Pair())
        self.max_size *= 2

    def hash_func_1(self, x):
        return x % self.max_size

    def hash_func_2(self, x):
        #return x % (self.max_size - 1) + 1
        return (7 - x % 7) % self.max_size

    def double_hash(self, x, i):
        return (self.hash_func_1(x) + i * self.hash_func_2(x)) % self.max_size

    def find_place(self, key):
        find_ind = 0
        ind = self.double_hash(key, find_ind)

        found = False
        while not found and find_ind <= self.max_size:
            if self.data[ind].is_empty():
                found = True
            else:
                find_ind += 1
                ind = self.double_hash(key, find_ind)
        return ind

    def insert(self, key, value):
        ind = self.find_elem(key)
        if ind == -1:
            ind = self.find_place(key)

        self.data[ind].used = False
        self.data[ind].first = key
        self.data[ind].second = value

        self.size += 1
        if self.max_size < self.size * self.koef:
            self.expand_table()

    def find_elem(self, key):
        find_ind = 0
        ind = self.double_hash(key, find_ind)

        found = False
        flag = -1
        while not found and find_ind <= self.max_size:
            if self.data[ind].first == key:
                found = True
                flag = ind
            else:
                find_ind += 1
                ind = self.double_hash(key, find_ind)
        return flag

    def find(self, key):
        ind = self.find_elem(key)
        if ind == -1:
            return 'Not Found'
        return self.data[ind].second

    def remove(self, key):
        ind = self.find_elem(key)
        if ind == -1:
            return 'Cannot be deleted'
        else:
            self.data[ind].first = None
            self.data[ind].second = None
            self.data[ind].used = True


