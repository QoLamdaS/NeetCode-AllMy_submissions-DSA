class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_sorted = sorted(s)
        # t_sorted = sorted(t)
        if sorted(s) == sorted(t):
            return True
        return False


        