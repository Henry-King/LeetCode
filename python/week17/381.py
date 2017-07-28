from collections import defaultdict
import random


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num, self.pos = [], defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.num.append(val)
        self.pos[val].add(len(self.num) - 1)
        return len(self.pos[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        ret = False
        if self.pos[val]:
            ret = True
            delete_index = self.pos[val].pop()
            last_val = self.num[-1]
            self.num[delete_index] = last_val
            if self.pos[last_val]:
                self.pos[last_val].add(delete_index)
                self.pos[last_val].discard(len(self.num) - 1)
            self.num.pop()
        return ret

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.num[random.randint(0, len(self.num) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
obj.insert(0)
obj.remove(0)
obj.insert(-1)
obj.remove(Z)
# obj.insert(4)
# obj.insert(3)
# obj.insert(4)
# obj.insert(2)
# obj.insert(4)
# obj.remove(4)
# obj.remove(3)
# obj.remove(4)
# obj.remove(4)
# obj.getRandom()
