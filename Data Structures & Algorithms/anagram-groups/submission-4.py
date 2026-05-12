from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        char_to_index = {
        'a': 0,  'b': 1,  'c': 2,  'd': 3,  'e': 4,
        'f': 5,  'g': 6,  'h': 7,  'i': 8,  'j': 9,
        'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
        'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
        'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
        'z': 25
        }
        for word in strs:
            word_freq = [0] * 26
            for c in word:
                word_freq[char_to_index[c]] += 1
            word_freq = tuple(word_freq)
            if word_freq in seen:
                seen[word_freq].append(word)
            else:
                seen[word_freq] = [word]
        sol = []
        for val in seen.values():
            sol.append(val)
        return sol