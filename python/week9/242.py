from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counter = Counter(s)
        t_counter = Counter(t)
        if s_counter == t_counter:
            return True
        else:
            return False
