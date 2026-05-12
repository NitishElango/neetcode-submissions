class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #checking to see if same length
        if len(s) != len(t):
            return False

        #declaring two hashmaps, for each string
        countS, countT = {}, {}
        #iterating through each char in string s, and translating to dictionary
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT