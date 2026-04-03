class Solution:
    def reverseBits(self, n: int) -> int:
        rev = f"{n:032b}"[::-1]
        # print(rev)
        # print(int(rev,2))
        return int(rev,2)