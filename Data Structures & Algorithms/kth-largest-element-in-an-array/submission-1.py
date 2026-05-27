"""
Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Your given an array, you can solve it by sorting array any algo and reversing or keeping it as is and return kth
index or len-kth index that seems too simple though.

Approach
<!-- Describe your approach to solving the problem. -->
Binary Search:
- Needs sorted data
- Searches for a value
- Does not rearrange array
- Time: O(log n)

Quickselect:
- Works on unsorted data
- Searches for kth position/rank
- Rearranges array using partitioning
- Average time: O(n)

You need to rearrange array into smaller than pivot | pivot | larger than pivot. 

If len(larger than pivot ) == k - 1, then pivot is the kth largest value. if its not, pick a pivot
from the larger than pivot array. if < k - 1 then its in the smaller group


[2,3,1,5,4] 
[2,3,1] [4] [5, 6] k = 1

Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

Code
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        sub_num = nums

        while True:
            pivot_index = len(sub_num) // 2
            pivot_num = sub_num[pivot_index]

            larger = []
            smaller = []
            equal = []

            for num in sub_num:
                if num > pivot_num:
                    larger.append(num)
                elif num < pivot_num:
                    smaller.append(num)
                else:
                    equal.append(num)

            # kth largest is in the larger side
            if k <= len(larger):
                sub_num = larger

            # kth largest is the pivot
            elif k <= len(larger) + len(equal):
                return pivot_num

            # kth largest is in the smaller side
            else:
                k -= len(larger) + len(equal)
                sub_num = smaller
                    
            




            



        