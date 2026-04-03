class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we will recall matches
        recall = {}
        ln = len(numbers)
        for li,n in enumerate(numbers):
            diff = target - n
            ri = ln-1
            if diff in numbers:
                # find the match's index
                while ri > li and numbers[ri] != diff:
                    ri -= 1
                return [li+1, ri+1]
        return [-1, -1]        

