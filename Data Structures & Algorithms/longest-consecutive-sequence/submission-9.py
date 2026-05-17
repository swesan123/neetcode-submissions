class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        
        
        nums_set = set(nums)
        print(f"nums set = {nums}")
        nums = list(nums_set)
        nums.sort()
        print(f"nums sorted = {nums}")
        inc = 1
        max_num = 0

        for i in range(1, len(nums)):
            print(f"nums[i-1] = {nums[i-1]}, nums[i] - 1 = {abs(nums[i]) - 1}")
            if nums[i-1] == nums[i] - 1:
                inc += 1
                print(f"True: inc = {inc}")
            else:
                print(f"False, inc = {inc}, max_num = {max_num}")
                if inc > max_num:
                    max_num = inc
                    print(f"Setting max_num: {max_num}")
                inc = 1
        
        if inc > max_num:
            max_num = inc
            
        return max_num
        