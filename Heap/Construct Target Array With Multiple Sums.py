import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total=sum(target)
        target=[-x for x in target]
        heapq.heapify(target)
        while True:
            largest=-heapq.heappop(target)
            rest=total-largest
            if largest==1 or rest==1:
                return True
            if rest==0 or largest<=rest:
                return False
            prev=largest%rest
            if prev==0:
                return False
            total=rest+prev
            heapq.heappush(target,-prev)
     
    
     
