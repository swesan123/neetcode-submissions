class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Brainstorm:
        nums is int array 
        k is a int
        return k most frequent elements

        We need to store the count of each number in a hash map, sort the values, so its most to least. so k coresponds to the index of the 
        value.

        Pseudocode: 
        k = num from user
        nums = list of values

        numbers = dict{}

        for n in nums: 
            if n in numbers: 
                numbers[n] += 1 
            else if n not in numbers:
                numbers[n] = 1
        
        numbers.values().sort() # sorts most frequent to least

        return numbers[:k] # returns top k frequent keys i.e. k = 1, numbers[:1] returns numbers[0]
        '''

        numbers = {}
        for n in nums:
            numbers[n] = 1 + numbers.get(n, 0)
        
        sorted_nums = sorted(numbers, key=numbers.get, reverse=True)

        topk = sorted_nums[:k]

        return topk



        