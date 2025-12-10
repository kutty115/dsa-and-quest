class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1_len=len(nums1)
        counter=1
        pairs=[]
        heap=[]
        for i in range(min(k,nums1_len)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))
        while heap and counter<=k:
            s,i,j=heapq.heappop(heap)
            pairs.append([nums1[i],nums2[j]])
            next_ele=j+1
            if len(nums2)>next_ele:
                heapq.heappush(heap,(nums1[i]+nums2[next_ele],i,next_ele))
            counter+=1
        return pairs
