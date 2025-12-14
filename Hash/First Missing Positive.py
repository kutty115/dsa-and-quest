class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        i=1
        for i in range(1,len(nums)+2):
            if i not in s:
                return i
           
        
