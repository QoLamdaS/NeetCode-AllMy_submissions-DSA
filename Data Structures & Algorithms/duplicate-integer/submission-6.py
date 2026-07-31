class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False #* It means there is no any duplicate inside the list
        else:
            return True
