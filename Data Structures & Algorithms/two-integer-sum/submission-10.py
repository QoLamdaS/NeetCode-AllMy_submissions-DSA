class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            target -= i
            for j in nums:
                target -= j
        if nums[i] + nums [j] == target:
            return False
        
            
