class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=Counter(nums)
        t=[]
        for i in range(1,len(nums)+1):
            if d[i]==0:
                t.append(i)
        return t
