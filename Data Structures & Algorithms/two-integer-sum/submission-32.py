#? Hopefully I still understand this solution code later =)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            difference = target - value #* Calculate the 'compliment' or 'missing piece' we need to reach the target sum.
            if difference in seen: #! Check if we have already encountered this 'difference' before.
                #* If it's in 'seen', we found our matching pair!
                #! seen[difference] gives the index of the previously saved number.
                #! index is the current position we are at right now.
                return [seen[difference], index] 
            seen[value] = index #* If we haven't found the pair yet, record the current number and its index in 'seen' for future iterations to find.
        
            
