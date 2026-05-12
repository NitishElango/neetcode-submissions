class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            sol[sorted_word].append(word)
        return sol.values()
            

         
                
        
                 