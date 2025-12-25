class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def helper(n):
            if n==1:
                return [1]
            left=helper((n+1)//2)
            right=helper(n//2)
            return [2*x-1 for x in left]+[2*x for x in right]
        return helper(n)
        
