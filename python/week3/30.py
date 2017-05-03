import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_num = len(words)
        word_length = len(words[0])
        ret = []
        counter = collections.Counter(words)

        for i in xrange(0, len(s) - word_num * word_length + 1):
            copy = dict(counter)
            for j in xrange(len(words)):
                scan = s[i + j * word_length: i + j * word_length + word_length]
                if scan in copy:
                    times = copy[scan]
                    if times > 1:
                        copy[scan] -= 1
                    else:
                        del copy[scan]
                else:
                    break

                if not copy:
                    ret.append(i)
        return ret


s = Solution()
print s.findSubstring("wordgoodgoodgoodbestword",
                      ["word", "good", "best", "good"])
