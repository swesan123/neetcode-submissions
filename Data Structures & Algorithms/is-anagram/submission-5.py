class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # comparing # of letters +-1 letters
        if len(s) != len(t):
            return False 

        count1 = {}
        count2 = {}
        for letter in s:
            count1[letter] = count1.get(letter, 0) + 1
        for letter in t:
            count2[letter] = count2.get(letter, 0) + 1

        return count1 == count2
   

        
