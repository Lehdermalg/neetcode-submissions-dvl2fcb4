class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we just treat this as one list...
        R = len(matrix)
        C = len(matrix[0])
        li = 0
        ri = R*C - 1

        # find column using given row
        while li <= ri:
            mid = (li+ri)//2
            row = mid // C
            col = mid % C
            val = matrix[row][col]

            if val == target:
                return True
            elif val > target:
                # move window left
                ri = mid-1
            else:
                # move window right
                li = mid+1

        return False