class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        matrix = [[j if j > 0 else i for j in xrange(len(word2) + 1)] for i in xrange(len(word1) + 1)]

        for i in xrange(len(word1)):
            for j in xrange(len(word2)):
                if word1[i] == word2[j]:
                    matrix[i + 1][j + 1] = matrix[i][j]
                else:
                    matrix[i + 1][j + 1] = min(matrix[i][j + 1], matrix[i + 1][j], matrix[i][j]) + 1

        return matrix[len(word1)][len(word2)]
