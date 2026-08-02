class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            difference_i = target - i
            for j in nums:
                difference_j = target - i
        if difference_i + difference_j == target:
            return False
        
            
