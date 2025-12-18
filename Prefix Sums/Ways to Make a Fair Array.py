class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n=len(nums)
        even=[0]*(n+1)
        odd=[0]*(n+1)
        c=0
        for i in range(n):
            even[i+1]=even[i]
            odd[i+1]=odd[i]
            if i%2==0:
                even[i+1]+=nums[i]
            else:
                odd[i+1]+=nums[i]
        for i in range(n):
            even_left=even[i]
            odd_left=odd[i]
            even_right=odd[n]-odd[i+1]
            odd_right=even[n]-even[i+1]
            if even_left+even_right==odd_left+odd_right:
                c+=1
        return c
        
