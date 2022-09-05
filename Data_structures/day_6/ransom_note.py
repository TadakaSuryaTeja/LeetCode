class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_list = list(ransomNote)
        magazine_list = list(magazine)

        for i in ransom_list:
            if i not in magazine_list:
                return False
            elif i in magazine_list:
                magazine_list.remove(i)

        return True
