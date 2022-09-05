from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_values = Counter(s)
        list_keys = []
        for key, value in s_values.items():
            if value == 1:
                list_keys.append(key)

        if len(list_keys) == 0:
            return -1

        for i in range(len(s)):
            if s[i] == list_keys[0]:
                return i
