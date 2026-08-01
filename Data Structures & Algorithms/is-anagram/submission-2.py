class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = s.sorted()
        ta = t.sorted()
        if sa == ta:
            return True
        return False


        