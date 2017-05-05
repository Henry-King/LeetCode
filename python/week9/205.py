class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for i, (s_value, t_value) in enumerate(zip(s, t)):
            if (s_value in s_dict and t_value not in t_dict) or \
                    (s_value not in s_dict and t_value in t_dict) or \
                    (s_value in s_dict and t_value in t_dict and s_dict[s_value] != t_dict[t_value]):
                return False
            else:
                s_dict[s_value] = i
                t_dict[t_value] = i
        return True


s = Solution()
print s.isIsomorphic("foo", "bar")
