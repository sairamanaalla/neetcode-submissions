class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        val=1
        i=0
        while i < len(nums)-1:
            if nums[i] <= 0 :
                i+=1
                continue
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            if nums[i] == val:
                val +=1
            else:
                return val
            i+=1
        if nums[-1] == val:
            return val+1        
        return val

        