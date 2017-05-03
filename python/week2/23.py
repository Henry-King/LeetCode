# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists_len = len(lists)
        if lists_len == 0:
            return None
        elif lists_len == 1:
            return lists[0]
        else:
            list_a = self.mergeKLists(lists[:lists_len/2])
            list_b = self.mergeKLists(lists[lists_len/2:])
            ret = ListNode(None)
            pointer = ret
            while list_a and list_b:
                if list_a.val < list_b.val:
                    pointer.next = list_a
                    list_a = list_a.next
                else:
                    pointer.next = list_b
                    list_b = list_b.next
                pointer = pointer.next
            if list_a:
                pointer.next = list_a
            elif list_b:
                pointer.next = list_b
            return ret.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


s = Solution()
result = s.mergeKLists([None])
while result:
    print result.val
    result = result.next
