class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = dict()
        for word in strs:
            temp = word
            word = sorted(word)
            word = "".join(word)
            if word in sol:
                sol[word].append(temp)
            else:
                sol[word] = [temp]
        ret = []
        for vals in sol.values():
            ret.append(vals)
        return ret
