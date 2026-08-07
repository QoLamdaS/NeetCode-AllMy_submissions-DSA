class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #! Only do quick review with different solution code. I peeking some hints hehehe =)
            for _ in range(i + 1, len(nums)):
                if nums[i] + nums [j] == target:
                    return [i, j]
                    #? TESTING???