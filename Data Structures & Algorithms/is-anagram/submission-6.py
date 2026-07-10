class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # most optimal solution is static array implementation

        # sanity check:
        if len(s) != len(t):
            return False

        # Step 1: create a 26 character sized 0 array for each character
        alphabets = [0] * 26

        # Loop using any string's length
        # for character in str S- we increment
        # for character in str T- we decrement
        for i in range(len(s)):
            alphabets[(ord(s[i]) - ord('a'))] += 1
            alphabets[(ord(t[i]) - ord('a'))] -= 1
        
        for count in alphabets:
            if count != 0:
                return False
        
        return True