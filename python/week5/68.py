class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line, ret = [], []
        line_word_num = 0
        for word in words:
            if len(word) + len(line) + line_word_num > maxWidth:
                temp_line = []
                spaces = self.__compute_space(maxWidth, line_word_num, len(line))
                for i, j in zip(line, spaces):
                    temp_line.append(i)
                    temp_line.append(j)
                ret.append("".join(temp_line))
                line_word_num = 0
                del line[:]
            line_word_num += len(word)
            line.append(word)
        if line:
            ret.append(" ".join(line).ljust(maxWidth))
        return ret

    def __compute_space(self, maxWidth, line_word_num, word_num):
        ret = []
        space_num = maxWidth - line_word_num
        if word_num == 1:
            ret.append(" " * space_num)
        else:
            average_space = space_num / (word_num-1)
            left_out_space = space_num - average_space * (word_num-1)
            for i in xrange(word_num - 1):
                count = average_space
                if left_out_space:
                    count += 1
                    left_out_space -= 1
                ret.append(" " * count)
            ret.append("")
        return ret


s = Solution()
print s.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."],
                    6)
