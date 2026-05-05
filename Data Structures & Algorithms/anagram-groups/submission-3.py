from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result = []
        seen = defaultdict(list)
        for idx, string in enumerate(strs):
            frequency_of_chars = [0] * 26
            for ch in string:
                frequency_of_chars[ord(ch) - ord('a')] += 1
            seen[tuple(frequency_of_chars)].append(string)
        return list(seen.values())

                