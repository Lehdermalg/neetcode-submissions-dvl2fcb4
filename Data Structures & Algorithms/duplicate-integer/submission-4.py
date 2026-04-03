class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foo = set()
        for n in nums:
            if n not in foo:
                foo.add(n)
            else:
                return True
        return False