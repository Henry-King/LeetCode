class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            profit = 0
            min_so_far = prices[0]
            for index in xrange(1, len(prices)):
                if prices[index] < prices[index - 1]:
                    profit += prices[index - 1] - min_so_far
                    min_so_far = prices[index]

            if prices[-1] > min_so_far:
                profit += prices[-1] - min_so_far

            return profit
        else:
            return 0


s = Solution()
print s.maxProfit([1, 2])
