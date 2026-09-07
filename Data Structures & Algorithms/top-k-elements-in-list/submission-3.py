import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}

        for num in nums:
            h[num]=h.get(num,0) + 1
        
        heap=[]

        for num,freq in h.items():
            heapq.heappush(heap,(freq,num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans=[]

        for freq,num in heap:
            ans.append(num)
        return ans

        