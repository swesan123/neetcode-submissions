class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ 
        First we need for loop to iterate through the strs, then another for loop to iterate through 
        string. Need to somehow associate the letter count to each word and store the index of that word. 
        since we need o(n * m) time complexity which is nested for loop. Maybe store letters as keys then index as values.
        Example: {a: {0, 3, 5}, c: {0, 3}, t: {0, 1, 2, 3, 4, 5}, p: {1, 2, 4}, o: {1, 2, 4}, h: {5} }
        Then group by common where i are in the same letters as j:
        [[0,3], ]

        Actually a better method might be sorting. If the word sorted is in the list, add it to the 
        list within the dict of which the word cooresponds to else add word to new index to dict and add 
        element to first index in list. 
        
        {sorted_word: {0, 1}}

        if sorted_word not in anagrams.keys(): 
            


        """
        anagrams = {} # define dict to store anagrams. 
        for index, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if not sorted_word in anagrams.keys():
                anagrams[sorted_word] = [strs[index]]
            else:
                anagrams[sorted_word].append(strs[index])
    
        result = list(anagrams.values())
        return result

        