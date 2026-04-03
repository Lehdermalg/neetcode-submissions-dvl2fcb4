class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we will zero-in on the correct outcome (uncorrected indices)
        l, r = 0, len(numbers)-1

        while l < r:
            test = numbers[l] + numbers[r]

            # we return the catch
            if test == target:
                return [l+1, r+1]
            
            # to raise the sum, we move l up
            if test < target:
                l += 1

            # to lower the sum, we move r down
            if test > target:
                r -= 1
                
        # if nothing matches
        return [-1, -1]