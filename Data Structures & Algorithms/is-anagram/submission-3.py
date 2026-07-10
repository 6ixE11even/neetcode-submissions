class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length of both strings is not same, return False
        if len(s) != len(t):
            return False

        dictT, dictS = {} , {}

        for i in range(len(s)):
            # checks if letter is present in dicts or not and adds its count
            dictS[s[i]] = 1 + dictS.get(s[i],0)
            dictT[t[i]] = 1 + dictT.get(t[i],0)

        for key in dictS:
            if dictS[key] != dictT.get(key,0):
                return False
        
        return True
        