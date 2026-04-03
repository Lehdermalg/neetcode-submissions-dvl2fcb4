class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        return bin(n).count('1')

    def countBits(self, n: int) -> List[int]:
        l = []
        for _ in range(n+1):
            l.append(self.hammingWeight(_))
        return l