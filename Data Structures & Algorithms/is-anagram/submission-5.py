class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        if ls != len(t):
            return False
        counts =[0]*26
        oa = ord('a')
        for c in range(ls):
            counts[ord(s[c])-oa]+=1
            counts[ord(t[c])-oa]-=1
        for c in counts:
            if c != 0:
                return False
        return True
