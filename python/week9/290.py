class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern and str:
            words = str.split()
            if len(words) == len(pattern):
                pattern_indexes = {}
                words_indexes = {}
                for i, (pattern_value, word_value) in enumerate(zip(pattern, words)):
                    if (pattern_value in pattern_indexes and word_value not in words_indexes) or \
                            (pattern_value not in pattern_indexes and word_value in words_indexes) or \
                            (pattern_value in pattern_indexes and word_value in words_indexes and pattern_indexes[
                                pattern_value] != words_indexes[word_value]):
                        return False
                    else:
                        pattern_indexes[pattern_value] = i
                        words_indexes[word_value] = i
                return True
            else:
                return False
        elif (pattern and not str) or (not pattern and str):
            return False
        else:
            return True
