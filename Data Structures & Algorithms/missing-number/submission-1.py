class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i,n in enumerate(nums):
            if n > i:
                return i
        return i+1