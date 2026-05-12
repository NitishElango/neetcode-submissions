from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        for word in strs:
            word_freq = [0] * 26
            for c in word:
                word_freq[ord(c) - 97] += 1
            word_freq = tuple(word_freq)
            if word_freq in seen:
                seen[word_freq].append(word)
            else:
                seen[word_freq] = [word]
        sol = []
        for val in seen.values():
            sol.append(val)
        return sol