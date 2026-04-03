class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we will iterate over a triangle
        ln = len(nums)
        for i in range(ln):
            # store the diff between target and current number
            diff = target - nums[i]
            # check if any of the later numbers matches
            for j in range(i+1,ln):
                if nums[j] == diff:
                    return [i,j]
        return [-1, -1]
