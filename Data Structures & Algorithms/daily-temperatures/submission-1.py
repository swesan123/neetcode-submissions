class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        i = 0
        n = 0
        res = [] 
        for currt in temperatures:            
            for t in temperatures[i:]:
                if currt < t: 
                    res.append(n)
                    n = 0
                    break
                n += 1
            if n > 0:
                n = 0 
                res.append(0)
            i += 1   
        return res
        