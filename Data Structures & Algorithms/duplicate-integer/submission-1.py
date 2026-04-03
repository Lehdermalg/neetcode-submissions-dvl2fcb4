class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = list(set(nums))
        return len(s) != len(nums)