class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            min_sofar = prices[0]
            max_difference = 0
            for item in prices[1:]:
                if item <= min_sofar:
                    min_sofar = item
                else:
                    max_difference = max(max_difference, item - min_sofar)
            return max_difference
        else:
            return 0


s = Solution()
print s.maxProfit([7, 6, 4, 3, 1])
