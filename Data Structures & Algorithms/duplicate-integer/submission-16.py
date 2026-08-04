class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        #* I understand my solution code a bit effortlessly (Just reviewing only).     