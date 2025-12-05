class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=sorted(nums)
        d={}
        for i,n in enumerate(a):
            if n not in d:
                d[n]=i
        res=[]
        for n in nums:
            res.append(d[n])
        return res

        
