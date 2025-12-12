class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        
        c=1
        res=a
        while len(res)<len(b):
            res+=a
            c+=1
        if b in res:
            return c
        res+=a
        if b in res:
            return c+1
            
        return -1
        
