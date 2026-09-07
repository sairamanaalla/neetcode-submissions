class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for num in nums:
            if num in h:
                h[num] +=1
            else:
                h[num] = 1
        ans=[]
        for i in range(k):
            top = -1
            val = -1
            for k,v in h.items():
                if v > top:
                    top = v
                    val = k
            ans.append(val)
            h[val]=-1
        return ans
             
        