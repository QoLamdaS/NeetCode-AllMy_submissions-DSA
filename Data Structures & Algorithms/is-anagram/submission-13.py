class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #! Bcs "==" operator in Py naturally returns a boolean [True or False]

        