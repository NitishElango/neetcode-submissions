class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        res = []

        for valu in hashmap.values():
            res.append(valu)
        return res

