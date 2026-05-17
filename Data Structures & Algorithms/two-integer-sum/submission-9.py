class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # take a list of numbers make it into a set
        # i,e, (1,2,3,4)
        # enumerate over nums, and take first val (1)
        # subtract target from first val (7-1) = 6
        # Check if that value is is in the set(idx:)
        # if its in the set, return the idx of both.
        # if its not in the set remove that first value, 
        # move onto the next value. 
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums[i+1:]:
                # add i to offset the index from the sublist
                return [i, i + 1 + nums[i+1:].index(diff)]

