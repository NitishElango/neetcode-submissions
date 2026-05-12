class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        c1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 
        'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 
        'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 
        't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        c2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 
        'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 
        'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 
        't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        
        for c in s1:
            c1[c] +=1
        
        l,r = 0 , 0
        #
        while r < len(s2):
            while r - l + 1 <= len(s1):
                c2[s2[r]] +=1
                r+=1
            for key, val in c1.items():
                if val > 0:
                    print(key)
            print("end of c1")
            for key, val in c2.items():
                if val > 0:
                    print(key)
            print("end of c2")
            if c2 == c1:
                return True
            else:
                c2[s2[l]] -=1
                l+=1
        return False