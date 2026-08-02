class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in seen: #? I really so have no idea how to solve this problem. I saw googling solution
                return [seen[difference], index]
            seen[value] = index
        
            
