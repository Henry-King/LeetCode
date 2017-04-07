class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [p for p in path.split("/") if p and p != "."]
        stack = []
        for item in places:
            if item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        return "/" + "/".join(stack)


s = Solution()
print s.simplifyPath("/...")
