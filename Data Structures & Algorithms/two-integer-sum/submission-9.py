class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums[i] + nums [j] == target:
            return False
        for i in nums:
            target -= i
            for j in nums:
                target -= j
        
            
