class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ln = len(numbers)
        for li,n in enumerate(numbers):
            diff = target - n
            ri = ln-1
            # find the match's index
            while numbers[ri] >= diff:
                if numbers[ri] == diff:
                    return [li+1, ri+1]
                ri -= 1
        # if nothing matches
        return [-1, -1]        

