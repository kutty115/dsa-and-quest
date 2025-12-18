
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        inn=[]
        arr.sort()
        mabs=arr[1]-arr[0]
        for i in range(len(arr)-1):
            m=abs(arr[i+1]-arr[i])
            if m<mabs:
                mabs=m
                inn.clear()
                inn.append([arr[i],arr[i+1]])
            elif m==mabs:
                inn.append([arr[i],arr[i+1]])
        return inn