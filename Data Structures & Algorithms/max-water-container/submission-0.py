"""
length is equal to distance between idx and height as whatever is largest value at that idx.
[1,7,2,5,4,7,3,6]
idx_1 = 7, idx_7 = 6, choose min height so idx_7=6

You have a L and R boundary. [1,7,2,5,4,7,3,6] lets say L = 0, R = len(s) -1. 

we intialize max_water to 0,  try min(height(L), height(R)) * (R-L), if its > than max_water. We set max water to
that water value. We start at ends because thats always maxmimum length. 

if we update L and R depending if max_water is updated let me try this with these numbers. 


"""
class Solution:
   def maxArea(self, heights: List[int]) -> int:
      max_water = 0
      l, r = 0, len(heights) - 1

   
      while l < r:
         
         h_l = heights[l]
         h_r = heights[r]
         min_h = min(h_l, h_r)
         length = r - l
         water = length * min_h

         if water > max_water:
            max_water = water
         if h_l == min_h:
            l += 1

         if h_r == min_h:
            r -= 1

      return max_water




        