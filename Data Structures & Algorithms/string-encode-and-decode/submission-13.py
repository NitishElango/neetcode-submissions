class Solution:

    def encode(self, strs: List[str]) -> str:
        delimeter = '#'
        ret = []
        for word in strs:
            length = str(len(word))
            formattedword = length + delimeter + word
            ret.append(formattedword)
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        i = 0
        sol = []
        while i in range(len(s)):
            #isolating the length
            length_word = []
            while s[i] != "#":
                length_word.append(s[i])
                i+=1
            length = int("".join(length_word))
            #skip the delimeter
            i+=1
            #read the word of size length
            word = []
            stop = i + length
            while i < stop:
                word.append(s[i])
                i+=1
            sol.append("".join(word))
        print(sol)
        return sol
