class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else: 
                frequency[num] = 1

        
        num_arr = []
        for i in range(k):
            print(frequency)
            if len(frequency) > 0:
                max_item = max(frequency.items(), key=lambda x: x[1])
                print(max_item)
                num_arr.append(max_item[0])
                frequency.pop(max_item[0], None)
                print(num_arr)
        print(num_arr)
        return num_arr
