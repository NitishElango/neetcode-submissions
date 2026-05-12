class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        length = 0
        temp = []
        res = []
        while i < len(s):
            #getting the length
            while s[i] != '#':
                length *=10
                length += int(s[i])
                i+=1
            #skip delimeter
            i+=1
            # getting the actual word
            curr = i
            while i < curr + length and i < len(s):
                temp.append(s[i])
                i +=1
            res.append("".join(temp))
            temp = []
            length = 0
            print(res)
        return res
        
