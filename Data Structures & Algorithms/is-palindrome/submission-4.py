class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pointers for left and right
        l, r = 0, len(s)-1
        # we move the pointers ignoring non-alphanumeric chars
        while l < r:
            # move left ignoring invalids
            while l < r and not s[l].isalnum():
                l += 1
            # move right ignoring invalids
            while r > l and not s[r].isalnum():
                r -= 1
            # compare the lowercased chars - catching errors early
            if s[l].lower() != s[r].lower():
                return False
            # continue iterating over VALIDS
            l += 1
            r -= 1
        # handling first world problems
        return True            