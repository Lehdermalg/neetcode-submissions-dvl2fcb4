class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R = len(matrix[0])-1
        C = len(matrix)-1
        spiral = []
        # 0  , 0   .. R  , 0  
        # R  , 0   .. R  , C  
        # R  , C   .. 0  , C  
        # 0  , C   .. 0  , 0+c
        left, right = 0, R
        top, bottom = 0, C
        # we walk the rectangle rim
        # top
        while left <= right and top <= bottom:
            for r in range(left, right+1):
                spiral.append(matrix[top][r])
            # remove top row
            top +=1

            # right
            for c in range(top, bottom+1):
                spiral.append(matrix[c][right])
            # remove right column
            right -=1

            # early terminate for odd breadth or width
            if not (left <= right and top <= bottom):
                break

            # bottom
            for r in range(right, left-1, -1):
                spiral.append(matrix[bottom][r])
            # remove bottom row
            bottom -=1

            # left
            for c in range(bottom, top-1, -1):
                spiral.append(matrix[c][left])
            # remove left column
            left +=1

        return spiral
            