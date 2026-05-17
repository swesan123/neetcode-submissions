class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # define a list if that number is already in that list 
        # return false 

        x = {}
        for n in nums:
            if n not in x:
                x[n] = 1
            else:
                return True 
        return False 