class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)): #! If lengths match, duplicates don't exist
            return False #* It means there is no any duplicate inside the list
        else:
            return True #* It means there is a duplicate in the list
