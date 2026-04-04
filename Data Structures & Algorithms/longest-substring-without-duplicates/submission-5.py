class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # to be sure - all ASCII is 256
        char_i = [-1]*256
        max_length = 0
        li = 0
        double = False
        # go over the string
        for ri, c in enumerate(s):
            oc = ord(c)

            # if the char index is larger than left window index 
            if char_i[oc] >= li:
                # move the left window index to the newer position
                li = char_i[oc] + 1

            # update the char index to right window index (always current index) 
            char_i[oc] = ri

            # calculate the length and store if its maximal
            length = ri - li + 1
            if length > max_length:
                max_length = length
         
        return max_length