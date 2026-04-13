class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_frequency(string):
            freq = {}
            for char in string:
                if char not in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1
            return freq

        return get_frequency(s) == get_frequency(t)
        