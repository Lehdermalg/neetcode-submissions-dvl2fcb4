class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we get rid of spaces ... because space belongs in SPACE
        s = s.lower()
        p = ''
        for c in s:
            # store only alphanumeric
            if c.isalpha() or c.isnumeric():
                p+=c
        print(p)
        # store the length
        ls = len(p)
        for i in range(ls//2):
            if p[i] != p[ls-i-1]:
                return False
        return True