class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res=[]
        j=0
        for num in range(1,n+1):
            if j==len(target):
                break
            if num==target[j]:
                res.append("Push")
                j+=1
            else:
                res.append("Push")
                res.append("Pop")
        return res
        
