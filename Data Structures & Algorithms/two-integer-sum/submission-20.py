class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in nums:
            difference = target - nums[i]
            if difference in enumerate(seen):
                return (difference, i)
            seen.add(nums[i])
        
            
