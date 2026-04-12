class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)-1
        C = len(matrix[0])-1

        # find zeroes, store their coordinates
        zero_coords = []
        for r in range(R+1):
            for c in range(C+1):
                if matrix[r][c] == 0:
                    zero_coords.append((r,c))
        print(zero_coords)
        # iterate over zero coords, zero others
        for zr,zc in zero_coords:
            for r in range(R+1):
                matrix[r][zc] = 0
            for c in range(C+1):
                matrix[zr][c] = 0
        