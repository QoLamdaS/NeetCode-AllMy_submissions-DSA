class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.sorted()
        t = t.sorted()
        if s == t:
            return True
        return False


        