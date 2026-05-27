"""
Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Your given an array, you can solve it by sorting array any algo and reversing or keeping it as is and return kth
index or len-kth index that seems too simple though.

Approach
<!-- Describe your approach to solving the problem. -->

Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

Code
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        nums.reverse()
        print(nums)
        return nums[k-1]


        