class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        previushash = {}

        for i , n in enumerate(nums): 
            diff= target - n
            if diff in previushash:
                return[previushash[diff], i]
            else:
                previushash[n]=i


