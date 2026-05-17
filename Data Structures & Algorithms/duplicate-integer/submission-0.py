class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for x in nums:
            print(num_dict.items())
            if str(x) not in num_dict.keys():
                print("Initializing")
                num_dict[str(x)] = 0
            else: 
                print("Incrementing")
                num_dict[str(x)] += 1
            
        print(num_dict.values())
        for i in num_dict.values():
            print(i)
            if i > 0:
                print(i>0)
                return True
        return False 
    
         