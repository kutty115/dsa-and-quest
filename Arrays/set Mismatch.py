class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=Counter(nums)
        l=[]
        for i,j in c.items():
            if j==2:
                l.append(i)
        for i in range(1,max(nums)+2):
            if i not in nums:
                l.append(i)
        return [l[0],l[1]]
        
        
