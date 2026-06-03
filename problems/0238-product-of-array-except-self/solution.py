class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1]*len(nums)
        prefix = 1
        for i in range(0,len(nums)):
            prefix_array[i] = prefix
            prefix *= nums[i]
        postfix_array = [1]*len(nums)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            postfix_array[i] = postfix
            postfix *= nums[i]

        ans=[1]*len(nums)

        for i in range(len(nums)):
            ans[i] = prefix_array[i]*postfix_array[i]
        return ans

        