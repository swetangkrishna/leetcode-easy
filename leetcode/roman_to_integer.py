class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
         "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,    
        "I": 1  
        }   
        z = roman[s[len(s)-1]]
        for i in range(len(s)-1):
            if roman[s[i]]>=roman[s[i+1]]:
                z += roman[s[i]]
            else:
                z -= roman[s[i]]
        return z