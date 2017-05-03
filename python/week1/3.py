class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set()
        length = 0
        right = 0
        left = 0
        while right < len(s) and left < len(s):
            letter = s[right]
            if letter in chars:
                chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1
                length = max(length, right - left)
        return length


s = Solution()
print s.lengthOfLongestSubstring("gaaqfeqlqky")
