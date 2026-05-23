from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def dfs(ind, curr_word):
            if ind >= n:
                if curr_word in wordDict:
                    return True
                else:
                    return False
            else:
                new_word = curr_word + s[ind]
                if new_word in wordDict:
                    return dfs(ind + 1, "") or dfs(ind + 1, new_word)
                else:
                    return dfs(ind + 1, new_word)
        
        n = len(s)
        return dfs(0, "")