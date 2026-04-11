class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lci, rci = 0, len(matrix[0])-1
        lri, rri = 0, len(matrix)-1
        print(f'{lci}:{rci}, {lri}:{rri}')
        # early termination for target not within matrix
        if target < matrix[0][0] or target > matrix[rri][rci]:
            return False

        # find row using first element in row
        while lri <= rri:
            midr = (rri+lri)//2
            if matrix[midr][0] < target:
                if matrix[midr][rci] > target:
                    # target is in this row... time to find the column
                    break
                elif matrix[midr][rci] == target:
                    # target found!
                    return True
                else:
                    # target is not in this row, increment row
                    lri = midr+1
            elif matrix[midr][0] == target:
                # target found!
                return True
            elif matrix[midr][0] > target:
                # target is not in this row, decrement row
                rri = midr-1

        # find column using given row
        while lci <= rci:
            midc = (rci+lci)//2
            if matrix[midr][midc] > target:
                # decrement column
                rci = midc-1
            elif matrix[midr][midc] == target:
                # target found!
                return True
            else:
                # increment row
                lci = midc+1

        return False