class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1 
            else:
                d[n] = 1
        maxi = -1
        ans = -1
        for key,value in d.items():
            if value > maxi:
                ans = key
                maxi = value
        return ans



        
        