class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount:
            res = [-1] * (amount + 1)
            for coin in coins:
                if coin < len(res):
                    res[coin] = 1

            for i in range(1, len(res)):
                for coin in coins:
                    if i - coin >= 0 and res[i - coin] > 0:
                        res[i] = min(res[i - coin] + 1, res[i]) if res[i] > 0 else res[i - coin] + 1

            return res[-1]
        else:
            return 0


s = Solution()
print s.coinChange([1, 2, 5], 11)
