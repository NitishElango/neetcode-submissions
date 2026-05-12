class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
        for i in t:
            if i in hashmap:
                hashmap[i]-=1
            else:
                return False
        for i in hashmap.values():
            if i!=0:
                return False
        return True
