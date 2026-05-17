class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix_prod = 1
        for i in range(len(nums)):
            prefix.append(prefix_prod)
            prefix_prod *= nums[i]

        postfix = []
        post_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix.append(post_prod)
            post_prod *= nums[i]

        postfix.reverse()  # Align with prefix order

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])

        return output

        
        