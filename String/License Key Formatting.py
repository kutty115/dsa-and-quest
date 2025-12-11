class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        g=s.upper().replace('-','')[::-1]
        e=[]
        for i in range(0,len(g),k):
            e.append(g[i:i+k])
        return '-'.join(e)[::-1]
        
