class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # take target - i and see if that number exists in the array 
        # if target = 10 nums_dict = {6, 5, 4} 
        # nums = [3,4,5,6], target = 7
        num_dict = {}
        diff = 0
        i = 0
        j = 0
        for index, num in enumerate(nums): 
            j = index # 1
            print(f"j = {j}")
            diff = target - num # diff = 7 - 4 = 3
            print(f"diff = target - num = {target} - {num} = {diff}")
            if diff in num_dict.values(): # yes 
                print(f"diff in num_dict = {diff} in {num_dict}")
                break 
            else:
                print("diff not in dict, adding element num to dict")
                num_dict[j] = num # {0: 3}
                print(f"num_dict[j] = num, num_dict[{j}] = {num}, num_dict = {num_dict}")
        
        for key, value in num_dict.items():
            if value == diff:
                i = key
                break
        return [i, j]
        
