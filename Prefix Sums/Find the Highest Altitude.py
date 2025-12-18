
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0,gain[0]]
        m=0
        for g in range(1,len(gain)):
            res.append(res[g]+gain[g])
        return max(res)
        