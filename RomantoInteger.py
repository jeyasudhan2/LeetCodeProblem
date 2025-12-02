class Solution:
    def romanToInt(self, s: str) -> int:
        result =0
        slength =len(s)
        roamanLetter ={
            "I":1,
            "V":5,
             "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i=0
        while i < slength:
            if i < slength-1 and  ( roamanLetter[s[i]] < roamanLetter[s[i+1]]):
                result += roamanLetter[s[i+1]] -roamanLetter[s[i]]
                i += 2
            else:
                result += roamanLetter[s[i]]
                i+=1
     
        return result
      

solution =Solution()
print(solution.romanToInt("III"))      
print(solution.romanToInt("LVIII"))    
print(solution.romanToInt("MCMXCIV")) 
