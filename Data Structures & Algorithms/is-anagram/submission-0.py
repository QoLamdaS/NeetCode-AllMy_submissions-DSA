class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s.sorted() == t.sorted():
            return True
        return False


        