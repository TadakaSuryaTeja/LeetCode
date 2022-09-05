from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_values = Counter(t)
        s_values = Counter(s)

        for i, value in t_values.items():
            if i in s_values:
                if value != s_values[i]:
                    return False
            else:
                return False
        return True
