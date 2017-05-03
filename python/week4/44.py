class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_length = len(s)
        p_length = len(p)
        s_pointer, p_pointer = 0, 0
        s_match_index, p_match_index = -1, -1
        while s_pointer < s_length:
            if (p_pointer < p_length) and (s[s_pointer] == p[p_pointer] or p[p_pointer] == '?'):
                s_pointer += 1
                p_pointer += 1
            elif p_pointer < p_length and p[p_pointer] == '*':
                s_match_index = s_pointer
                p_match_index = p_pointer
                p_pointer += 1
            elif s_match_index != -1:
                s_match_index += 1
                s_pointer = s_match_index
                p_pointer = p_match_index + 1
            else:
                return False

        while p_pointer < p_length and p[p_pointer] == '*':
            p_pointer += 1
        return p_pointer == p_length


s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("aa", "aa")
print s.isMatch("aaa", "aa")
print s.isMatch("aa", "*")
print s.isMatch("aa", "a*")
print s.isMatch("ab", "?*")
print s.isMatch("aab", "c*a*b")
print s.isMatch("a", "")
print s.isMatch("mississippi", "m*issi*iss*")
print s.isMatch("", "*")
print s.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b")
print s.isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa",
                "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****")
