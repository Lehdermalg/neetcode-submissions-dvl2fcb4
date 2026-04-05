class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        oa = ord("A")
        char_cnt = [0] * 26
        lwi = 0
        max_frq = 0
        max_len = 0

        # iterate over the string
        for rwi in range(len(s)):
            # count the char in the window
            char_idx = ord(s[rwi]) - oa
            char_cnt[char_idx] += 1

            # store most frequent char
            if char_cnt[char_idx] > max_frq:
                max_frq = char_cnt[char_idx]

            # check budget (R-L+1 = W)
            # W - MF > K
            while (rwi-lwi+1) - max_frq > k:
                # decrease the count of lwi char
                char_cnt[ord(s[lwi])-oa] -= 1
                # move the lwi
                lwi += 1
            
            # calculate window size
            cws = rwi - lwi + 1
            if cws > max_len:
                max_len = cws
        return max_len