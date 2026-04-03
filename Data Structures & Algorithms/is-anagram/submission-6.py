class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we will use these later
        len_s = len(s)
        oa = ord('a')
        # fail fast - different lengths
        if len_s != len(t):
            return False
        # we count all a-zA-Z characters
        char_count = [0]*26*2
        for i in range(len_s):
            # increment for a letter from first string
            char_count[ord(s[i])-oa] += 1
            # decrement for a letter from second string
            char_count[ord(t[i])-oa] -= 1
        print(char_count)
        # check if any of the counters is off 0
        for i in char_count:
            if i != 0:
                return False
        return True