from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_s = ""
        result_list = []
        for i in digits:
            string_s += str(i)
        result = int(string_s) + 1
        for i in str(result):
            result_list.append(int(i))
        return result_list
