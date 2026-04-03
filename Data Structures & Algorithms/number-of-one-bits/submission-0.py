class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        mask = 1
        for _ in range(32):
            if n & mask:
                hw += 1
            mask <<= 1
        return hw 