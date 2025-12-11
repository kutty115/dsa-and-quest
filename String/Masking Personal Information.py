class Solution:
    def maskPII(self, s: str) -> str:
        res=""
        if "@" in s:
            res+=s[0].lower()+"*****"
            i=s.index("@")
            res+=s[i-1].lower()
            res+=s[i::].lower()
        else:
            ph=""
            for ch in s:
                if ch.isdigit():
                    ph+=ch
            if len(ph)==10:
                return "***-***-"+ph[6::]
            if len(ph)==11:
                return "+*-***-***-"+ph[7::]
            if len(ph)==12:
                return "+**-***-***-"+ph[8::]
            if len(ph)==13:
                return "+***-***-***-"+ph[9::]
        return res        
