class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(0,len(s)):
            if s[i+1:len(s):]+s[0:i+1:]==goal:
                return True
        return False
        
