class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        nums = [3,4,5,6], target = 7

        '''
        
        seen = {}

        for i, num in enumerate(nums):
            diff = target-num # diff = 4; diff = 3

            if diff in seen: # false; true
                return [seen[diff], i] # [0, 1]

            seen[num] = i # seem = [3:0]
        

