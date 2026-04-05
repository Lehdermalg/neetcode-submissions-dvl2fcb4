class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # measure how many uppercase ASCII letters we need
        oa = ord("A")
        tab_len = ord("Z") - oa + 1 
        max_count = 0
        max_length = 0
        length = 0
        lwi = 0
        # prepare a counter table
        char_count = [0]*tab_len
        # iterate over the string (moving right window)
        for rwi, c in enumerate(s):
            i = ord(c)-oa
            # increment char counter
            char_count[i] += 1
            # max count and char
            if char_count[i] > max_count:
                max_char = c
                max_count = char_count[i]
            # calculate the total length
            all_count = sum(char_count) 
            length = all_count - max_count
            # if budget not spent
            if length <= k:
                # store max_length
                if max_count > max_length:
                    max_length = max_count
            else:
                # decrease the char count from lwi
                char_count[ord(s[lwi])-oa] -= 1
                # move the left window
                lwi += 1

            print(f"rwi: {rwi}, c: {c}, mc: {max_count}, cc[{i}]:{char_count[i]}, lc: {length}, ml: {max_length}")
        # use budget ONLY if there were changes...
        if all_count > max_length:
            # and only the spendable part of it...
            max_length += min(k, all_count-max_length)
        return max_length          
