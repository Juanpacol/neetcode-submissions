class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previusMap = {}

        for i , n in enumerate(nums):
            diff=target-n 
            if diff in previusMap:
                return[previusMap[diff],i]
            previusMap[n]=i
        return
