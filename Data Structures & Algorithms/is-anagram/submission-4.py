class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            dict1 = dict()
            for l in s:
                if l in dict1:
                    dict1[l]+=1
                else:
                    dict1[l] = 1
            for l in t:
                if l in dict1:
                    if dict1[l] == 0:
                        return False
                    dict1[l] -=1
                else:
                    return False
            for val in dict1.values():
                if val != 0:
                    return False
            return True

        