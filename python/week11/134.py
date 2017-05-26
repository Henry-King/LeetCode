class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]l
        :type cost: List[int]
        :rtype: int
        """
        if gas and cost:
            start = total = tank = 0
            for i in xrange(len(gas)):
                tank += gas[i] - cost[i]
                if tank < 0:
                    start = i + 1
                    total += tank
                    tank = 0
            return -1 if tank + total < 0 else start
        return -1


s = Solution()
print s.canCompleteCircuit([4], [5])
