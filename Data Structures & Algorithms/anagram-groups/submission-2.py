class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = dict()
        sol_list = []
        for word in strs:
            count_word = tuple(sorted(word))
            if count_word in sol:
                sol[count_word].append(word)
            else:
                sol[count_word] = [word]
        for val in sol.values():
            sol_list.append(val)
        return sol_list

            