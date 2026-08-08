class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #! Just a quick review to defend DSA weakenings to me :/