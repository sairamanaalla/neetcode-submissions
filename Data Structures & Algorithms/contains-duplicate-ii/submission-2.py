class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        h={}
        for i in range(n):
            if nums[i] in h and (i-h[nums[i]]) <=k:
                return True
            
            h[nums[i]] = i
            
        return False
            




        