class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res=[0]*n
        s=[]
        p=0
        for log in logs:
            f,t,time=log.split(':')
            f=int(f)
            time=int(time)
            if t=="start":
                if s:
                    res[s[-1]]+=time-p
                s.append(f)
                p=time
            else:
                res[s.pop()]+=time-p+1
                p=time+1
        return res
        
