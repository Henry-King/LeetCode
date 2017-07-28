import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num, self.pos = [], {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = False
        if val not in self.pos:
            self.num.append(val)
            self.pos[val] = len(self.num) - 1
            ret = True
        return ret

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        ret = False
        if val in self.pos:
            delete_index = self.pos[val]
            last_num = self.num[-1]
            self.num[delete_index] = last_num
            self.pos[last_num] = delete_index
            self.num.pop()
            self.pos.pop(val)
            ret = True
        return ret

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.num[random.randint(0, len(self.num) - 1)]



        # Your RandomizedSet object will be instantiated and called as such:


obj = RandomizedSet()
param_1 = obj.insert(3)
param_2 = obj.remove(3)
param_3 = obj.remove(0)
param_4 = obj.insert(3)
param_5 = obj.getRandom()
param_6 = obj.remove(3)
