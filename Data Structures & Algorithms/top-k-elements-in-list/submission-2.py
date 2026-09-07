import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}

        for num in nums:
            h[num]=h.get(num,0) + 1
        
        heap=[]

        for num,freq in h.items():
            heapq.heappush(heap,(-freq,num))
        
        ans=[]

        for _ in range(k):
            freq,num = heapq.heappop(heap)
            ans.append(num)
        return ans

        