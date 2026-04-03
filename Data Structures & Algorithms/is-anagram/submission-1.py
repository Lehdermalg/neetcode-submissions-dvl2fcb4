class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        for l in s:
            if l in sd.keys():
                sd[l] +=1
            else:
                sd.update({l:1})
        for l in t:
            if l not in sd.keys():
                return False
            sd[l] -= 1
            if sd[l]<0:
                return False
        return True
