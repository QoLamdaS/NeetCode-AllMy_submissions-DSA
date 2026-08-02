class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in nums:
            difference = target - i
            if difference == seen:
                return False
            seen.add(i)
        
            
