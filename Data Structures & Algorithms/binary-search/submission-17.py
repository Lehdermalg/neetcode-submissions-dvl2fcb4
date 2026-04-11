class Solution:
    def search(self, nums: List[int], target: int) -> int:
        li = 0
        ri = len(nums)
        lenlist = ri
        s = 0
        # edge case: 0
        if ri == 0:
            return -1

        print(f'step {s}: {li},{ri}')
        # repeat procedure until the left- and right-indices do not match
        while li <= ri:
            # divide the right index in half,
            mid = (ri+li)//2
            if mid >= lenlist:
                return -1
            s +=1
            print(f'step {s}: {li},{mid},{ri}')
            # check the element under the half-len-idx
            # choose half or terminate based on outcome
            if nums[mid] == target:
                # item found
                return mid
            elif nums[mid] > target:
                # move window left
                ri = mid-1
                print(f'step {s}: {li},{mid},{ri}')
            elif nums[mid] < target:
                # move window right
                li = mid+1
                print(f'step {s}: {li},{mid},{ri}')
        # not found
        return -1