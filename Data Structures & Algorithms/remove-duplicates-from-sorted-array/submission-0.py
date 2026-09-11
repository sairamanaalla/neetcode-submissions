class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        count=1
        val = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[j]:
                j +=1
                nums[j] = nums[i]
                count +=1
        return count

            
        