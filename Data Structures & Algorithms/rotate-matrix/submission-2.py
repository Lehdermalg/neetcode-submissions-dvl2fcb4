class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # we read the row&col size
        R = len(matrix[0])-1
        C = len(matrix)-1

        # case even (+1+2 <== and odd)
        # we walk the entire matrix element-by-element
        # but we iterate only in the items of one quadrant
        for i in range((R+1)//2):
            for j in range((C+2)//2):
                # 0+i, 0+j   => R-j, 0+i
                # R-j, 0+i   => R-i, C-j
                # R-i, C-j   => 0+j, C-i
                # 0+j, C-i * => 0+i, 0+j
                foo = matrix[i  ][j  ]
                matrix[i  ][j  ] = matrix[R-j][i  ]
                matrix[R-j][i  ] = matrix[R-i][C-j]
                matrix[R-i][C-j] = matrix[j  ][C-i]
                matrix[j  ][C-i] = foo
