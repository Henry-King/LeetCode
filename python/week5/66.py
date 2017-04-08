class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        index = len(digits) - 1
        while carry and index >= 0:
            digit = digits[index]
            carry, digits[index] = divmod(digit + carry, 10)
            index -= 1
        if carry:
            digits = [1] + digits
        return digits


s = Solution()
print s.plusOne([1, 0])
