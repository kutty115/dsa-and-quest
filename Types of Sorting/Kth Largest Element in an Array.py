
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        #nums=list(set(nums))
        nums.sort()
        return nums[-k]
        