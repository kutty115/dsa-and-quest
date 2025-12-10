import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[-s for s in stones]
        heapq.heapify(h)
        while len(h)>1:
            first=-heapq.heappop(h)
            second=-heapq.heappop(h)
            if first!=second:
                heapq.heappush(h,-(first-second))
        return -h[0] if h else 0

        