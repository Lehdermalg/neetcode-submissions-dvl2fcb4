class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we will check if the target diff is in the nums
        recall = {}
        for i, n in enumerate(nums):
            diff = target - n
            # if we have seen the diff, we return the indices
            if diff in recall:
                return [recall[diff], i]
            # otherwise we store
            recall[n] = i
        
        # should we have been lied to :D
        return [-1, -1]