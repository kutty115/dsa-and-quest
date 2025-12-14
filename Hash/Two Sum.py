class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i,val in enumerate(nums):
            diff=target-val
            if diff in res:
                return [res[diff],i]
            res[val]=i
        #return 
            
        