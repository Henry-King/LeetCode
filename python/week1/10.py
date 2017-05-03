class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        else:
            dfa = self.__gen_dfa(p)
            return dfa.move(s, 0)

    def __gen_dfa(self, p):
        dfa = []
        p_pos = 0
        while p_pos < len(p):
            letter = p[p_pos]
            if letter == '.':
                if p_pos + 1 < len(p) and p[p_pos + 1] == '*':
                    dfa.append(State('wildcard', 'any'))
                    p_pos += 1
                else:
                    dfa.append(State('wildcard', 'once'))
            else:
                if p_pos + 1 < len(p) and p[p_pos + 1] == '*':
                    dfa.append(State('letter', 'any', letter))
                    p_pos += 1
                else:
                    dfa.append(State('letter', 'once', letter))
            p_pos += 1

        def link(x, y):
            x.next_state = y
            return y

        reduce(link, dfa)
        return dfa[0]


class State:
    def __init__(self, token, repeat, value=None, next_state=None):
        self.token = token
        self.repeat = repeat
        self.next_state = next_state
        self.value = value

    def move(self, original_str, pos):
        if pos >= len(original_str):
            p = self
            if p.repeat == 'any':
                while p.next_state is not None:
                    if p.repeat != 'any':
                        return False
                    p = p.next_state
                if p.repeat == 'any':
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.token == 'wildcard':
                if self.repeat == 'once':
                    if self.next_state is None:
                        if pos+1 == len(original_str):
                            return True
                        else:
                            return False
                    else:
                        return self.next_state.move(original_str, pos + 1)
                else:
                    if self.next_state is None:
                        return True
                    else:
                        p = self.next_state
                        while p and p.repeat == 'any':
                            p = p.next_state
                        if not p:
                            return True
                        for i in range(pos, len(original_str)):
                            if self.next_state.move(original_str, i):
                                return True
                        return False
            else:
                if self.repeat == 'once':
                    if original_str[pos] == self.value:
                        if self.next_state is None:
                            if pos + 1 == len(original_str):
                                return True
                            else:
                                return False
                        else:
                            return self.next_state.move(original_str, pos + 1)
                    else:
                        return False
                else:
                    if self.next_state is None:
                        for i in range(pos, len(original_str)):
                            if original_str[i] != self.value:
                                return False
                        return True
                    else:
                        if self.next_state.move(original_str, pos):
                            return True
                        else:
                            for i in range(pos, len(original_str)):
                                if original_str[i] == self.value:
                                    if self.next_state.move(original_str, i+1):
                                        return True
                                else:
                                    break
                            return False


s = Solution()
print s.isMatch("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*")
