class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # measure how many uppercase ASCII letters we need
        oa = ord("A")
        tab_len = ord("Z") - oa + 1 
        max_count = 0
        max_to_change = 0
        to_change = 0
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
                max_count = char_count[i]
            # calculate the total length
            # all_count = sum(char_count)
            all_count = rwi - lwi + 1 
            to_change = all_count - max_count
            # if budget not spent
            if to_change <= k:
                # store max_to_change
                if max_count > max_to_change:
                    max_to_change = max_count
            else:
                # decrease the char count from lwi
                char_count[ord(s[lwi])-oa] -= 1
                # move the left window
                lwi += 1

            print(f"rwi: {rwi}, c: {c}, mc: {max_count}, cc[{i}]:{char_count[i]}, tc: {to_change}, mtc: {max_to_change}")
        # use budget ONLY if there were changes...
        if all_count > max_to_change:
            # and only the spendable part of it...
            max_to_change += min(k, all_count-max_to_change)
        return max_to_change          
