class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        directory = []
        while i < len(path):
            if path[i] == '/':
                self.__process_dir(directory, stack)
            else:
                directory.append(path[i])
            i += 1

        self.__process_dir(directory, stack)

        ret = []
        if stack:
            for item in stack:
                ret.append("/")
                ret.append(item)
        else:
            ret.append("/")

        return "".join(ret)

    def __process_dir(self, directory, stack):
        if directory == ['.']:
            pass
        elif directory == ['.', '.']:
            if stack:
                stack.pop()
        elif directory:
            stack.append("".join(directory))

        del directory[:]


s = Solution()
print s.simplifyPath("/...")
