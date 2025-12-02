class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        d=defaultdict(list)
        for i in range(len(nums)):
            rem=i%n
            d[rem].append(nums[i])
        res=[]
        for k,v in d.items():
            for m in v:
                res.append(m)
        return res