import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell, pre_sell, buy, pre_buy = 0, 0, int(-sys.maxint - 1), None
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell - price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + price, pre_sell)
        return sell


s = Solution()
print s.maxProfit([1, 2, 3, 0, 2])
