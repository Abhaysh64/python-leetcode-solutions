class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        hash_dict = {}

        for i,v in enumerate(sorted_nums):
            if v not in hash_dict:
                hash_dict[v]=i

        ans = []

        for i in nums:
            ans.append(hash_dict[i])

        return ans