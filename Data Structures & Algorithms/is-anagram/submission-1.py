class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False
            else:
                t = t.replace(c, "", 1)
        for c in t:
            if c not in s:
                return False
            else:
                return True
        return True