class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # let's sort things out first
        nums.sort()
        ln = len(nums)
        triplets = []
        # we will move the left index through and it will be our negative "target"
        
        for li, n in enumerate(nums):
            # after sorting, we can jump over repetitions to avoid duplicates
            if li>0 and n == nums[li-1]:
                continue
            # Here we do the twoSum...
            # start the middle and right indices
            mi, ri = li+1, ln-1
            target = -n

            while mi < ri:
                sum_num = nums[mi] + nums[ri]
                # store match
                if sum_num == target:
                    while mi+1 < ln and nums[mi] == nums[mi+1]:
                        mi += 1
                    triplets.append([n, nums[mi], nums[ri]])
                    mi += 1
                # to raise the sum - increase the leftmost index
                if sum_num < target:
                    mi += 1
                # to lower the sum - decrease the rightmost index
                if sum_num > target:
                    ri -= 1
            
        return triplets