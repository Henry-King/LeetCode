class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        value2index = {}
        for index, value in enumerate(nums):
            if value in value2index:
                pre_index = value2index[value]
                if abs(pre_index - index) > k:
                    value2index[value] = index
                else:
                    return True
            else:
                value2index[value] = index

        return False
