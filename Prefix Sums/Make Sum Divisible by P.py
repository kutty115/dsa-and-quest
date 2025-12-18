class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        rem=total%p
        if rem==0:
            return 0
        h={0:-1}
        res=len(nums)
        pr=0
        for i,v in enumerate(nums):
            pr=(pr+v)%p
            n=(pr-rem)%p
            if n in h:
                res=min(res,i-h[n])
            h[pr]=i
        return res if res<len(nums) else -1
            

        
        
