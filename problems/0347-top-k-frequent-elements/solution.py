class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        ans = sorted(hashmap,key = lambda num : hashmap[num],reverse = True)
        return ans[:k]
        