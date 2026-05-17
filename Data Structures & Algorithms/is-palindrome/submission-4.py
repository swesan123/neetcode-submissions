class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        To read foward and backward, maybe we can do a solution where we delete the spacing, then we create a flip string by
        swapping first and last letters (0 to n-1). second and second last letters (1, n-2). The center letter is a pivot. Maybe 
        actually its simpler to do a sort. Actually that wouldn't work what if its similar words with same characters. We don't 
        need to swap center variable, we only need to swap left and rights. 

        WasitacaroracatIsaw (need to use a .lower() to ignore case)

        instead of checking whole word if its the same, we can simply just swap, then check that index with the orginialwords index, 
        and if it doesn't match just instantly return False. 

        Another pattern I spotted is that palindromes are symmetrical on the central letter, so all i need to do is just flip the second half,
        not whole string. 

        

        pseucdocode:
        s = s.replace(" ", "")
        n = len(s)
        middle = ceil(n-1/2)

        left_half = str[:middle]  # abba, middle = ceil(n-1/2) = ceil(4-1/2) = 2. s[:2] = ab
        right_half = str[middle:]  # abba, s[2:] = ba 

        fliped_right = right_half[::-1]

        if flipped_right == left_half:
            return True
        else: 
            return False
        
        '''
        s = (''.join(c for c in s if c.isalnum())).lower()
        print(s)
        n = len(s)

        
        # 012345 0123456
        # abbbba racecar
        if n % 2 == 0:
            middle = ((n - 1) // 2) + 1
            l = s[:middle]
            r = s[middle:]
        else:
            middle = ((n - 1) // 2) 
            l = s[:middle]
            r = s[middle+1:]
       
        print(l)
        print(r)

        f_r = r[::-1]
        print(f_r)

        return l == f_r
        