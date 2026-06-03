class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            ans[tuple(key)].append(str)



        return list(ans.values())