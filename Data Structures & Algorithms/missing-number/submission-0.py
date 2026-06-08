class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        list_iter = list(range(0,len(nums)+1))

        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i] ^ list_iter[i]

        ans ^= list_iter[-1]
            
        return ans
