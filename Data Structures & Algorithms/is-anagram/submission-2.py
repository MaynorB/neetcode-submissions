class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False
            else:
                t = t.replace(c, "", 1)
        if len(t) > 0:
            return False
        return True