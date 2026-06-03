class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1+hashmap.get(num,0)

        return sorted(hashmap,key = lambda num : hashmap[num],reverse = True)[:k]
        

        





        