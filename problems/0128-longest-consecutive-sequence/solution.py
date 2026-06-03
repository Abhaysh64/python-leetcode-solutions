class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_set = set(nums)
        if len(sorted_set) == 0:
            return 0
        longest = 1
        for num in sorted_set:
            if num-1 not in sorted_set:
                length = 1
                while ( num + length) in sorted_set:
                    length += 1
                longest = max(longest,length)
        return longest

        