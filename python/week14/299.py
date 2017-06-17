from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0, 0
        secret_dict, guess_dict = defaultdict(int), defaultdict(int)

        for secret_value, guess_value in zip(secret, guess):
            if secret_value == guess_value:
                bulls += 1
            else:
                secret_dict[secret_value] += 1
                guess_dict[guess_value] += 1

        for key in secret_dict:
            cows += min(secret_dict[key], guess_dict[key])

        return "{}A{}B".format(bulls, cows)


s = Solution()
print s.getHint("1123", "0111")
