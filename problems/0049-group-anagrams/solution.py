class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            grouped[sorted_word].append(word)
        return list(grouped.values())