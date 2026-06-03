class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        Pproduct, Sproduct = 1,1
        j = len(nums) - 1
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] *= Pproduct
            ans[j] *= Sproduct
            Pproduct *= nums[i]
            Sproduct *= nums[j]
            j-=1
        
        return ans
        


        