import string


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        result = []
        if wordList and endWord in wordList:
            wordList = set(wordList)
            queue = {beginWord}
            connection = {}
            done = False
            while queue and not done:
                next_queue = set()
                map(wordList.remove, filter(lambda foo: foo in wordList, queue))

                for word in queue:
                    word_separated = list(word)
                    for index in xrange(len(word_separated)):
                        for letter in string.ascii_lowercase:
                            original_letter, word_separated[index] = word_separated[index], letter
                            new_word = "".join(word_separated)
                            next_level = connection[word] if word in connection else set()

                            if new_word == endWord:
                                done = True
                                next_level.add(new_word)
                                connection[word] = next_level
                            elif new_word != word and new_word in wordList:
                                next_queue.add(new_word)
                                next_level.add(new_word)
                                connection[word] = next_level
                            word_separated[index] = original_letter
                if done:
                    break
                else:
                    queue = next_queue

            if done and connection:
                def generator(start, temp):
                    if start == endWord:
                        result.append(temp[:])
                    elif start in connection:
                        for middle_word in connection[start]:
                            temp.append(middle_word)
                            generator(middle_word, temp)
                            temp.pop()

                generator(beginWord, [beginWord])
        return result


s = Solution()
print s.findLadders("hit",
                    "cog",
                    ["hot", "dot", "dog", "lot", "log", "cog"])
