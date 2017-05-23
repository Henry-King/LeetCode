from collections import deque
import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if wordList and endWord in wordList:
            wordList = set(wordList)
            visited = {beginWord}
            queue = deque([beginWord, None])
            level = 1
            while queue:
                value = queue.popleft()
                if value:
                    word_list = list(value)
                    for index in xrange(len(word_list)):
                        for letter in string.ascii_lowercase:
                            original_letter, word_list[index] = word_list[index], letter
                            word = "".join(word_list)
                            if word == endWord:
                                return level + 1
                            elif word in wordList and word not in visited:
                                visited.add(word)
                                queue.append(word)
                            word_list[index] = original_letter
                else:
                    level += 1
                    if queue:
                        queue.append(None)
        return 0


s = Solution()
print s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
